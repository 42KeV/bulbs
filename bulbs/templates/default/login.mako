<%inherit file="base.mako"/>

<p>New to ${project}? <a href="/register">Register</a> now and recieve free cookies!</p>

<div class="input-box">
    <div class="pull-right">
        <div class="col-sm-offset-7">
            <div class="col-sm-10">
                <p>Enter your username and password to gain access to restricted content, the ability to create new threads and reply to others.</p>
                
                <h4>Help</h4>
                    <ul>
                        <li><a href="#">I've forgotten my username/password</a></li>
                        <li><a href="#">My account was hacked!</a></li>
                    </ul>
            </div>
        </div>
    </div>
    
    <form class="form-horizontal" method="POST" role="form">
        <div class="form-group">
            <label for="username" class="col-sm-2 control-label">Username</label>
            <div class="col-sm-5">
                <input type="text" class="form-control" name="username">
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">Password</label>
            <div class="col-sm-5">
                <input type="password" class="form-control" name="password">
            </div>
        </div>
        
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-2">
                <button type="submit" class="btn btn-default">Sign in</button>
            </div>
        </div>
    </form>
</div>