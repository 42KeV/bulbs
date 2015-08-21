<%inherit file="base.mako"/>

<style>
.category-row {
    background-color: #F38630;
    font-weight: bold;
    text-align: center;
}
.subcategory-row {
    background-color: #E0E4CC;
}
</style>

% if is_logged_in:
    <p>Welcome back, ${request.session["user"]["username"]}</p>
% endif

% for category in categories:
<div class="panel panel-default">
    <div class="category-row">
        <div class="panel-heading">${category.get("title")}</div>
    </div>

    <table class="table">
    % for subcategory in subcategories:
        % if subcategory.get("category_id") == category.get("id"):
            <% lastpost = subcategory.get("last_post") %>
            <tr class="subcategory-row">
                <td class="subcategory-title">
                    <a href="/forum/${subcategory.get('id')}">${subcategory.get("title")}</a>
                    <div class="subcategory-desc">${subcategory.get("desc")}</div>
                </td>
                <td>
                    <div class="pull-right">
                        Threads: ${subcategory.get("threads")} <br>
                        Replies: ${subcategory.get("posts")}
                    </div>
                </td>
                <td>
                    % if lastpost is not None:
                        <div class="pull-right">
                            Last post was made by 
                            <a href="${lastpost.get('username')}">${lastpost.get("username")}</a>
                            <a href="#"><i class="fa fa-arrow-circle-right"></i></a>
                        </div>
                    % endif
                </td>
            </tr>
        % endif
    % endfor
    </table>
</div>
% endfor
