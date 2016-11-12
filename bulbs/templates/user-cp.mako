<%inherit file="base.mako"/>

<br>

<form method="POST">
    <div class="row">
        <div class="large-4 columns">
            <label>New password
                <input type="password" name="new_password"/>
            </label>
        </div>
        
        <div class="large-4 columns left">
            <label>New password again
                <input type="password" name="new_password2"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-4 columns center">
            <label>Email
                <input type="email" name="email" placeholder="$previous email^"/>
            </label>
        </div>

        <div class="large-4 columns">
            <label>Avatar
                <input type="file" name="avatar"/>
            </label>
        </div>
        
        <div class="large-4 columns">
            % if not None:
                <label style="padding-top: 10px">
                    <img src="http://i.somethingawful.com/forumsystem/emoticons/emot-smugdog.gif"/>
                </label>
            % endif
        </div>
    </div>
    
    <div class="row">
        <div class="large-4 columns">
            <label>Real name
                <input type="text" name="real_name"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-4 columns">
            <label>City
                <input type="text" name="city"/>
            </label>
        </div>
        
        <div class="large-4 columns">
            <label>State/Province
                <input type="text" name="state"/>
            </label>
        </div>
        
        <div class="large-4 columns">
            <label>Country
                <input type="text" name="country"/>
            </label>
        </div>
    </div>

    
    <div class="row">
        <div class="large-12 columns">
            <label>Biography
                <textarea rows="6" name="bio"></textarea> <br>
            </label>
        </div>
    </div>
    
    <hr class="seperator">
    
    <div class="row">
        <div class="large-6 columns">
            <p>You must enter your current password to save these changes.</p>
        
            <label>Current password *
                <input type="password" name="current_password"/>
            </label>
        </div>
    </div>
    
    
    <div class="row">
        <div class="large-6 large-offset-4 columns">
            <button type="submit" class="button">Save changes</button>
        </div>
    </div>
</form>

<script>
$(function() {
    $("#nav-user-cp").addClass("active");
});
</script>
