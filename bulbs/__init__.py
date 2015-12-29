from pyramid.config import Configurator
from pyramid.exceptions import NotFound, Forbidden
from pyramid.view import view_config
from pyramid.view import notfound_view_config
from pyramid.response import Response
from pyramid.httpexceptions import HTTPFound

from pyramid.authentication import AuthTktAuthenticationPolicy
from pyramid.authorization import ACLAuthorizationPolicy

from bulbs.components import db


@notfound_view_config()
def notfound(request):
    return Response("not found, dude", status="404 Not Found")

def unauthorized(request):
    return Response("You are not authorized to view this page.")

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    
    authn_policy = AuthTktAuthenticationPolicy("global hellhole of a world", hashalg="sha512")
    authz_policy = ACLAuthorizationPolicy()
    
    config = Configurator(settings=settings)
    
    config.set_authentication_policy(authn_policy)
    config.set_authorization_policy(authz_policy)
    
    config.include('pyramid_mako')
    config.include('pyramid_beaker')
    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('register', '/register')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')
    config.add_route('contact', '/contact')
    config.add_route('about', '/about')
    config.add_route('usercp', '/control-panel')
    config.add_route('manage', '/manage')
    config.add_route('post_edit', '/edit')
    
    # admin panel routes
    config.add_route('admin_home', '/admin')
    config.add_route('admin_login', '/admin/login')
    
    # - admin layout management routes
    config.add_route('admin_struct_home', '/admin/structure')
    config.add_route('admin_struct_new_category', 'admin/structure/create-new-category')
    config.add_route('admin_struct_new_subcategory', 'admin/structure/create-new-subcategory')
    
    config.add_route('user_view', '/user/{username}')
    config.add_route('new-topic', '/{cat_slug}/{subcat_slug}/posting-new')
    config.add_route('new-reply', '/{cat_slug}/{subcat_slug}/{topic_slug}/replying-to/{post_id}')
    
    config.add_route('category', '/{cat_slug}')
    config.add_route('subcategory', '/{cat_slug}/{subcat_slug}')
    config.add_route('topic', '/{cat_slug}/{subcat_slug}/{topic_slug}')
    #config.add_view(error_view, renderer='error.mako', context=NotFound)

    #config.add_view('unauthorized', renderer='errors/unauthorized.mako')
    
    db.init()
    config.scan()
    app = config.make_wsgi_app()
    
    return app
