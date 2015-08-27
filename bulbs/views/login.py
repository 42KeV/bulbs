from pyramid.httpexceptions import HTTPFound
from bulbs.resources import connection
from pyramid.view import view_config

from bulbs.auth.controller import authorize


@view_config(route_name="login", renderer="login.mako")
def main(request):
    if request.method == "POST":
        username = request.params.get("username")
        password = request.params.get("password")
        auth = authorize(username, password)
        
        if auth.get("success"):
            request.session["identity"] = auth.get("session")
            url = request.route_url("home")
            
            return HTTPFound(location=url)
    
    session = request.session
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Log In",
        "session": session
    }
