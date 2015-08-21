<%inherit file="base.mako"/>

% if is_logged_in:
    <form method="POST" role="form">
        <div class="form-group">
            <label>Subject</label>
            <input type="text" class="form-control" name="subject">
            
            <label>Message</label>
            <textarea class="form-control" rows="12" name="message"></textarea>
            
            <div style="padding-top: 10px; float: right">
                <button type="submit" class="btn btn-default">Post thread</button>
            </div>
        </div>
    </form>
% else:
    <h1>Error</h1>
    <p>You are not authorized to view this page</p>
% endif