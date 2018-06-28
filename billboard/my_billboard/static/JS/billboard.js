$("#my_form").hide();

$(".show_form").click(function(){
    $("#my_form").show();
    $('#show_buttons').hide();
    $('.empty').hide();
});

$(".close_form").click(function(){
    $("#my_form").hide();
    $('#show_buttons').show();
});