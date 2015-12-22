from pyramid import threadlocal
from bulbs.components import db
from psycopg2.extensions import AsIs
from slugify import slugify


def generate_slug(data, id, table):
    slug = slugify(data)
    cursor = db.con.cursor()
    cursor.execute(
        "SELECT exists(SELECT true FROM %s WHERE slug=%s)", (AsIs(table), slug))
    slug_exists = cursor.fetchone()[0]
    
    if not slug_exists or id == 0:
        return slug

    return "{0}-{1}".format(slug, id)

def username_from_id(user_id):
    ''' Returns the username corresponding to the user id '''

    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT username FROM bulbs_User WHERE id = %s", (user_id, ))        
        username = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get username, ", e)
        
    return username
    
def number_of_threads(forum_id):
    ''' Returns the number of threads in a specific forum '''

    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT count(id) FROM bulbs_Post WHERE subcategory_id = %s \
             AND parent_post IS NULL", (forum_id, ))
        views = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get amount of threads, ", e)
        
    return views
    
def number_of_posts(forum_id):
    ''' Returns the number of posts in a specific forum '''
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT count(id) FROM bulbs_Post WHERE subcategory_id = %s \
             AND parent_post IS NOT NULL", (forum_id, ))
        posts = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get amount of posts, ", e)
        
    return posts
    
def number_of_views(thread_id):
    ''' Returns the number of views in a specific thread '''

    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT views FROM bulbs_PostView WHERE post_id = %s", (thread_id, ))
        views = cursor.fetchone()[0]
    except ValueError as e:
        raise ValueError("failed to get amount of thread views, ", e)
        
    return views
    
def number_of_replies(thread_id):
    ''' Returns the number of replies in a specific thread '''

    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT count(id) FROM bulbs_Post WHERE parent_post = %s", 
                (thread_id, ))
        replies = cursor.fetchone()[0]
    except ValueError as e:
        raise ValueError("failed to get amount of thread replies, ", e)

    return replies
    
def subcat_title_from_id(subcategory_id):
    ''' Returns the title corresponding to the subcategory id '''

    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT title FROM bulbs_Subcategory WHERE id = %s", (subcategory_id, ))
        title = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get subcat name from id, ", e)
        
    return title
    
def subcat_moderators(subcategory_id):
    ''' Returns a list of moderators in a specific forum '''

    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT subcat_id, user_id, username FROM bulbs_Moderator \
             WHERE subcat_id = %s", (subcategory_id, ))
        mods = cursor.fetchone()[0]
    except TypeError as e:
        return None # no moderators for the forum in question
        
    return list(mods)
    
def last_post(subcategory_id, parent_post=None):
    '''Returns the last post from a specific forum. If parent_post is not None, returns last post data from a thread'''
    #parent_post is set to None by default, if parent post is provided then we'll return the last post data for a thread
    
    cursor = db.con.cursor()

    if parent_post is not None:
        cursor.execute(
            "SELECT user_id, to_char(date, 'Mon FMDD, YYYY HH:MI AM') FROM bulbs_post \
             WHERE parent_post = %s ORDER BY date DESC LIMIT 1", (parent_post, )
         )
         
        data = cursor.fetchone()
    else:
        cursor.execute(
            "SELECT user_id, to_char(date, 'Mon FMDD, YYYY HH:MI AM'), id \
             FROM bulbs_post WHERE subcategory_id = %s ORDER BY date DESC LIMIT 1",
                 (subcategory_id, )
         )
         
        data = cursor.fetchone()
            
    if data is None:
        return None
    
    last_post = {
        "user_id": data[0],
        "date":    data[1]
    }

    last_post["username"] = username_from_id(last_post["user_id"])
    
    if parent_post is not None: 
        # this is true if this function was queried for a thread
        # no other information is required to display for a thread so we return the dict
        return last_post
    
    last_post["post_id"] = data[2] 
    
    try:
        cursor.execute(
            "SELECT parent_post FROM bulbs_Post WHERE subcategory_id = %s ORDER BY date \
             DESC LIMIT 1", (subcategory_id, )
         )
         
        last_post["root_id"] = cursor.fetchone()[0]
    except TypeError as e:
        cursor.execute(
            "SELECT id FROM bulbs_Post WHERE subcategory_id = %s ORDER BY date \
             DESC LIMIT 1", (forum_id, )
         )
         
        last_post["root_id"] = cursor.fetchone()[0]
        
    return last_post
    
def is_root_post(post_id):
    ''' Returns True if the post_id doesn't have a parent (is first post in a topic) '''

    try:
        cursor = db.con.cursor()
        cursor.execute("SELECT parent_post FROM bulbs_Post WHERE id = %s", (post_id, ))
        parent_id = cursor.fetchone()[0]
    except TypeError:
        # the post_id specified doesn't exist
        return False
        
    return True
    
def thread_pages(thread_id):
    ''' Returns the amount of pages a thread should have '''
    registry = threadlocal.get_current_registry()
    limit = int(registry.settings.get("posts_per_page"))

    cursor = db.con.cursor()
    cursor.execute(
        "SELECT count(*) FROM bulbs_Post WHERE id = %s OR parent_post = %s",
            (thread_id, thread_id))
    total_rows = cursor.fetchone()[0]
    pages = int(total_rows / limit if total_rows % limit == 0  else (total_rows / limit) + 1)
   
    return pages
