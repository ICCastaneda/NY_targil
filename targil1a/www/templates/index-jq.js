var Handle_index_html = "Handle_index_html";


$(document).ready(function(){
    $("#id_btnreg").click(function(){
        alert("Hello! I am an alert box!!");
    });
});
function formpostfunc(){
        //alert("Hello! I am an alert box!!");
        var user = $('#id_un').val();
        var pass = $('#id_pw').val();
        $.ajax({
            url: '/add_event',
            data: $('form').serialize(),
            type: 'POST',
            success: function(response) {
                alert(response["add_event"]);
            },
            error: function(error) {
                console.log(error);
            }
        })
};

//console.log("in func1");
//.- sendform.js     file 
    //$(function() {
    //$('#id_btnreg').click(function() {
//$("#buildyourform").on('click', '#id_btnreg', function () { 

