from pyramid.view import view_config
from bulbs.components.subcategory import number_of_threads, number_of_posts, last_post
from bulbs.components import db


def catinfo(cat):
    keys = "id", "title", "desc", "slug"
    keys_values = zip(keys, cat)
    return dict(keys_values)

def categories():
    """Return a dict containing all categories."""
    cursor = db.con.cursor()
    cursor.execute("SELECT id, title, description, slug FROM bulbs_category")
    cats = cursor.fetchall()        
    data = map(catinfo, cats)
    return data

def subcatinfo(data):
    keys = "id", "title", "category_id", "desc", "slug"
    keys_values = zip(keys, data)
    id = data[0]
    return dict(keys_values,
        id=id,
        threads=number_of_threads(id),
        posts=number_of_posts(id),
        last_post=last_post(id)
    )

def subcategories(cat_id=None):
    """Return a dict containing information from a specified category or forums for every category."""
    cursor = db.con.cursor()
    if cat_id is not None:
        cursor.execute(
            "SELECT id, title, category_id, description, slug FROM bulbs_subcategory \
             WHERE category_id = %s", (cat_id, ))
    else:
        cursor.execute(
            "SELECT id, title, category_id, description, slug FROM bulbs_subcategory")
    children = cursor.fetchall()        
    subcategories_ = map(subcatinfo, children)
    return subcategories_

@view_config(route_name="home", renderer="home.mako")
def response(request):
    cursor = db.con.cursor()
    cats = categories()
    subcats = list(subcategories())
    cursor.execute("SELECT username FROM bulbs_user ORDER BY date DESC LIMIT 1")
    newest_user = cursor.fetchone()[0]        
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Home",
        "categories": cats,
        "subcategories": subcats,
        "new_member": newest_user
    }
