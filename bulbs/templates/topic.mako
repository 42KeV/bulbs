<%inherit file="base.mako"/>

<%
    page = request.params.get("page")
    if page is not None:
        page = int(page)
%>

<style>
.post-container {
    background-color: #d3d3d3;
}

/*.post-container:nth-of-type(2n) > .row {
    background-color: #d3d3d3;
}*/
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
                <section class="large-6 columns post-header">
                    <span class="post-date">${post.get("date")}</span>
                    <div id="#post-${post.get('id')}"></div>
                </section>
                
                <section class="large-6 columns post-options">
                % if request.session.get("identity") is not None:
                    <a href="${slugs.get('topic')}/replying-to/${post.get('id')}" class="button tiny">Reply</a>
                    <a href="#" class="button tiny">Quote</a>
                    
                    % if request.session.get("identity").get("username") == post.get("username"):
                        <a href="#" class="button tiny">Edit</a>
                    % endif
                % endif 
                </section>  
            </div>
            
            <div class="row post-info">
                <section class="large-2 columns post-user">
                    <a class="poster-username" href="/user/${post.get('username')}">${post.get("username")}</a>
                    <span class="poster-title">${post.get("user_title")}</span>
                    
                    <span class="poster-avatar">
                        % if post.get("avatar") is not None:
                            <img src="${post.get("avatar")}"/>
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
        <div class="large-12 columns seperator">
            
        </div>
    </div>
    % endfor
</div>
