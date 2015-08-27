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
            
            .post-container {
                padding-right: 2em;
            }
            
        </style>

    </head>
    
    <body>
        <div class="container">
            <div class="row">
                <nav>
                    <div class="large-12 columns text-center">
                        <h1>Administrator Control Panel</h1>
                    </div>
                </nav>
            </div>
            
            <style>

            </style>
            
            <div class="large-12 columns">
                <ul class="button-group even-6">
                    <li><a class="button secondary" href="/admin">Home</a></li>
                    <li><a class="button secondary" href="/admin">Structure</a></li>
                    <li><a class="button secondary" href="/admin">Users</a></li>
                    <li><a class="button secondary" href="/admin">Settings</a></li>
                    <li><a class="button secondary" href="/admin">Groups</a></li>
                    <li><a class="button secondary" href="/admin">Add-ons</a></li>
                </ul>
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
        
        <footer style="bottom:0;width:100vw;">
            <div class="large-12 medium-12 text-center columns">
                <p class="subheader">Powered by <a href="https://github.com/galileo94/bulbs">Bulbs</a></p>
            </div>
        </footer>
           
    </body>
</html>
