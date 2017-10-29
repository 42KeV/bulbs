from pyramid import threadlocal
from psycopg2.extensions import AsIs
from slugify import slugify

from bulbs.components import db


def generate_slug(data, id, table):
    """Return a slug."""
    slug = slugify(data)
    cursor = db.con.cursor()
    
    # sqlite3
    #cursor.execute(
    #    "SELECT exists(SELECT 1 FROM {} WHERE slug=?)".format(table), (slug,)
    #)
    
    cursor.execute(
        "SELECT exists(SELECT true FROM %s WHERE slug=%s)", (AsIs(table), slug))
    slug_exists = cursor.fetchone()[0]
    
    if not slug_exists or id == 0:
        return slug

    return "{0}-{1}".format(slug, id)
    
def is_root_post(post_id):
    """Return True if the post_id doesn't have a parent (This means this is the first post in a topic)."""
    try:
        cursor = db.con.cursor()
        cursor.execute("SELECT parent_post FROM bulbs_Post WHERE id = %s", (post_id, ))
        parent_id = cursor.fetchone()[0]
    except TypeError:
        # the post_id specified doesn't exist
        return False
        
    return True
    