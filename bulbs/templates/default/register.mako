<%inherit file="base.mako"/>



<p>You can sign up to ${project} by entering your information here.</p>

<div class="input-box">
    <div class="pull-right">
        <div class="col-sm-offset-7">
            <div class="col-sm-10">
                <div class="tos">
                    <h2>
                        <a href="/tos">Terms Of Service</a>
                    </h2>
                        <p>By registering on this forum, you agree to have read the Terms Of Service and Privacy Policy</p>
                </div>
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
                <input type="password" class="form-control" name="password1">
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">Password</label>
            <div class="col-sm-5">
                <input type="password" class="form-control" name="password2">
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">E-mail</label>
            <div class="col-sm-5">
                <input type="email" class="form-control" name="email">
            </div>
        </div>
        
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-2">
                <button type="submit" class="btn btn-default">Register</button>
            </div>
        </div>
    </form>
</div>