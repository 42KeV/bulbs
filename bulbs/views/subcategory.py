from pyramid.view import view_config
from bulbs.components import helpers
from bulbs.components import db


def topics(cursor, subcategory_id, page):
    thread_limit = 30
    start_position = page * thread_limit - thread_limit
    
    cursor.execute(
        "SELECT id, title, user_id, isLocked, slug FROM bulbs_Post \
         WHERE subcategory_id = %s AND parent_post IS NULL ORDER BY latest_reply \
         DESC LIMIT %s OFFSET %s", (subcategory_id, thread_limit, start_position)
    )

    def topicinfo(thread):
        keys = "id", "title", "user_id", "is_locked", "slug"
        keys_values = zip(keys, thread)
        
        def statinfo(stat):
            keys = "views", "replies", #"last_post"
            keys_values = zip(keys, stat)
            
            return dict(keys_values)
            
        thread_id = thread[0]
        user_id = thread[2]
        stats = (helpers.number_of_views(cursor, thread_id),
            helpers.number_of_replies(cursor, thread_id)
            #d_helpers.last_post(cursor, None, parent_post=thread_id)
        )
        
        return dict(keys_values,
            author=helpers.username_from_id(cursor, user_id),
            last_post=helpers.last_post(cursor, None, parent_post=thread_id),
            stats=statinfo(stats)
        )

    threads = cursor.fetchall()
    content = map(topicinfo, threads)
    
    return content

@view_config(route_name="subcategory", renderer="subcat-view.mako")
def response(request):
    """ This takes a subcategory slug and returns all of its threads, replies and views """
    page_id = request.params.get("page")
    
    try:
        page = 1 if page_id is None else int(page_id)
    except Exception:
        print ("String was passed for page_id")
        
    slugs = {
        "cat": request.matchdict["cat_slug"],
        "subcat": request.matchdict["subcat_slug"]
    }
    
    cursor = db.con.cursor()
    cursor.execute("SELECT id FROM bulbs_subcategory WHERE slug = %s", 
        (slugs.get("subcat"), ))
    
    try:
        subcategory_id = cursor.fetchone()[0]
    except Exception:
        return Response("Invalid subcategory slug")
        
    try:
        threads = topics(cursor, subcategory_id, page)
        title = helpers.subcategory_title_from_id(cursor, subcategory_id)
        moderators = helpers.subcategory_moderators(cursor, subcategory_id)
    except ValueError as e:
        raise ValueError("invalid subcategory id passed")
          
    return {
        "project": request.registry.settings.get("site_name"),
        "slugs": slugs,
        "title": title,
        "threads": threads,
        "subcat_name": title,
        "subcat_id": subcategory_id,
        "session": request.session,
        "moderators": moderators
    }

