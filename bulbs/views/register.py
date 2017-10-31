from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response
from pyramid.view import view_config

from bulbs.components import db
from bulbs.components.auth import generate_password, whois
from bulbs.components.user import register_user, username_taken

# DEFINE database placeholder marker

# sqlite = ?
# psycopg2 = %s
    
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
            request.session["identity"] = whois(username)
            url = request.route_url("home")
            return HTTPFound(location=url)
        if password != password_again:
            return Response("Passwords do not match.")
        else:
            url = request.route_url("error")
            return HTTPFound(location=url)
            
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Register"
    }
