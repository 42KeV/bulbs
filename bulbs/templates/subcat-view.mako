<%inherit file="base.mako"/>


<br>

<div class="row">
    <div class="large-6 columns">
        <div class="left">
            <ul class="breadcrumbs">
	            <li><a href="/">Home</a></li>
	            <li class="current"><a href="#">${title}</a></li>
            </ul>
        </div>
    </div>

    <div class="">        
        <div class="small-6 columns">
            % if request.session.get("identity") is not None:
                <div class="right">
                    <a href="${slugs.get('subcat')}/posting-new" class="button small">Post topic</a>
                    <a href="#" class="button small">Post poll</a>
                </div>
            % endif
        </div>
    </div>
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
        <% lastpost = thread.get("last_post") %>
       
        <div class="row-background">
            <div class="category">
                <div class="topic subcat row">
                
                    <div class="medium-7 columns">
                        <div class="subcat-title">
                            <a href="${slugs['subcat']}/${thread.get('slug')}">${thread.get("title")}</a> <br>
                            Created by <a href="#">${thread.get("author")}</a>
                        </div>
                    </div>
                    
                    <div class="subcat-stats medium-2 columns">
                        ${thread.get("stats").get("views")} Views <br>
                        ${thread.get("stats").get("replies")} Replies
                    </div>
                    
                    <div class="subcat-last medium-3 columns">
                        % if lastpost is not None:
                            Last post made by <a href="#">${lastpost.get("username")}</a>
                        % endif
                    </div>
                    
                </div>
            </div>
        </div>
    % endfor

</div>
