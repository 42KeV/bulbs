<%inherit file="base.mako"/>

<%
    ident = request.session.get("identity") or False  
    
    if ident:
        is_logged_in = True
    else:
        is_logged_in = False
%>

<br>

<div class="container">
    <div class="row wide-row">
        <div class="large-6 columns">
            % if is_logged_in:
                <p>Logged in as ${ident.get("username")}</p>
            % else:
                <p>Welcome, are you new here? <a href="/register">Click here</a> to sign up</a></p>
            % endif
        </div>
        
        <div class="large-6 columns text-right">
            % if is_logged_in:
                <p>There have been $n new posts since your last visit.</p>
            % endif
        </div>
    </div>

    % for category in categories:
        <div class="row wide-row row-header-container">
            <div class="large-12 text-center columns">
                <span class="cat-name">${category.get("title")}</span>
            </div>
        </div>

        % for subcategory in subcategories:
            % if subcategory.get("category_id") == category.get("id"):
                <% last_post = subcategory.get("last_post", None) %>
                
                <div class="row wide-row row-container" data-cat="${category.get('slug')}" data-subcat="${subcategory.get('slug')}">
                    <div class="large-7 columns subcat-column">
                        <a href="#"><h4 class="subcat-title">${subcategory.get("title")}</h4></a>
                        <span class="subcat-desc">${subcategory.get("desc")}</span>
                    </div>
                    
                    <div class="large-2 columns subcat-stats subcat-column">
                        <% t = "Thread" if subcategory.get("threads") == 1 else "Threads" %>
                        <% r = "Post" if subcategory.get("posts") == 1 else "Posts" %>
                        
                        <span class="subcat-threads">${subcategory.get("threads")} ${t}</span>
                        <span class="subcat-replies">${subcategory.get("posts")} ${r}</span>
                    </div>
                    
                    <div class="large-3 columns subcat-stats lastpost-column">
                        % if last_post is not None:
                            Last post by <a href="user/${last_post.get('username')}">${last_post.get("username")}</a> on
                            <span class="last-post-date">${last_post.get("date")}</span>
                        % endif
                    </div>
                </div>
            % endif
        % endfor
    % endfor
</div>


<script>
$(function() {
    $("#nav-home").addClass("active");
    
    $(".lastpost-column").click(function() {
        var parent = $(this).parent();
        var cat = parent.attr("data-cat");
        var subcat = parent.attr("data-subcat");
        window.location.href = cat + "/" + subcat // + topic + page + post_id;
    });
    
    $(".subcat-column").click(function() {
        var parent = $(this).parent();
        var cat = parent.attr("data-cat");
        var subcat = parent.attr("data-subcat");
        window.location.href = cat + "/" + subcat;
    });
    
});
</script>
