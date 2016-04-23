<%inherit file="base.mako"/>

<br>

<div class="container">
    <div class="row">
        <ul class="left breadcrumbs">
            <li><a href="/">Home</a></li>
            <li class="current"><a href="#">${title}</a></li>
        </ul>

        % if request.session.get("identity") is not None:
            <div class="right">
                <a href="${slugs.get('subcat')}/posting-new" class="button tiny">Post topic</a>
                <a href="#" class="button tiny">Post poll</a>
            </div>
        % endif
    </div>
    
    <div class="large-12 columns">
        <div class="row">
            % if moderators is not None:
                <p>Moderators:
                    % for mod in moderators:
                        ${mod},
                    % endfor
                </p>
            % endif
        </div>

        <hr class="seperator">

        % for thread in threads:
            <% last_post = thread.get("last_post") %>
           
            <div class="row-background">
                <div class="category">
                    <div class="row row-container" data-topic="${thread.get('slug')}" >

                        <div class="medium-7 columns">
                            <div class="subcat-title">
                                <h4 style="margin: 0; padding: 0">${thread.get("title")}</h4>
                                Created by <a href="#">${thread.get("author")}</a>
                            </div>
                        </div>
                        
                        <div class="subcat-stats medium-2 columns">
                            ${thread.get("stats").get("views")} Views <br>
                            ${thread.get("stats").get("replies")} Replies
                        </div>
                        
                        <div class="subcat-last medium-3 columns">
                            % if last_post is not None:
                                Last post made by <a href="#">${last_post.get("username")}</a>
                            % endif
                        </div>
                        
                    </div>
                </div>
            </div>
        % endfor

    </div>
</div>

<script>
$(function() {
    $(".row-container").click(function() {
        var topic = $(this).attr("data-topic");
        var subcat = "${slugs.get('subcat')}";
        
        window.location.href = subcat + "/" + topic;        
    });
});
</script>
