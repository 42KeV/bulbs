<%inherit file="base.mako"/>

<form method="POST">
    <div class="row">
        <div class="small-5 small-centered columns">
            <div class="row"> 
                <div class="small-3 columns">
                    <label for="right-label" name="username" class="right inline">Username</label>
                </div>
                
                <div class="small-9 columns">
                    <input type="text" name="username">
                </div>
            </div>
        </div>
    </div>
    
    <div class="row">
        <div class="small-5 small-centered columns">
            <div class="row"> 
                <div class="small-3 columns">
                    <label for="right-label" class="right inline">Password</label>
                </div>
                
                <div class="small-9 columns">
                    <input type="password" name="password">
                </div>
            </div>
        </div>
    </div>
    
    <div class="row">
        <div class="small-5 columns right">
            <button type="submit" class="button">Sign in</button>
        </div>
    </div>
</form>
