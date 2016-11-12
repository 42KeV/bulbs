<%inherit file="base.mako"/>

<br>

<form method="POST">
    <div class="row">
        <div class="large-12 columns">
            <label>Subject
                <input type="text" value="In reply to [${replying_to}]" name="subject">
            </label>
        </div>
    </div>

    <div class="row">
        <div class="large-12 columns">
            <label>Message
                <textarea rows=12 name="message"></textarea>
            </label>
        </div>
    </div>
    
    <br>
    
    <div class="row">
        <div class="large-2 columns right">
            <button type="submit" class="button right">Submit</button>
        </div>
    </div>
</form>
