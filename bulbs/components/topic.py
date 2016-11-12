from bulbs.components import db
from html.parser import HTMLParser
from slugify import slugify


class PostParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.parsing_script = False
        self.content = []
        
    def handle_starttag(self, tag, attrs):
        print (tag, attrs)
        if tag == "script":
            self.parsing_script = True
        self.content.append("<{0}>".format(tag))
            
    def handle_endtag(self, tag):
        if tag == "script":
            self.parsing_script = False
        self.content.append("</{0}>".format(tag))
            
    def handle_data(self, data):
        if not self.parsing_script:
            data = data.replace("\r\n", "<br>")
        self.content.append(data)
            
    def script_content(self):
        return self.script_body
    
    def parsed_content(self):
        return self.content
        
def format_post(message):
    parser = PostParser()
    parser.feed(message)
    
    return "".join(parser.parsed_content())

def append_id_to_slug(slug, id):
    if id == 0:
        return slug
        
    id_slug = "{0}-{1}".format(slug, id)
    
    return id_slug
    
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
    
def create_topic(subject, content, subcategory_id, ip, username):
    """Creates a thread in the specified subcategory."""

    cursor = db.con.cursor()
    formatted_post = format_post(content)

    cursor.execute("SELECT id FROM bulbs_user WHERE username = %s", (username, ))
    
    try:
        user_id = cursor.fetchone()[0]
    except TypeError as e:
        print ("user id not found, ", e)
        return
        
    cursor.execute("\
        INSERT INTO bulbs_post (subcategory_id, title, content, ispoll, date, user_id, ip, parent_post, latest_reply, isLocked) VALUES \
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
    
    # we return the thread slug so the user can be redirected to it
    return topic_slug
