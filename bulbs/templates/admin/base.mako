<!doctype html>
<html>
    <head>
        <title>${project} - ${title}</title>
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/foundation.min.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/custom.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/normalize.css')}">

        <%
            is_logged_in = True if request.session.get("user") is not None else False
        %>

    </head>
    
    <body>
        <div class="container">
            <div class="row">
                <nav>
                    <div class="large-6 columns">
                        <h1 style="margin: 0">Free Games Forum Admin CP</h1>
                         % if is_logged_in:
                            <p>Logged in as ${request.session.get("user").get("username")}</p>
                        % endif
                    </div>
                    
                    <ul class="button-group right">
                        <li><a href="/" class="button">Home</a></li>
                        
                        % if is_logged_in:
                            <li><a href="/inbox" class="button">Inbox</a></li>
                            <li><a href="/logout" class="button">Sign out</a></li>
                        % else:
                            <li><a href="/login" class="button">Sign in</a></li>
                        % endif
                    </ul>
                </nav>
            </div>
        </div>
        
        <div class="container">
            ${self.body()}
        </div>
        
        <script src="${request.static_url('bulbs:static/js/vendor/jquery.js')}"></script>
        <script src="${request.static_url('bulbs:static/js/foundation.min.js')}"></script>
        
        <script>
            $(document).foundation();
        </script>     
        
        <footer class="row">
            <div class="small-12 columns">
                <p class="subheader text-center">Copyright &copy; ${project} 2015 | Powered by <a href="https://github.com/galileo94/bulbs">Bulbs</a></p>
            </div>
        </footer>
           
    </body>
</html>
