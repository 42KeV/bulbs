from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from bulbs.components import db
from bulbs.components.security import generate_password


def username_taken(username):
    cursor = db.con.cursor()
    cursor.execute(
        "SELECT id FROM bulbs_user WHERE lower(username) = %s", (username.lower(), ))
    data = cursor.fetchone()
    if data is None:
        return False
    return True

@view_config(route_name="register", renderer="register.mako")
def response(request):
    ''' This view is called when someone is signing up '''
    
    if request.method == "POST":
        username = request.params.get("username")
        password = request.params.get("password1")
        password_again = request.params.get("password2")
        email = request.params.get("email")

        if username_taken(username):
            return Response("username already exists. please choose a different one.")

        if password == password_again:
            cursor = db.con.cursor()
            hashed_password = generate_password(password)
            cursor.execute(
                "INSERT INTO bulbs_user (username, password, email, ip, date, karma, title, group_id) \
                VALUES (%s, %s, %s, %s, now(), %s, %s, %s)",
                (
                    username, 
                    hashed_password, 
                    email, 
                    request.client_addr, 
                    0,
                    "Newbie",
                    1
                )
            )
                            
            db.con.commit()
            url = request.route_url("login")
            return HTTPFound(location=url)
            
        else:
            url = request.route_url("error")
            return HTTPFound(location=url)
            
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Register"
    }
