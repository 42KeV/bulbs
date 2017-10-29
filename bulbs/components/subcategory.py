from bulbs.components import db

from bulbs.components.user import username_from_id


def last_post(subcategory_id, parent_post=None):
    """Return the last post from a forum. If parent_post is not None, return last post data from a thread."""
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
            #"SELECT user_id, id \
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
    
def subcat_moderators(subcategory_id):
    """Return a list of moderators for the specified forum."""
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT subcat_id, user_id, username FROM bulbs_Moderator \
             WHERE subcat_id = %s", (subcategory_id, ))
        mods = cursor.fetchone()[0]
    except TypeError as e:
        return None # no moderators for the forum in question
        
    return list(mods)
    
def subcat_title_from_id(subcategory_id):
    """Return the title corresponding to the subcategory id."""
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT title FROM bulbs_Subcategory WHERE id = %s", (subcategory_id, ))
        title = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get subcat name from id, ", e)
        
    return title
    
def number_of_posts(forum_id):
    """Return the number of posts in a subcategory."""
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT count(id) FROM bulbs_Post WHERE subcategory_id = %s \
             AND parent_post IS NOT NULL", (forum_id, ))
        posts = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get amount of posts, ", e)
        
    return posts
    
def number_of_threads(forum_id):
    """Return the number of threads in a subcategory."""
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT count(id) FROM bulbs_Post WHERE subcategory_id = %s \
             AND parent_post IS NULL", (forum_id, ))
        views = cursor.fetchone()[0]
    except Exception as e:
        raise ValueError("failed to get amount of threads, ", e)
        
    return views