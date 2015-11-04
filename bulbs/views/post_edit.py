from pyramid.view import view_config


@view_config(route_name="post_edit", renderer="post_edit.mako")
def response(request):
    post_id = request.params.get("post")
    login_state = request.session.get("login_state")
    
    try:
        current_user_id = request.session.get("user")["id"]
    except Exception as e:
        return Response("Invalid session, please login")
        
    cur = con.cursor()
    cur.execute("SELECT user_id FROM bulbs_Post WHERE id = %s", (post_id, ))
    created_by_user_id = cur.fetchone()[0]
    
    if current_user_id != created_by_user_id:
        return Response("You do not have permissions to edit that post")   
    
    if request.method == "POST":
        if login_state is None:
            return Response("You are not authorized to view this page")
            
        post_subject = request.params.get("subject")
        post_message = request.params.get("message")
        
        post_message = post_message.replace("\r\n", "<br>")
        
        cur.execute("UPDATE bulbs_Post SET title = %s, content = %s WHERE id = %s", (post_subject, post_message, post_id))
        cur.execute("SELECT parent_post FROM bulbs_Post WHERE id = %s", (post_id, ))
        
        thread_id = cur.fetchone()[0]
        
        if thread_id is None:
            thread_id = post_id
        
        con.commit()
        
        url = request.route_url("thread_view",
            _query = {"id": thread_id}
        )
        return HTTPFound(location = url)

    cur.execute("SELECT title, content FROM bulbs_Post WHERE id = %s", (post_id, ))
    
    thread_data = cur.fetchone()
    thread_title = thread_data[0]
    thread_post = thread_data[1].replace("<br>", "\r\n").decode("utf-8")
    
    return {
        'project': request.registry.settings.get("site_name"),
        'page_title': 'Post edit',
        'title': thread_title,
        'message': thread_post,
        'is_logged_in': login_state
    }
