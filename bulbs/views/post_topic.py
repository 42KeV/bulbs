from pyramid.view import view_config
from bulbs.resources import connection
from bulbs.components.topic import create_topic
from pyramid.httpexceptions import HTTPFound
from pyramid.response import Response


@view_config(route_name='new-topic', renderer='new-topic.mako')
def main(request):
    ''' User gets this view when he goes to create a new topic '''
    category_slug = request.matchdict["cat_slug"]
    subcategory_slug = request.matchdict["subcat_slug"]

    if request.session.get("identity") is None:
        return Response("You are not authorized to view this page")

    if request.method == "POST":            
        post_subject = request.params.get("subject")
        post_message = request.params.get("message")
        username = request.session.get("identity").username
        
        cursor = connection.con.cursor()
        cursor.execute(
            "SELECT id FROM bulbs_subcategory WHERE slug = %s",
            (subcategory_slug, )
        )
        subcategory_id = cursor.fetchone()[0]
        
        new_thread_slug = create_topic(
            subject=post_subject,
            subcategory_id=subcategory_id,
            content=post_message,
            ip=request.client_addr,
            username=username
        )
        
        if not new_thread_slug:
            return Response("Something went wrong creating a new thread. Contact an administrator about this...")

        url = request.route_url(
            "topic",
            cat_slug=category_slug,
            subcat_slug=subcategory_slug,
            topic_slug=new_thread_slug
        )

        return HTTPFound(location=url)
    
    return {
        "project": request.registry.settings.get("site_name"),
        "title": "Writing new thread",
        "session": request.session
    }
