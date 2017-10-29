from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from bulbs.components import db
from bulbs.components.auth import generate_password
from bulbs.components.user import register_user, username_taken

# DEFINE database placeholder marker

# sqlite = ?
# psycopg2 = %s




#def username_taken(username):
#    """Check if the username already exists in the database and return a boolean."""
#    cursor = db.con.cursor()
#    cursor.execute(
#        "SELECT id FROM bulbs_user WHERE lower(username) = %s", 
#         (username.lower(), ))
#    try:
#        data = cursor.fetchone()[0]
#    except TypeError:
#        return False    # Username doesn't exist.
        
#    return True
    
#def register_user(username, password, email, ip):
#    """Insert a user into the database."""
#    cursor = db.con.cursor()
#    hashed_password = generate_password(password)
#    cursor.execute(
#        "INSERT INTO bulbs_user (username, password, email, ip, date, karma, title, group_id) \
#         VALUES (%s, %s, %s, %s, now(), %s, %s, %s)",
#         (username, hashed_password, email, ip, 0, "Newbie", 1))
#    db.con.commit()
    
#    return True
    
@view_config(route_name="register", renderer="register.mako")
def response(request):
    if request.method == "POST":
        username = request.params.get("username")
        password = request.params.get("password1")
        password_again = request.params.get("password2")
        email = request.params.get("email")

        if username_taken(username):
            return Response("That username already exists. Please choose a different one.")
        if password == password_again:
            register_user(1, username, password, email, request.client_addr)
            url = request.route_url("login")
            return HTTPFound(location=url)
        else:
            url = request.route_url("error")
            return HTTPFound(location=url)
            
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Register"
    }
