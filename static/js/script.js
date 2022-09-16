function normalNews(x) {
  x.className = 'list-group-item list-group-item-action';
}

function activeNews(x) {
  x.className = 'list-group-item list-group-item-action active';
}

function normalNav(x) {
  x.className = 'list-group-item list-group-item-action dropdown-toggle';
}

function activeNav(x) {
  x.className = 'list-group-item list-group-item-action dropdown-toggle active';
}

$(document).ready(function(){
    $(".dropright").hover(function(){
        var dropdownMenu = $(this).children(".dropdown-menu");
        if(dropdownMenu.is(":visible")){
            dropdownMenu.parent().toggleClass("open");
        }
    });
});
function normal(x) {
  x.className = 'list-group-item list-group-item-action';
}

function active(x) {
  x.className = 'list-group-item list-group-item-action active';
}

$(function() {
    $('.form-check-input').click(function() {
        if ($('.form-check-input').is(':checked')) {
            $('#submit').removeAttr('disabled');
        } else {
            $('#submit').attr('disabled', 'disabled');
        }
    });
});
function func() {
    document.getElementById('b-delete').value = 'delete';
}
function showPhone() {
    document.getElementById('phone-1').style.display = 'grid';
    document.getElementById('show-b-p').style.display = 'none';
}
function showEmail() {
    document.getElementById('email-1').style.display = 'grid';
    document.getElementById('show-b-e').style.display = 'none';
}