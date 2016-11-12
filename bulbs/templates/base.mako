<!doctype html>
<html>
    <head>
        <title>${project} - ${title}</title>
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/foundation.min.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/output.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/normalize.css')}">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">

        <link href='https://fonts.googleapis.com/css?family=Walter+Turncoat|Parisienne' rel='stylesheet' type='text/css'>

        <%
            ident = request.session.get("identity") or False  
            
            if ident:
                is_logged_in = True
            else:
                is_logged_in = False
        %>
        
<style>
/*.foundation-row {
    max-width: 63.5rem;
}
.row {
    max-width: 90rem;
}*/
</style>
        
    </head>
    
    <body>
        <div id="site-info" oldstyle="background-color: #9BCEFF">
            <div class="row">
                <h1 style="font-family: 'Walter Turncoat', cursive; font-weight: bold; color: #fff;">FREE GAMES FORUM</h1>
            </div>
        </div>
        <nav class="top-bar" data-topbar role="navigation">

            <section class="top-bar-section">
                <!-- Right Nav Section -->
                <ul class="left">
                    <li class="top-nav-button" id="nav-home"><a href="/"><i class="fa fa-home"></i> Home</a></li>
                </ul>
                
                % if is_logged_in:
                    <ul class="left">
                        <li class="top-nav-button" id="nav-user-cp">
                            <a href="/control-panel">
                                <i class="fa fa-cog" aria-hidden="true"></i> User CP</a>
                        </li>
                        % if ident.get("group_id") == 3:
                            <li id="nav-admin-cp">
                                <a href="/admin">
                                    <i class="fa fa-cogs" aria-hidden="true"></i> Admin CP</a>
                            </li>
                        % endif
                    </ul>
                % endif
                
                <ul class="right">
                    % if is_logged_in:
                            <li class="top-nav-button" id="nav-inbox"><a href="/inbox">Inbox</a></li>
                            <li class="top-nav-button" id="nav-sign-out"><a href="/logout">Sign out</a></li>
                        % else:
                            <li class="top-nav-button" id-nav-sign-up"><a href="/register">Register</a></li>
                            <li class="top-nav-button" id="nav-sign-in"><a href="/login">Sign in</a></li>
                    % endif
                    <!--
                    <li class="has-dropdown">
                        <a href="#">Right Button Dropdown</a>
                        
                        <ul class="dropdown">
                            <li><a href="#">First link in dropdown</a></li>
                            <li class="active"><a href="#">Active link in dropdown</a></li>
                        </ul>
                    </li>-->
                </ul>
                
            </section>
        </nav>

        <script src="${request.static_url('bulbs:static/js/vendor/jquery.js')}"></script>

        <section class="child-content">
            ${self.body()}
        </section>
        
        <script src="${request.static_url('bulbs:static/js/custom.js')}"></script>
        <script src="${request.static_url('bulbs:static/js/foundation.min.js')}"></script>
        
        <script>
            $(document).foundation();
        </script>     
        
        <!--<footer style="bottom:0;width:100vw;">
            <div class="large-12 medium-12 text-center columns">
                <p class="subheader">Powered by <a href="https://github.com/galileo94/bulbs">Bulbs</a></p>
            </div>
        </footer>-->
           
    </body>
</html>
