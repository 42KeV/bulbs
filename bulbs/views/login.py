from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from bulbs.components.auth import checkpw, whois


@view_config(route_name="login", renderer="login.mako")
def response(request):
    if request.method == "POST":
        username = request.params.get("username")
        password = request.params.get("password")
        matched = checkpw(username, password)
        if matched:
            request.session["identity"] = whois(username)
            url = request.route_url("home")
            return HTTPFound(location=url)
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Log In",
    }
