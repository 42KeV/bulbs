from bulbs.resources import helpers
from bulbs.resources import connection
from pyramid.view import view_config
from pyramid.response import Response
from itertools import chain


def topic_content(cursor, thread_id, page):
    def metainfo(user_id):
        keys = "username", "user_title", "karma", "avatar", "post_count"
        
        cursor.execute(
            "SELECT username, title, karma, avatar FROM bulbs_user WHERE id = %s",
                (user_id, )
        )
        profile = cursor.fetchone()
        
        cursor.execute(
            "SELECT count(*) FROM bulbs_post WHERE user_id = %s", (user_id, )
        )
        postcount = cursor.fetchone()[0]
        
        datatuples = profile, (postcount, )
        data = list(chain.from_iterable(datatuples))
        keys_values = zip(keys, data)
        
        return dict(keys_values)
        
    def postinfo(post):
        keys = "id", "subcat_id", "user_id", "title", "content", "date", "ip"
        user_id = post[2]
        
        meta = metainfo(user_id)
        keys_values = zip(keys, post)
        
        return dict(keys_values, **meta)

    def postrange(page, thread_id):
        postlimit = 15 # max 15 posts per page
        startindex = page*postlimit-postlimit # grab the appropiate posts for the page
        
        cursor.execute(
            "SELECT id, subcategory_id, user_id, title, content, \
            to_char(date, 'Mon FMDD, YYYY HH:MI'), ip FROM bulbs_post \
            WHERE id = %s OR parent_post = %s ORDER BY date LIMIT %s OFFSET %s",
                (thread_id, thread_id, postlimit, startindex)
        )
        
        posts = cursor.fetchall()
        
        return posts
        
    data = postrange(page, thread_id)
    content = map(postinfo, data)
    
    return content


@view_config(route_name='topic', renderer='topic-view.mako')
def main(request):
    """ This view function is called when a thread is opened and returns the posts """
    slug = {
        "cat": request.matchdict.get("cat_slug"),
        "subcat": request.matchdict.get("subcat_slug"),
        "topic": request.matchdict.get("topic_slug")
    }
    
    cursor = connection.con.cursor()
    cursor.execute("SELECT id FROM bulbs_post WHERE slug = %s AND parent_post IS NULL", (slug.get("topic"), ))
    
    try:
        thread_id = cursor.fetchone()[0]
    except Exception as e:
        return Response("Invalid thread ID specified")
        
    rootpost = helpers.is_root_post(cursor, thread_id)
    
    if not rootpost:
        return Response("Invalid thread ID specified")
        
    page_id = request.params.get("page")
    page = 1 if page_id is None else int(page_id)
        
    content = list(topic_content(cursor, thread_id, page))

    subcategory_id = content[0]["subcat_id"]
    subcategory_title = helpers.subcategory_title_from_id(cursor, subcategory_id)  
    
    cursor.execute("SELECT title from bulbs_Post WHERE id = %s", (thread_id, ))
    topic_title = cursor.fetchone()[0]
    
    cursor.execute("UPDATE bulbs_PostView SET views = views + 1 WHERE post_id = %s", (thread_id, ))
    connection.con.commit()
    
    cursor.execute("SELECT isLocked from bulbs_Post WHERE id = %s", (thread_id, ))
    thread_locked = cursor.fetchone()[0]

    return {
        'project': request.registry.settings.get("site_name"),
        'title': topic_title,
        'slug': slug,
        'topic_id': thread_id,
        'subcat_name': subcategory_title,
        'session': request.session,
        'posts': content,
        'thread_is_locked': thread_locked,
        'pages': helpers.thread_pages(cursor, page)
    }
