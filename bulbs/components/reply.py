from slugify import slugify

from bulbs.components import db
from bulbs.components.post import format_post


def reply_to_topic(subject, content, topic_id, ip, username):
    """Creates a reply in the specified topic."""
    formatted_post = format_post(content)
    cursor = db.con.cursor()

    cursor.execute("SELECT subcategory_id FROM bulbs_post WHERE id = %s", (topic_id, ))
    subcat_id = cursor.fetchone()[0]      
    
    cursor.execute("SELECT id FROM bulbs_user WHERE username = %s", (username, ))
    user_id = cursor.fetchone()[0]

    post_slug = slugify(subject)

    cursor.execute("\
        INSERT INTO bulbs_Post (subcategory_id, parent_post, title, content, date, user_id, ip, slug) VALUES \
        (%s, %s, %s, %s, now(), %s, %s, %s)", (
            subcat_id, 
            topic_id, 
            subject, 
            formatted_post, 
            user_id,
            ip, 
            post_slug
        ))

    cursor.execute("UPDATE bulbs_Post SET latest_reply = now() WHERE id = %s", (topic_id, ))
    db.con.commit()
    
    return True