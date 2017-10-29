from pyramid.view import view_config
from bulbs.components import db
from bulbs.components.helpers import generate_slug


def destined_subcat_id():
    cursor = db.con.cursor()
    #sqlite3cursor.execute("SELECT rowid FROM bulbs_subcategory")
    cursor.execute("SELECT last_value FROM bulbs_subcategory_id_seq")
    try:
        future_id = cursor.fetchone()[0] + 1
    except TypeError:
        future_id = 1
    return future_id

def catinfo(data):
    keys = "id", "title"
    keys_values = zip(keys, data)
    
    return dict(keys_values)

@view_config(route_name="admin_struct_new_subcategory", renderer="admin/structure/new-subcategory.mako")
def main(request):
    cursor = db.con.cursor()
    cursor.execute("SELECT id, title FROM bulbs_category")
    cat_data = cursor.fetchall()
    categories = map(catinfo, cat_data)
    
    if request.method == "POST":
        subcat_name = request.params.get("subcatname")
        cat_id = request.params.get("catid")
        subcat_desc = request.params.get("subcatdesc")
        subcat_rank = request.params.get("subcatrank")
        subcat_slug = request.params.get("subcatslug")
        
        # temporary workaround for mysterious subcatslug empty string
        if len(subcat_slug) == 0:
            subcat_slug = None
        
        if subcat_slug is None:
            subcat_slug = generate_slug(
                subcat_name, 
                destined_subcat_id(),
                "bulbs_subcategory"
            )

        # authorize user, make sure he's admin
        #
        #
        # > auth here
        #
        #
        
        cursor = db.con.cursor()
        cursor.execute(
            "INSERT INTO bulbs_subcategory (title, description, category_id, date, ip, slug) \
             VALUES (%s, %s, %s, now(), %s, %s)", (
                subcat_name, 
                subcat_desc,
                cat_id,
                request.client_addr, 
                subcat_slug
            )
        )
        
        db.con.commit()
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "ACP - New subcategory",
        "categories": categories
    }
