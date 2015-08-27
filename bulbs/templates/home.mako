<%inherit file="base.mako"/>

<%
    current_username = None
    if request.session.get("user") is not None:
        current_username = request.session.get("user").get("username")
    if current_username is None:
        is_logged_in = False
    else:
        is_logged_in = True
%>


<div class="row">
    <div class="large-12 columns">
        % if is_logged_in:
            <p>There have been $n new posts since your last visit.</p>
        % endif
    </div>
</div>

% for category in categories:
    <div class="row">
        <div class="large-12 columns text-center">
            <span class="cat-name">${category.get("title")}</span>
        </div>
    </div>

    <hr class="seperator">
    
    % for subcategory in subcategories:
        % if subcategory.get("category_id") == category.get("id"):
            <% lastpost = subcategory.get("last_post", None) %>
            
            
            <div class="row-background">
            <div class="subcat row">
                
                <div class="large-7 columns">
                    <span class="subcat-name">
                        <a class="subcat-title" href="${category.get('slug')}/${subcategory.get('slug')}">
                            ${subcategory.get("title")}
                        </a>
                    </span>
                    
                    <span class="subcat-desc">${subcategory.get("desc")}</span>
                </div>
                
                <div class="large-2 subcat-stats columns">
                    <span class="subcat-threads">${subcategory.get("threads")} Threads</span>
                    <span class="subcat-replies">${subcategory.get("posts")} Replies</span>
                </div>
                
                <div class="large-3 subcat-stats columns">
                    % if lastpost is not None:
                        <span class="last-post-date">${lastpost.get("date")}</span>
                        by <a href="#">${lastpost.get("username")}</a>
                    % endif
                </div>
                
            </div>
            </div>
        % endif
    % endfor        
    </div>
% endfor
