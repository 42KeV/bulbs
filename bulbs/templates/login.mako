<%inherit file="base.mako"/>

<br>

<form method="POST">
    <div class="container">
        <div class="row">
            <div class="large-6 large-centered columns">
                <label>Username
                    <input type="text" name="username">
                </label>
            </div>            
        </div>
        
        <div class="row">
            <div class="large-6 large-centered columns">
                <label>Password
                    <input type="password" name="password">
                </label>
            </div>            
        </div>
        
        <div class="row">
            <div class="large-6 large-centered columns">
                <button type="submit" class="button right">Sign in</button>
            </div>
        </div>
    </div>
</form>

<script>
$(function() {
    $("#nav-sign-in").addClass("active");
});
</script>
