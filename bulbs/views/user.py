from pyramid.view import view_config
from bulbs.components import db


@view_config(route_name="user_view", renderer="user.mako")
def response(request):
    username = request.matchdict.get("username")
    cursor = db.con.cursor()
    cursor.execute(
        "SELECT username, to_char(date, 'Mon FMDD, YYYY HH:MM AM'), karma, title, \
        name, city, state, country, biography, avatar \
        FROM bulbs_User WHERE username = %s", (username, ))
    data = cursor.fetchone()
    userdata = {
        "username": data[0],
        "DOB": data[1],
        "karma": data[2],
        "title": data[3],
        "name": data[4],
        "city": data[5],
        "state": data[6],
        "country": data[7],
        "biography": data[8],
        "avatar": data[9]
    }
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "{0}'s profile".format(userdata["username"]),
        "user": userdata
    }
