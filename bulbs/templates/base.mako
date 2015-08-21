<!doctype html>
<html>
    <head>
        <title>${project} - ${title}</title>
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/foundation.min.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/custom.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/normalize.css')}">

        <%
            ident = request.session.get("identity") or False  
            
            if ident:
                is_logged_in = True
            else:
                is_logged_in = False
        %>

    </head>
    
    <body>
        <div class="container">
            <div class="row">
                <nav>
                    <div class="large-6 columns">
                        <h1 style="margin: 0">${project}</h1>
                        % if is_logged_in:
                            <p>Logged in as ${ident.username}</p>
                        % else:
                            <p>Welcome, are you new here? <a href="/register">Click here</a> to sign up</a></p>
                        % endif
                    </div>
                    
                    <ul class="button-group right">
                        <li><a href="/" class="button">Home</a></li>
                        
                        % if is_logged_in:
                            % if ident.group_id == 3:
                                <li><a href="/admin" class="button">Admin CP</a></li>
                            % endif
                            <li><a href="/inbox" class="button">Inbox</a></li>
                            <li><a href="/logout" class="button">Sign out</a></li>
                        % else:
                            <li><a href="/login" class="button">Sign in</a></li>
                        % endif
                    </ul>
                </nav>
            </div>
        </div>
        
        <section class="child-content">
            ${self.body()}
        </section>
        
        <script src="${request.static_url('bulbs:static/js/vendor/jquery.js')}"></script>
        <script src="${request.static_url('bulbs:static/js/custom.js')}"></script>
        <script src="${request.static_url('bulbs:static/js/foundation.min.js')}"></script>
        
        <script>
            $(document).foundation();
        </script>     
        
        <hr class="seperator">
        
        <footer style="bottom:0;width:100vw;">
            <div class="large-12 medium-12 text-center columns">
                <p class="subheader">Powered by <a href="https://github.com/galileo94/bulbs">Bulbs</a></p>
            </div>
        </footer>
           
    </body>
</html>
