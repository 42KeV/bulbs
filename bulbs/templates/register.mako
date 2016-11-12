<%inherit file="base.mako"/>

<br>

<form method="POST">
    <div class="container">
        <div class="row">
            <div class="large-6 large-centered columns">
                <label>Username
                    <input type="text" name="username"/>
                </label>
            </div>            
        </div>
        
        <div class="row">
            <div class="large-6 large-centered columns">
                <label>Password
                    <input type="password" name="password1"/>
                </label>
            </div>            
        </div>
        
        <div class="row">
            <div class="large-6 large-centered columns">
                <label>Password again
                    <input type="password" name="password2"/>
                </label>
            </div>            
        </div>
        
        <div class="row">
            <div class="large-6 large-centered columns">
                <label>E-mail
                    <input type="text" name="email"/>
                </label>
            </div>            
        </div>
        
        <div class="row">
            <div class="large-6 large-centered columns">
                <button type="submit" class="button right">Sign up</button>
            </div>
        </div>
    </div>
</form>
