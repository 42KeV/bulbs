<%inherit file="base.mako"/>

<div class="jumbotron">
    <h1>Bulbs documentation</h1>
        <p>Bulbs is currently in development, this page may be incomplete.</p>
        <p>Current version: 0.1</p>
</div>

<h2>Contents</h2>
<ul>
    <li><a href="#modules">Modules</a></li>
</ul>

<h1 id="modules" class="page-header">Modules</h1>
<h2>Post</h2>
    <p>This module controls all data input</p>
    
    <h3>make_thread(**kwargs)</h3>
        <div style="padding-left: 50px;">
            <p>arguments: <span class="text-muted">username, forum_id, post_subject, post_message, author_ip</span></p>
            <p>This is the function that inserts thread data into the database, 
        </div>
        
    <h3>make_reply(**kwargs)</h3>
        <div style="padding-left: 50px;">
            <p>arguments: <span class="text-muted">username, thread_id, post_subject, post_message, author_ip</span></p>
        </div>