from pyramid import threadlocal
from pyramid.view import view_config
from pyramid.response import Response

from bulbs.components import helpers
from bulbs.components import db

from bulbs.components.subcategory import subcat_title_from_id
from bulbs.components.topic import thread_pages

def userinfo(userid):
    """Return a dict containing profile information corresponding to the user id specified."""
    keys = "username", "title", "karma", "avatar", "post_count"
    cursor = db.con.cursor()
    cursor.execute("SELECT username, title, karma, avatar FROM bulbs_user WHERE id = %s",
                    (userid, ))
    profile = list(cursor.fetchone())
    try:
        cursor.execute("SELECT count(*) FROM bulbs_post WHERE user_id = %s",
                        (userid, ))
        postcount = cursor.fetchone()[0]
    except Exception as e:
        print (e)
        raise SystemError("what the hELL")
    profile.append(postcount)
    keys_values = zip(keys, profile)
    return dict(keys_values)

def postinfo(post):
    """Return a dict containing information about a post."""
    keys = "id", "subcat_id", "user_id", "title", "content", "date", "ip"
    userid = post[2]
    author = userinfo(userid)
    keys_values = zip(keys, post)
    return dict(keys_values, **author)

def pageposts(page, thread_id):
    """Return a list of tuples containing the posts to be displayed for the specified page number in a thread."""
    registry = threadlocal.get_current_registry()
    limit = int(registry.settings.get("posts_per_page"))
    startindex = page*limit-limit
    cursor = db.con.cursor()
    cursor.execute("SELECT id, subcategory_id, user_id, title, content, \
                    to_char(date, 'Mon FMDD, YYYY HH:MI'), ip FROM bulbs_post \
                    WHERE id = %s OR parent_post = %s ORDER BY date LIMIT %s OFFSET %s",
                    (thread_id, thread_id, limit, startindex))
    posts = cursor.fetchall()
    return posts

@view_config(route_name='topic', renderer='topic.mako')
def response(request):
    slugs = {
        "cat": request.matchdict.get("cat_slug"),
        "subcat": request.matchdict.get("subcat_slug"),
        "topic": request.matchdict.get("topic_slug")
    }
    cursor = db.con.cursor()
    
    try:
        cursor.execute("SELECT id FROM bulbs_post WHERE slug = %s AND parent_post IS NULL", (slugs.get("topic"), ))
        topic_id = cursor.fetchone()[0]
    except Exception as e:
        return Response("Invalid thread ID specified")

    page_id = request.params.get("page")
    page = 1 if page_id is None else int(page_id)
    
    data = pageposts(page, topic_id)
    content = list(map(postinfo, data))
    
    subcat_id = content[0]["subcat_id"]
    subcat_title = subcat_title_from_id(subcat_id)  
    
    cursor.execute("SELECT title from bulbs_Post WHERE id = %s", (topic_id, ))
    topic_title = cursor.fetchone()[0]
    
    cursor.execute("UPDATE bulbs_PostView SET views = views + 1 WHERE post_id = %s", (topic_id, ))
    db.con.commit()

    return {
        "project": request.registry.settings.get("site_name"),
        "title": topic_title,
        "slugs": slugs,
        "topic_id": topic_id,
        "subcat_name": subcat_title,
        "posts": content,
        "pages": thread_pages(topic_id)
    }
