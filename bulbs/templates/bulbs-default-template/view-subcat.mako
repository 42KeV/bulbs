<%inherit file="base.mako"/><!--%>-->

<div id="quick-nav">${project} ${forum_name}</div>

% if is_logged_in:
    <a href="/post-poll/${forum_id}">Post poll</a>
    <a href="/post-thread/${forum_id}">Post thread</a>
% endif


<table class="ui-container threads">
    <thead>
        <th>title</th>
        <th>views</th>
        <th>replies</th>
        <th>last post</th>
    </thead>
    <tbody>
        % for thread in threads:
            <% last_post = thread.get("stats").get("last_post") %>
            <tr>
                <td class="thread title">
                    <a href="/thread/${thread.get('id')}">${thread.get("title")}</a>
                    <div class="thread author">by ${thread.get("author")}</div>
                </td>
                <td class="thread views">${thread.get("stats").get("views")}</td>
                <td class="thread replies">${thread.get("stats").get("replies")}</td>
                <td class="thread last">
                    % if last_post is not None:
                        <a href="/user/${last_post.get('username')}">${last_post.get("username")}</a>
                    % else:
                        nobody
                    % endif
                </td>
            </tr>
        % endfor
    </tbody>
</table>

<!--
<div id="ui-container">
    <div id="threads">
        % for thread in threads:
            <div class="thread-row">
                <div class="thread title">
                    <a href="/thread/${thread.get('id')}">${thread.get("title")}</a>
                </div>
                <div class="thread views">${thread.get("stats").get("views")}</div>
                <div class="thread replies">${thread.get("stats").get("replies")}</div>
                
                <% last_poster = thread.get("stats").get("last_post") %>
                <div class="thread last">
                    % if last_poster is not None:
                        ${last_poster.get("username")}
                    % else:
                        nobody
                    % endif
                </div>
            </div>
        % endfor
    </div>
</div>
-->
