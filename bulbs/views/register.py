from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from bulbs.resources import connection
from bulbs.auth.controller import generate_password

import bcrypt


def username_taken(cursor, username):
    cursor.execute(
        "SELECT id FROM bulbs_user WHERE username = %s", (username, )
    )

    taken = cursor.fetchone()
    
    if taken:
        return True
    
    return False

@view_config(route_name="register", renderer="register.mako")
def main(request):
    ''' This view is called when someone is signing up '''
    
    if request.method == "POST":
        username = request.params.get("username")
        password = request.params.get("password1")
        password_again = request.params.get("password2")
        email = request.params.get("email")
        
        cursor = connection.con.cursor()
        
        if username_taken(cursor, username):
            return Response("username already exists. please choose a different one.")

        if password == password_again:
            hashed_password = generate_password(password)
            cursor.execute(
                "INSERT INTO bulbs_user (username, password, email, ip, date, karma, title) \
                VALUES (%s, %s, %s, %s, now(), %s, %s)",
                (
                    username, 
                    hashed_password, 
                    email, 
                    request.client_addr, 
                    0,
                    "Newbie"
                )
            )
                            
            connection.con.commit()
            url = request.route_url("login")
            return HTTPFound(location=url)
            
        else:
            url = request.route_url("error")
            return HTTPFound(location=url)
            
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Register"
    }
