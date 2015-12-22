<%inherit file="base.mako"/>

<br>

<div class="large-12 columns">
    <div class="left">
        <ul class="breadcrumbs">
            <li><a href="/">Home</a></li>
            <li><a href="../${slug.get('subcat')}">${subcat_name}</a></li>
            <li class="current"><a href="#">${title}</a></li>
        </ul>
    </div>
</div>

<nav>
    <ul class="pagination">
        <li>
            <a href="#" aria-label="Previous">
            <span aria-hidden="true">&laquo;</span>
            </a>
        </li>
        % for n in range(pages):
            <li><a href="?page=${n+1}">${n+1}</a></li>
        % endfor
        <li>
            <a href="#" aria-label="Next">
            <span aria-hidden="true">&raquo;</span>
            </a>
        </li>
    </ul>
</nav>

% for post in posts:
    % if loop.index == 0:
        <div class="post-container">
            <section class="large-12 columns ">
                <h2 class="post-title">${post.get("title")}</h2>
            </section>
        </div>
    % endif

<div class="post-container">
    <div style="max-width: 100%;" class="row">
        <section class="large-2 columns post-header">
            <span class="post-date">${post.get("date")}</span>
            <div id="#post-${post.get('id')}"></div>
        </section>
        

        
        <section class="small-3 columns post-options">
        % if request.session.get("identity") is not None:
            <a href="${slug.get('topic')}/replying-to/${post.get('id')}" class="button tiny secondary gray-border">Reply</a>
            <a href="#" class="button tiny secondary gray-border">Quote</a>
            
            % if request.session.get("identity").get("username") == post.get("username"):
                <a href="#" class="button tiny secondary gray-border">Edit</a>
            % endif
        % endif 
        </section>  
    </div>
    
    <div style="max-width: 100%;" class="row">
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

<hr class="seperator">

% endfor
