from sys import modules

from pyramid.view import view_config
from pyramid.response import Response

from bulbs.components.user import register_user


@view_config(route_name="install", renderer="install.mako")
def response(request):

    if request.method == "POST":
        dbtype = request.params.get("dbtype")
        
        dbname = request.params.get("dbname")
        dbuser = request.params.get("dbuser")
        dbpass = request.params.get("dbpass")
        dbport = request.params.get("dbport")
        
        # Forum administrator account details
        username = request.params.get("username")
        email = request.params.get("email")
        password1 = request.params.get("password1")
        password2 = request.params.get("password2")

        # Password validation, make sure the user typed in the same password twice
        if not password1 == password2:
            # check this via javascript first
            return Response("The passwords you entered did not match.")

        # If postgresql, write db info to file sql.cfg
        if dbtype == "postgresql":
            from db_setup import write_sql_config
            write_sql_config(dbname, dbuser, dbpass, dbport)
        
        from db_setup import database_setup
        database_setup(dbtype, dbname, dbuser, dbpass, dbport)
        
        register_user(3, username, password1, email, request.client_addr)  
        
        

    # Check out if the requirements have been installed
    required_mods = []
    
    with open("requirements.txt") as f:
        lines = f.read().split()
        
    for line in lines:
        mod = line.split("==")
        if mod[0] in modules:
            mod.append(True)
        else:
            mod.append(False)
            
        required_mods.append(mod)
        
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Home",
        "mods": required_mods
    }