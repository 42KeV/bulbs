<%inherit file="base.mako"/>

<a href="/user/${username}">Take me to my public profile</a>

<div class="input-box">
    <div class="pull-right">
        <div class="col-sm-offset-7">
            <div class="col-sm-10">
                <p>Provide your real name if you really want to get personal with the community.</p>
                <p>By providing your city and state, ${project} can display your local weather data, star charts and other cool things to make you feel at home.</p>
                <p>Write up a short or long biography about yourself, everyone loves reading extraordinarily long biographies that have a lot of text but say nothing.</p>
                <p>When choosing your avatar, you may upload a photo from your computer or use an external link, if your avatar is too large in dimensions it will be resized to the specifications set by the administrator, in addition if the file is too large in size the upload will fail.</p>
            </div>
        </div>
    </div>
    
    <form class="form-horizontal" method="POST" role="form">
        <div class="form-group">
            <label for="username" class="col-sm-2 control-label">Real name</label>
            <div class="col-sm-5">
                <input type="text" class="form-control" name="name">
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">City</label>
            <div class="col-sm-5">
                <input type="password" class="form-control" name="city">
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">State</label>
            <div class="col-sm-5">
                <input type="password" class="form-control" name="state">
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">Biography</label>
            <div class="col-sm-5">
                <textarea class="form-control" rows="4" name="bio"></textarea>
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">E-mail</label>
            <div class="col-sm-5">
                <input type="email" class="form-control" name="email">
            </div>
        </div>
        
        <div class="form-group">
            <label for="password" class="col-sm-2 control-label">Avatar</label>
            <div class="col-sm-5">
                <input type="text" class="form-control" name="avatar">
            </div>
        </div>
        
        <div class="form-group">
            <div class="col-sm-offset-2 col-sm-2">
                <button type="submit" class="btn btn-default">Save changes</button>
            </div>
        </div>
    </form>
</div>

<br>