from pyramid.view import view_config
from bulbs.components import db
from pyramid.response import Response


@view_config(route_name="usercp", renderer="user-cp.mako")
def response(request):
    ident = request.session.get("identity")
    
    if ident is None:
        return Response("You are not authorized to view this page. Please login to continue")
    
    if request.method == "POST":
        username = ident.get("username")
        
        print ("USE$RNAME ISSSSSSSSSSS", username)
        
        real_name = request.params.get("name")
        city = request.params.get("city")
        state = request.params.get("state")
        email = request.params.get("email")
        bio = request.params.get("bio")
        avatar = request.params.get("avatar")
        current_password = request.params.get("current_password")

        cursor = db.con.cursor()

        if current_password: # user wants to change password
            new_password1 = request.params.get("new_password1")
            new_password2 = request.params.get("new_password1")
            
            if not new_password1 == new_password2: # user typed the same password correctly
                return Response("Invalid current password!")
                
        if real_name:
            cursor.execute("UPDATE bulbs_user SET real_name = %s WHERE username = %s", (real_name, username))
        if city:
            cursor.execute("UPDATE bulbs_user SET city = %s WHERE username = %s", (city, username))
        if state:
            cursor.execute("UPDATE bulbs_user SET state = %s WHERE username = %s", (state, username))
        if email:
            cursor.execute("UPDATE bulbs_user SET email = %s WHERE username = %s", (email, username))
        if bio:
            print ("updating bio .................")
            cursor.execute("UPDATE bulbs_user SET biography = %s WHERE username = %s", (bio, username))
        if avatar:
            cursor.execute("UPDATE bulbs_user SET avatar = %s WHERE username = %s", (avatar, username))
            
        db.con.commit()
            
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "User CP"
    }
