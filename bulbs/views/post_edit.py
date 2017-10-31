from pyramid.view import view_config
from pyramid.httpexceptions import HTTPFound
from bulbs.components import db
from bulbs.components.topic import thread_pages


@view_config(route_name="post_edit", renderer="post_edit.mako")
def response(request):
    post_id = request.params.get("post")
    #logged_in = request.session.get("identity")
    current_user_id = request.session["identity"].get("id")#insecure af
        
    cursor = db.con.cursor()
    cursor.execute("SELECT user_id FROM bulbs_post WHERE id = %s", (post_id, ))
    created_by_user_id = cursor.fetchone()[0]
    
    if current_user_id != created_by_user_id:
        return Response("You do not have permissions to edit that post")   
    
    if request.method == "POST":
       # if logged_in is None:
       #     return Response("You are not authorized to view this page")
            
        post_subject = request.params.get("subject")
        post_message = request.params.get("message")
        post_message = post_message.replace("\r\n", "<br>")
        
        cursor.execute("UPDATE bulbs_post SET title = %s, content = %s WHERE id = %s", (post_subject, post_message, post_id))
        cursor.execute("SELECT parent_post FROM bulbs_Post WHERE id = %s", (post_id, ))
        
        topic_id = cursor.fetchone()[0]
        
        if topic_id is None:
            topic_id = post_id
        
        db.con.commit()
        
        cursor.execute("SELECT subcategory_id, slug FROM bulbs_post WHERE id = %s", (topic_id, ))
        topic_data = cursor.fetchall()[0]
        subcat_id, topic_slug = topic_data[0], topic_data[1]

        cursor.execute("SELECT category_id, slug FROM bulbs_subcategory WHERE id = %s", (subcat_id, ))
        subcat_data = cursor.fetchall()[0]
        cat_id, subcat_slug =  subcat_data[0], subcat_data[1]
        
        cursor.execute("SELECT slug FROM bulbs_category WHERE id = %s", (cat_id, ))
        cat_data = cursor.fetchone()[0]
        cat_slug = cat_data[0]
                
        # Redirect to the post that was just edited

        url = request.route_url(
            "topic",
            cat_slug=cat_slug,
            subcat_slug=cat_slug,
            topic_slug=topic_slug,
            _query=(("page", thread_pages(topic_id)),)
        )

        return HTTPFound(location=url)

    cursor.execute("SELECT title, content FROM bulbs_post WHERE id = %s", (post_id, ))
    
    thread_data = cursor.fetchone()
    thread_title = thread_data[0]
    thread_post = thread_data[1].replace("<br>", "\r\n")
    
    return {
        'project': request.registry.settings.get("site_name"),
        'page_title': 'Post edit',
        'title': thread_title,
        'message': thread_post
    }
