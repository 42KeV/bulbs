from pyramid.httpexceptions import HTTPFound
from bulbs.resources import connection
from pyramid.view import view_config


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
        password1 = request.params.get("password1")
        password2 = request.params.get("password2")
        email = request.params.get("email")
        
        cursor = connection.con.cursor()
        
        if username_taken(cursor, username):
            return Response("username already exists. please choose a different one.")

        if password1 == password2:
            cursor.execute(
                "INSERT INTO bulbs_user (username, password, email, ip, date, karma, title) \
                VALUES (%s, encrypt(%s, 'close but no guitar', 'aes'), %s, %s, now(), %s, %s)",
                (username, password1, email, request.client_addr, 0, "Newbie")
            )
                            
            connection.con.commit()
            url = request.route_url("login")
            
            return HTTPFound(location=url)
            
        else:
            url = request.route_url("error")
            
            return HTTPFound(location=url)
            
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Register",
        "session": request.session
    }
