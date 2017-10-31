from pyramid import threadlocal
from slugify import slugify

from bulbs.components import db
from bulbs.components.post import format_post


def append_id_to_slug(slug, id):
    if id == 0:
        return slug
    id_slug = "{0}-{1}".format(slug, id)
    return id_slug

def create_topic(subject, content, subcategory_id, ip, username):
    """Create a thread in the specified subcategory."""
    cursor = db.con.cursor()
    formatted_post = format_post(content)

    cursor.execute("SELECT id FROM bulbs_user WHERE username = %s", (username, ))
    
    try:
        user_id = cursor.fetchone()[0]
    except TypeError as e:
        print ("user id not found, ", e)
        return
        
    cursor.execute("\
        INSERT INTO bulbs_post (subcategory_id, title, content, ispoll, date, user_id, ip, parent_post, latest_reply, islocked) VALUES \
        (%s, %s, %s, false, now(), %s, %s, NULL, now(), false)", (
            subcategory_id,
            subject,
            formatted_post, 
            user_id, 
            ip,
        ))

    cursor.execute("SELECT id FROM bulbs_post WHERE user_id = %s ORDER BY date DESC", (user_id, ))
    new_topic_id = cursor.fetchone()[0]

    topic_slug = append_id_to_slug(slugify(subject), new_topic_id)
    
    cursor.execute("UPDATE bulbs_post SET slug = %s WHERE id = %s", (topic_slug, new_topic_id))
    cursor.execute("INSERT INTO bulbs_postview (post_id, views) VALUES (%s, 0)", (new_topic_id, ))
    db.con.commit()
    
    # Return the topic slug so the user can be redirected to it
    return topic_slug

    
def thread_pages(thread_id):
    """Return the amount of pages a thread has."""
    registry = threadlocal.get_current_registry()
    limit = int(registry.settings.get("posts_per_page"))
    
    cursor = db.con.cursor()
    cursor.execute(
        "SELECT count(*) FROM bulbs_Post WHERE id = %s OR parent_post = %s",
            (thread_id, thread_id))
    total_rows = cursor.fetchone()[0]
    pages = int(total_rows / limit if total_rows % limit == 0  else (total_rows / limit) + 1)
    return pages

def number_of_replies(thread_id):
    """Return the number of replies in a thread."""
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT count(id) FROM bulbs_Post WHERE parent_post = %s", 
                (thread_id, ))
        replies = cursor.fetchone()[0]
    except ValueError as e:
        raise ValueError("failed to get amount of thread replies, ", e)
    return replies
    
def number_of_views(thread_id):
    """Return the number of views in a thread."""
    try:
        cursor = db.con.cursor()
        cursor.execute(
            "SELECT views FROM bulbs_PostView WHERE post_id = %s", (thread_id, ))
        views = cursor.fetchone()[0]
    except ValueError as e:
        raise ValueError("failed to get amount of thread views, ", e)
    return views
    
    