from pyramid.config import Configurator
from pyramid.exceptions import NotFound, Forbidden
from pyramid.view import view_config
from pyramid.view import notfound_view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound
from bulbs.resources import connection


#@notfound_view_config()
def notfound(request):
    return Response("not found, dude", status="404 Not Found")

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.include('pyramid_beaker')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('register', '/register')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('contact', '/contact')
    config.add_route('about', '/about')
    config.add_route('usercp', '/usercp')
    config.add_route('manage', '/manage')
    config.add_route('post_edit', '/edit')
    
    config.add_route('admin_home', '/admin')
    config.add_route('admin_new_category', 'admin/create-new-category')
    config.add_route('admin_new_subcategory', 'admin/create-new-subcategory')
    config.add_route('admin_login', '/admin/login')
    
    config.add_route('user_view', '/user/{username}')
    config.add_route('new-topic', '/{cat_slug}/{subcat_slug}/posting-new')
    config.add_route('new-reply', '/{cat_slug}/{subcat_slug}/{topic_slug}/replying-to/{post_id}')
    
    config.add_route('category', '/{cat_slug}')
    config.add_route('subcategory', '/{cat_slug}/{subcat_slug}')
    config.add_route('topic', '/{cat_slug}/{subcat_slug}/{topic_slug}')
    #config.add_view(error_view, renderer='error.mako', context=NotFound)
    #config.add_view(unauthorized_view, renderer='unauthorized.mako', context=Unauthorized)
    
    connection.init()
    config.scan()
    app = config.make_wsgi_app()
    
    return app
