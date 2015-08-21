from bulbs.resources import connection
from bulbs.resources.helpers import generate_slug
from pyramid.view import view_config


def future_subcategory_id(cursor):
    cursor.execute("SELECT last_value FROM bulbs_subcategory_id_seq")
    future_id = cursor.fetchone()[0] + 1

    return future_id

def catinfo(data):
    keys = "id", "title"
    keys_values = zip(keys, data)
    
    return dict(keys_values)

@view_config(route_name="admin_new_subcategory", renderer="admin/new-subcategory.mako")
def main(request):
    cursor = connection.con.cursor()
    cursor.execute("SELECT id, title FROM bulbs_category")
    cat_data = cursor.fetchall()
    categories = map(catinfo, cat_data)
    
    if request.method == "POST":
        subcategory_name = request.params.get("subcatname")
        category_id = request.params.get("catid")
        subcategory_desc = request.params.get("subcatdesc")
        subcategory_rank = request.params.get("subcatrank")
        subcategory_slug = request.params.get("subcatslug")
        
        if subcategory_slug is None:
            subcategory_slug = generate_slug(
                cursor,
                subcategory_name, 
                future_subcategory_id(cursor),
                "bulbs_subcategory"
            )
        
        # authorize user, make sure he's admin
        #
        #
        # > auth here
        #
        #
        
        cursor = connection.con.cursor()
        cursor.execute(
            "INSERT INTO bulbs_subcategory (title, description, category_id, date, ip, slug) \
             VALUES (%s, %s, %s, now(), %s, %s)", (
                subcategory_name, 
                subcategory_desc,
                category_id,
                request.client_addr, 
                subcategory_slug
            )
        )
        
        connection.con.commit()
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "ACP - New subcategory",
        "categories": categories
    }
