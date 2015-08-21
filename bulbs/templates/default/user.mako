<%inherit file="base.mako"/>

<div class="user-view">
    % if user["name"] is not None:
        <h1>Hi! I'm ${user["name"]}!</h1>
    % else:
        <h1>Hi! I'm ${user["username"]}</h1>
    % endif
    
    <div>
        <img class="user-avatar" src="${user['avatar']}"/> <h2 style="display: inline">${user["username"]}</h2>
    </div>
    
    <div class="user-info">
        <ul style="font-size: 16px">
            % for element in user:
                % if user[element] is not None:
                    % if element != "avatar":
                        <li>${element}: ${user[element]}</li>
                    % endif
                % endif
            % endfor
        </ul>
    </div>
    
    
</div>
