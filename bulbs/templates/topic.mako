<%inherit file="base.mako"/>%>

<%
    page = request.params.get("page")
    if page is not None:
        page = int(page)
%>

<style>
.post-container > .row {
    border-left: 1px solid #f5f5f5;
    border-right: 1px solid #f5f5f5;
}
.post-content {
    word-wrap: break-word;
}
</style>


<br>

<div class="container">
    <div class="row">
        <ul class="left breadcrumbs">
            <li><a href="/">Home</a></li>
            <li><a href="/${slugs.get('cat')}/${slugs.get('subcat')}">${subcat_name}</a></li>
            <li class="current"><a href="#">${title}</a></li>
        </ul>
    </div>

    <div class="row">
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
    </div>
    
    % for post in posts:
            % if loop.index == 0 and (page == 1 or page is None):
                <div class="row row-header-container" style="border-radius: 5px 5px 0 0">
                    <section class="large-12 columns">
                        <h2 class="post-title">${title}</h2>
                    </section>
                </div>
            % endif

        <div class="post-container">
            <div class="row post-info">                
                <section style="background-color: #f5f5f5" class="large-12 columns post-options">
                % if request.session.get("identity") is not None:
                    <a href="${slugs.get('topic')}/replying-to/${post.get('id')}" class="button tiny">Reply</a>
                    <a href="#" class="button tiny">Quote</a>
                    
                    % if request.session.get("identity").get("username") == post.get("username"):
                        <a href="/edit?post=${post.get('id')}" class="button tiny">Edit</a>
                    % endif
                % endif 
                </section>  
            </div>
            
            <div class="row post-info">
                <section class="large-2 columns post-user">
                    <span class="post-date">${post.get("date")}</span>
                    <div id="#post-${post.get('id')}"></div>
                
                    <%
                        # generate url safe usernames
                        from urllib.parse import quote
                    %>
                
                    <a class="poster-username" href="/user/${quote(post.get('username'))}">${post.get("username")}</a>
                    <span class="poster-title">${post.get("title")}</span>
                    
                    <span class="poster-avatar">
                        % if post.get("avatar") is not None:
                            <img src="${post.get('avatar')}"/>
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

    
    <div class="row">
        <hr>
    </div>
    % endfor
</div>

