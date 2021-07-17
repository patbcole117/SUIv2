$('#current_bout').load('/e_current_bout_table');
$('#clock').load('/e_clock');
$('#top').load('/e_top');

setInterval(function(){
    $('#clock').load('/e_clock');
}, 500);

setInterval(function(){
    $('#current_bout').load('/e_current_bout_table');
}, 30000);
