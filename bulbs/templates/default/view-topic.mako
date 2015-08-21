<%inherit file="base.mako"/><!--%>-->

<a href="/">${project}</a>

<a href="/forum/${forum_id}">${forum_name}</a>${thread_name}

% for page in range(1, pages + 1):
    <li><a href="?page=${page}">${page}</a></li>
% endfor

    <table class="post-table-container">
        <tbody>
            % for post in posts:
            <tr class="post-container">
                <td class="author-container">
                    <div class="username">${post.get("username")}</div>
                    <div class="user-title">${post.get("user_title")}</div>
                    <div class="avatar">
                        % if post.get("avatar") is not None:
                            <img src="${post.get('avatar')}"/>
                        % endif
                    </div>
                    <div class="post-count">${post.get("post_count")}</div>
                    <div class="post-date">${post.get("date")}</div>
                </td>
                <td class="message-container">
                    <div class="post-options">
                        <a href="/reply/${post.get('id')}">Reply</a>
                        <a href="#">Quote</a>
                    </div>
                    <div class="post-title">${post.get("title")}</div>
                    <div class="post-content">${post.get("content") | n}</div>
                </td>
            </tr>
            % endfor
        </tbody>
    </table>

<!--
    <div class="post-container">
        <div class="author-container">
            <div class="username">${post.get("username")}</div>
            <div class="user-title">${post.get("user_title")}</div>
            <div class="avatar">
                % if post.get("avatar") is not None:
                    <img src="${post.get('avatar')}"/>
                % endif
            </div>
            <div class="post-count">${post.get("post_count")}</div>
            <div class="post-date">${post.get("date")}</div>
        </div>
        <div class="message-container">
            <div class="post-title">${post.get("title")}</div>
            <div class="post-content">${post.get("content") | n}</div>
        </div>
    </div>
-->
