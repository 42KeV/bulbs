<%inherit file="../base.mako"/>

<div class="row">
    <section class="large-12 columns action-info">
        <p>By filling out this form, you will create a new category for ${project}. Categories are used for forum structure, seperating things that are alike under one section</p>
    </section>
</div>

<form method="POST">
    <div class="row">
        <div class="large-6 columns">
            <label>Name
                <input type="text" name="subcatname"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 columns">
            <label>Description
                <input type="text" name="subcatdesc"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 columns">
            <label>Category
                <select name="catid">
                    % for category in categories:
                        <option value="${category.get('id')}">${category.get("title")}</option>
                    % endfor
                </select>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 columns">
            <label>Sorting rank
                <input type="text" name="subcatrank"/>
            </label>
        </div>
    </div>
    
    <div class="row">
        <div class="large-6 columns">
            <label>Slug
                <input type="text" name="subcatslug" placeholder="gp4kg4ogk"/>
            </label>
        </div>
    </div>
    
    
    <div class="row">
        <div class="large-6 columns">
            <input class="right button" type="submit" value="Create"/>
        </div>
    </div>
</form>

