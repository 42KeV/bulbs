<%inherit file="base.mako"/>


<div class="container">

    <div class="row">
        % if user.get("avatar") is not None:
            <div class="large-4 columns">
                <img src="${user.get("avatar")}"/>
            </div>
        % endif
        <div class="large-8 columns">
            <h1 style="font-size:5em;font-weight:bold;color:#00A88C;">${user.get("username")}</h1>
        </div>
    </div>
    
    % for attr in user:
        % if attr == "username" or attr == "avatar":
            <!-- do nothing -->                
        % else:
            <div class="row">
                <div class="large-4 columns">
                    <h3 style="font-weight:bold;color:#00A88C;" class="right">${attr.capitalize()}:</h3>
                </div>
                <div class="large-8 columns">
                    <h3>${user.get(attr)}</h3>
                </div>
            </div>
        % endif
    % endfor
</div>


