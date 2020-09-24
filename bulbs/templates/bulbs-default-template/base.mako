<!DOCTYPE html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/bootstrap.min.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/font-awesome.min.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/theme.css')}">
        <script src="//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
        <title>${project} - ${page_title}</title>
        <style>
        .footer {
            background-color: #F5F5F5;
            bottom: 0;
            height: 60px;
            position: absolute;
            width: 100%;
        }
        .container .text-muted {
            margin: 20px 0;
        }
        </style>
    </head>
    
    <body>
        <header>
            <nav class="navbar navbar-default">
                <div class="container-fluid">
                    <div class="navbar-header">
                        <a class="navbar-brand" href="https://github.com/red-nova/bulbs">
                            <i class="fa fa-lightbulb-o"></i>
                        </a>
                    </div>
                    
                    <div class="collapse navbar-collapse">
                        <ul class="nav navbar-nav">
                            <li><a href="/">Home</a></li>
                            % if is_logged_in:
                                <li><a href="/logout">Sign out</a></li>
                            % else:
                                <li><a href="/login">Sign in</a></li>
                            % endif
                            <li><a href="/about">About us</a><li>
                        </ul>
                        <ul class="nav navbar-nav navbar-right">
                            % if is_logged_in:
                                <li>
                                    <a href="#" data-toggle="tooltip" title="Inbox">
                                        <i class="fa fa-inbox"></i>
                                    </a>
                                </li>
                            % endif
                            <li>
                                <a href="#" data-toggle="tooltip" title="Notifications">
                                    <i class="fa fa-envelope-o"></i>
                                </a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
            <!--
                <li><a href="/">home</a></li>
                <li><a href="/about">about</a></li>
                % if is_logged_in:
                    <li><a href="/logout">log out</li></a>
                % else:
                    <li><a href="/login">login</a></li>
                    <li><a href="/register">register</a></li>
                % endif
            </ul>-->
        </header>
        
        <div class="container">
            ${self.body()}
        </div>
        
        <footer class="footer">
            <div class="container">
                <p class="text-muted">Copyright &copy; <a href="//github.com/red-nova">red-nova</a> - <i class="fa fa-lightbulb-o"></i> Bulbs is free software available under the MIT license.</p>
            </div>
        </footer>
        
    </body>
</html>
