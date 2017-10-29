from pyramid.httpexceptions import HTTPFound
from pyramid.view import view_config
from bulbs.components import db
from bulbs.components.reply import reply_to_topic

@view_config(route_name='new-reply', renderer='new-reply.mako')
def response(request):
    ''' This view is called when someone is replying to a post '''
    if request.session.get("identity") is None:
        url = request.route_url(
            "unauthorized",
            reason="You need to be logged in to view this page"
        )
        
        return HTTPFound(location=url)
        
    slugs = {
        "cat": request.matchdict.get("cat_slug"),
        "subcat": request.matchdict.get("subcat_slug"),
        "topic": request.matchdict.get("topic_slug")
    }
    
    post_id = request.matchdict.get("post_id")

    cursor = db.con.cursor()
    cursor.execute("SELECT parent_post, user_id FROM bulbs_post WHERE id = %s", (post_id, ))
    original_post = cursor.fetchone()
    
    topic_id = original_post[0] # root idea, is None if user is replying to the root post
    
    if topic_id is None:
        topic_id = post_id
        
    original_user_id = original_post[1]
    
    if request.method == "POST":
        post_subject = request.params.get("subject")
        post_message = request.params.get("message")
        
        username = request.session.get("identity").get("username")

        post_written = reply_to_topic(
            post_subject,
            post_message,
            topic_id,
            request.client_addr,
            username
        )
        
        if not post_written:
            return Response("An error has occurred writing the post")

        url = request.route_url(
            "topic",
            cat_slug=slugs["cat"],
            subcat_slug=slugs["subcat"],
            topic_slug=slugs["topic"]
        )
        
        return HTTPFound(location=url)
    
    cursor.execute("SELECT title FROM bulbs_Post WHERE id = %s", (topic_id, ))
    thread_title = cursor.fetchone()[0]
    
    cursor.execute("SELECT username FROM bulbs_User WHERE id = %s", (original_user_id, ))
    rec_user = cursor.fetchone()[0]
    
    return {
        'project': request.registry.settings.get("site_name"),
        'title': 'Replying to {0}'.format(thread_title),
        'thread_title': thread_title,
        'replying_to': rec_user,
        'session': request.session
    }
