<%inherit file="base.mako"/>

<form method="POST">
    <div class="row">
        <div class="large-6 columns">
            <label>Username
                <input type="text" name="username"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 columns">
            <label>Password
                <input type="password" name="password1"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 columns center">
            <label>Password again
                <input type="text" name="password2"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 columns">
            <label>E-mail
                <input type="text" name="email"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 large-offset-4 columns">
            <button type="submit" class="button">Sign up</button>
        </div>
    </div>
</form>
