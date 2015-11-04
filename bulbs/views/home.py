from bulbs.components import db
from bulbs.components import helpers
from pyramid.view import view_config


def categories(cursor):
    cursor.execute("SELECT id, title, description, slug FROM bulbs_category")
    cats = cursor.fetchall()
    
    def catinfo(cat):
        keys = "id", "title", "desc", "slug"
        keys_values = zip(keys, cat)
        
        return dict(keys_values)
        
    data = map(catinfo, cats)

    return data

def subcategories(cursor, category_id=None):
    if category_id is not None:
        cursor.execute(
            "SELECT id, title, category_id, description, slug FROM bulbs_subcategory \
            WHERE category_id = %s", (category_id, )
        )
    else:
        cursor.execute(
            "SELECT id, title, category_id, description, slug FROM bulbs_subcategory"
        )
            
    children = cursor.fetchall()
    
    def foruminfo(data):
        keys = "id", "title", "category_id", "desc", "slug"
        keys_values = zip(keys, data)

        id = data[0]
        
        return dict(keys_values,
            id=id,
            threads=helpers.number_of_threads(cursor, id),
            posts=helpers.number_of_posts(cursor, id),
            last_post=helpers.last_post(cursor, id)
        )
        
    subcategories_ = map(foruminfo, children)

    return subcategories_

@view_config(route_name="home", renderer="home.mako")
def response(request):
    cursor = db.con.cursor()
    cat_data = categories(cursor)
    subcat_data = list(subcategories(cursor))

    print ("AUTH: ", request.session.get("auth"))

    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Home",
        "categories": cat_data,
        "subcategories": subcat_data
    }
