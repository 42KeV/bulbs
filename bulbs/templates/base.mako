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

        <style>
            .row-background:nth-child(even) {
                background-color: #F3EBF8;
                
            }
            
            .row-background {
                -webkit-transition: background-color 500ms ease;
                -moz-transition: background-color 500ms ease;
                -o-transition: background-color 500ms ease;
                -ms-transition: background-color 500ms ease;
                transition: background-color 500ms ease;
            }
            
            .subcat {
                -webkit-transition: background-color 500ms ease;
                -moz-transition: background-color 500ms ease;
                -o-transition: background-color 500ms ease;
                -ms-transition: background-color 500ms ease;
                transition: background-color 500ms ease;
            }
            
            .subcat:hover {
                background-color: #F9F9F9;
            }
            
            .row-background:hover {
                background-color: #DFD6E4;
            }
            
            .subcat-active {
                background-color: #DFD6E4;
            }
            
            .gray-border {
                border: 1px solid red;
            }
            
            .post-container {
                padding-right: 2em;
            }
            
        </style>

    </head>
    
    <body>
        <div class="container">
            <div class="row">
                <nav>
                    <div class="large-5 columns">
                        <h1 style="margin: 0">${project}</h1>
                        % if is_logged_in:
                            <p>Logged in as ${ident.username}</p>
                        % else:
                            <p>Welcome, are you new here? <a href="/register">Click here</a> to sign up</a></p>
                        % endif
                    </div>
                    
                    
                    <div class="large-7 columns">
                        <ul class="button-group round right">
                            <li><a href="/" class="button small secondary gray-border">Home</a></li>
                            
                            % if is_logged_in:
                                % if ident.group_id == 3:
                                    <li><a href="/admin" class="button secondary small gray-border">Admin CP</a></li>
                                % endif 
                                <li><a href="/usercp" class="button secondary small gray-border">User CP</a></li>
                                <li><a href="/inbox" class="button secondary small gray-border">Inbox</a></li>
                                <li><a href="/logout" class="button secondary small gray-border">Sign out</a></li>
                            % else:
                                <li><a href="/login" class="button secondary small gray-border">Sign in</a></li>
                            % endif
                        </ul>
                    </div>
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
        
        
        <!--<footer style="bottom:0;width:100vw;">
            <div class="large-12 medium-12 text-center columns">
                <p class="subheader">Powered by <a href="https://github.com/galileo94/bulbs">Bulbs</a></p>
            </div>
        </footer>-->
           
    </body>
</html>
