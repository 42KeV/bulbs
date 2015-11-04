from pyramid.view import view_config
from pyramid.response import Response


@view_config(route_name="usercp", renderer="user-cp.mako")
def response(request):
    ident = request.session.get("identity")
    
    print (ident)
    print (ident.is_authorized())
    
    
    if ident is None or not ident.is_authorized():
        return Response("You are not authorized to view this page. Please login to continue")
    
    #if ident is not None:
    #    if not ident.is_authorized():
    #        return Response("You are not authorized to view this page. Please login to continue")
    
    if request.method == "POST":            
        username = ident.username
        real_name = request.params.get("name")
        city = request.params.get("city")
        state = request.params.get("state")
        email = request.params.get("email")
        bio = request.params.get("bio")
        avatar = request.params.get("avatar")
        current_password = request.params.get("current_password")

        cur = con.cursor()

        if current_password: # user wants to change password
            new_password1 = request.params.get("new_password1")
            new_password2 = request.params.get("new_password1")
            
            if new_password1 == new_password2: # user typed the same password correctly
                pass
                
        if real_name:
            cur.execute("UPDATE bulbs_User SET real_name = %s WHERE username = %s", (real_name, username))
        if city:
            cur.execute("UPDATE bulbs_User SET city = %s WHERE username = %s", (city, username))
        if state:
            cur.execute("UPDATE bulbs_User SET state = %s WHERE username = %s", (state, username))
        if email:
            cur.execute("UPDATE bulbs_User SET email = %s WHERE username = %s", (email, username))
        if bio:
            cur.execute("UPDATE bulbs_User SET biography = %s WHERE username = %s", (bio, username))
        if avatar:
            cur.execute("UPDATE bulbs_User SET avatar = %s WHERE username = %s", (avatar, username))
            
        con.commit()
            
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "User CP"
    }
