<%inherit file="base.mako"/>

<script src="/static/ckeditor/ckeditor.js"></script>

% if is_logged_in:
    <form method="POST" role="form">
        <div class="form-group">
            <label>Subject</label>
            <input type="text" class="form-control" value="Re: ${replying_to} [${thread_title}]" name="subject">
            
            <a href="/markup_help">Markup help</a>
            
            <br>
            
            <label>Message</label>
                <textarea name="message" id="editor1"></textarea>
                
                <script>
                    CKEDITOR.replace( 'editor1' );
                </script>
            
            <div style="padding-top: 10px; float: right">
                <button type="submit" class="btn btn-default">Post reply</button>
            </div>
        </div>
    </form>
% else:
    <h1>Error</h1>
    <p>You are not authorized to visit this page</p>
% endif