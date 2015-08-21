<%inherit file="base.mako"/>

<script src="/static/ckeditor/ckeditor.js"></script>

<form method="POST" role="form">
    <div class="form-group">
        <label>Subject</label>
        <input type="text" class="form-control" value="${title}" name="subject">
        
        <a href="/markup_help">Markup help</a>

        <br>
            <textarea name="message" rows="8" class="form-control">${message}</textarea>
            
        <div style="padding-top: 10px; float: right">
            <button type="submit" class="btn btn-default">Post reply</button>
        </div>
    </div>
</form>