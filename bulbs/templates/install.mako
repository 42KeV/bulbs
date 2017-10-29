<!doctype html>
<html lang="en">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/foundation.min.css')}">
        <link rel="stylesheet" href="${request.static_url('bulbs:static/css/normalize.css')}">
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.5.0/css/font-awesome.min.css">
        <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
        
        <title>Bulbs - Installation</title>
        
        <style>
        body {
            padding: 0;
            font-family: "Open Sans", sans-serif;
            background-color: #fff; 
        }
        h1 {
            font-family: "Roboto", "Open Sans", sans-serif;
            font-size: 48px;
            font-weight: 900;
            line-height: 15px;

        }
        select {
            padding: .3rem; /* fixes select text cutting ifdk*/
        }
        </style>
    </head>
    
    <body>
        <div class="row">
            <h1 class="text-center">Bulbs</h1>
        </div>

        <div class="medium-6 medium-centered columns">
            <fieldset id="requirementfieldset" class="fieldset">
                <legend>Requirements</legend>
                <ul class="medium-block-grid-2">
                    <li class="text-center">
                        % for module in mods:
                            % if module[2]:
                                <strong style="color: #1d9d74">${module[0]} <i class="fa fa-check" aria-hidden="true"></i> </strong> <br>
                            % endif
                        % endfor
                    </li>
                    <li class="text-center">
                        % for module in mods:
                            % if not module[2]:
                                <strong style="color: #CD2626">${module[0]} <i class="fa fa-times" aria-hidden="true"></i> </strong> <br>
                            % endif
                        % endfor
                    </li>
                </ul>
            </fieldset>
        </div>
        
        
        <form method="POST">            
            <div class="medium-6 medium-centered columns">
                <fieldset id="dbfieldset" class="fieldset">
                    <legend>Database</legend>                   
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <select id="dbtype" name="dbtype">
                                <option value="postgresql">PostgreSQL</option>
                                <option value="sqlite3">Sqlite3</option>
                                <option value="mysql">MySQL</option>
                            </select>
                        </div>
                    </div>

                    <br>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Database name
                                <input type="text" name="dbname">
                            </label>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Database user
                                <input type="text" name="dbuser">
                            </label>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Database user password
                                <input type="text" name="dbpass">
                            </label>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Database port
                                <input type="text" name="dbport">
                            </label>
                        </div>
                    </div>
                </fieldset>
            </div>
            
            
            <br>

            
            <div class="medium-6 medium-centered columns">
                <fieldset class="fieldset">
                    <legend>Forum administrator</legend>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Username
                                <input type="text" name="username">
                            </label>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Email
                                <input type="text" name="email">
                            </label>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Password
                                <input type="text" name="password1">
                            </label>
                        </div>
                    </div>
                    
                    <div class="row">
                        <div class="medium-6 medium-centered columns">
                            <label>Password
                                <input type="text" name="password2">
                            </label>
                        </div>
                    </div>
                </fieldset>
            </div>

            <div class="medium-6 medium-centered columns">
                <h5 class="helper">By installing, you agree that I ain't responsible for no data breach, mmkay?</h5>
            </div>
            
            
            <div class="medium-6 medium-centered columns">
                <button type="submit" class="button right">Install</button>
            </div>
        </form>
    
    </body>
    <script src="${request.static_url('bulbs:static/js/vendor/jquery.js')}"></script>
    <script>
    $("#dbtype").change(function() {
        var disableDbSection = $(this).val() == "sqlite3";
        
        $("#dbfieldset input[type=text]").prop("disabled", disableDbSection);
    });
    </script>
</html>
