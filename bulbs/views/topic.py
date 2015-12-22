from pyramid import threadlocal
from pyramid.view import view_config
from pyramid.response import Response
from bulbs.components import helpers
from bulbs.components import db


def posterinfo(user_id):
    ''' returns a dict of profile information for the user id specified in the argument '''

    keys = "username", "title", "karma", "avatar", "post"
    cursor = db.con.cursor()
    cursor.execute(
        "SELECT username, title, karma, avatar FROM bulbs_user WHERE id = %s",
        (user_id, ))
    profile = list(cursor.fetchone())
        
    try:
        cursor.execute(
            "SELECT count(*) FROM bulbs_post WHERE user_id = %s", (user_id, ))
        posts = cursor.fetchone()[0]
    except Exception as e:
        # user id specified wasn't found
        print (e)
        raise SystemError("what the hELL")

    profile.append(posts)
    keys_values = zip(keys, profile)

    return dict(keys_values)

def postinfo(post):
    keys = "id", "subcat_id", "user_id", "title", "content", "date", "ip"
    user_id = post[2]
    author = posterinfo(user_id)
    keys_values = zip(keys, post)

    return dict(keys_values, **author)

def page_posts(page, thread_id):
    ''' returns a list of tuples of all the posts that should be displayed for the specified page number of a thread '''

    registry = threadlocal.get_current_registry()
    limit = int(registry.settings.get("posts_per_page"))

    start_index = page*limit-limit
    cursor = db.con.cursor()
    cursor.execute(
        "SELECT id, subcategory_id, user_id, title, content, \
        to_char(date, 'Mon FMDD, YYYY HH:MI'), ip FROM bulbs_post \
        WHERE id = %s OR parent_post = %s ORDER BY date LIMIT %s OFFSET %s",
        (thread_id, thread_id, limit, start_index)
    )
    posts = cursor.fetchall()

    return posts

@view_config(route_name='topic', renderer='topic-view.mako')
def response(request):
    ''' This view function is called when a thread is opened and returns the posts '''

    slug = {
        "cat": request.matchdict.get("cat_slug"),
        "subcat": request.matchdict.get("subcat_slug"),
        "topic": request.matchdict.get("topic_slug")
    }
    
    cursor = db.con.cursor()

    try:
        cursor.execute("SELECT id FROM bulbs_post WHERE slug = %s AND parent_post IS NULL", (slug.get("topic"), ))
        topic_id = cursor.fetchone()[0]
    except Exception as e:
        return Response("Invalid thread ID specified")
        
    root_post = helpers.is_root_post(topic_id)
    
    if not root_post:
        return Response("Invalid thread ID specified")
        
    page_id = request.params.get("page")
    page = 1 if page_id is None else int(page_id)
    data = page_posts(page, topic_id)
    content = list(map(postinfo, data))

    subcat_id = content[0]["subcat_id"]
    subcat_title = helpers.subcat_title_from_id(subcat_id)  
    
    cursor.execute("SELECT title from bulbs_Post WHERE id = %s", (topic_id, ))
    topic_title = cursor.fetchone()[0]
    
    cursor.execute("UPDATE bulbs_PostView SET views = views + 1 WHERE post_id = %s", (topic_id, ))
    db.con.commit()

    return {
        'project': request.registry.settings.get("site_name"),
        'title': topic_title,
        'slug': slug,
        'topic_id': topic_id,
        'subcat_name': subcat_title,
        'posts': content,
        'pages': helpers.thread_pages(topic_id)
    }
