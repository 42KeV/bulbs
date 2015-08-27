from bulbs.resources import connection
from bulbs.resources.helpers import generate_slug
from pyramid.view import view_config


def future_category_id(cursor):
    cursor.execute("SELECT last_value FROM bulbs_category_id_seq")
    future_id = cursor.fetchone()[0] + 1

    return future_id

@view_config(route_name="admin_struct_new_category", renderer="admin/structure/new-category.mako")
def main(request):
    
    if request.method == "POST":
        category_name = request.params.get("catname")
        category_desc = request.params.get("catdesc")
        category_rank = request.params.get("catrank")
        category_slug = request.params.get("catslug")
        
        # authorize user, make sure he's admin
        #
        #
        # > auth here
        #
        #
        
        cursor = connection.con.cursor()
        
        if category_slug is None:
            category_slug = generate_slug(
                cursor,
                category_name, 
                future_category_id(cursor),
                "bulbs_category"
            )
            
        cursor.execute(
            "INSERT INTO bulbs_category (title, description, date, ip, slug) \
             VALUES (%s, %s, now(), %s, %s)", (
                category_name, 
                category_desc, 
                request.client_addr, 
                category_slug
            )
        )
        
        connection.con.commit()
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "ACP - New category"
    }
