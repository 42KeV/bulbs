<%inherit file="base.mako"/>

<div class="row">
    <div class="large-12 columns">
        <div class="left">
            <ul class="breadcrumbs">
                <li><a href="/">Home</a></li>
                <li><a href="../">cats</a></li>
                <li><a href=".">${subcat_name}</a></li>
                <li class="current"><a href="#">${title}</a></li>
            </ul>
        </div>
    </div>
</div>

% for post in posts:
<div class="post-container">
    <div class="row">
        <section class="large-2 columns post-header">
            <span class="post-date">${post.get("date")}</span>
            <div id="#post-${post.get('id')}"></div>
        </section>
        
        % if loop.index == 0:
            <section class="large-7 columns">
                <span class="post-title">${post.get("title")}</span>
            </section>
        % endif
        
        <section class="small-3 columns post-options">
        % if request.session.get("identity") is not None:
            <a href="${slugs['topic']}/replying-to/${post.get('id')}" class="button tiny">Reply</a>
            <a href="#" class="button tiny">Quote</a>
            <a href="#" class="button tiny">Edit</a>
        % endif 
        </section>  
    </div>
    
    <div class="row">
        <section class="large-2 columns post-user">
            <a class="poster-username" href="/user/${post.get('username')}">${post.get("username")}</a>
            <span class="poster-title">${post.get("user_title")}</span>
            
            <span class="poster-avatar">
                % if post.get("avatar") is not None:
                    ${post.get("avatar")}
                % endif
            </span>
        </section>
        
        <section class="large-10 columns post-body">
            <section class="post-content">
                ${post.get("content") | n}
            </section>
        </section>
    </div>
</div>
% endfor
