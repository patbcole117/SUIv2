$('#top').load('/e_top');
$('#current_bout').load('/e_current_bout_table');
$('#clock').load('/e_clock');
$('#sbo').load('/e_sbo_config');
$('#sdc').load('/e_sdc_config');
$('#sui').load('/e_sui_config');

setInterval(function(){
    $('#clock').load('/e_clock');
}, 500);

setInterval(function(){
    $('#current_bout').load('/e_current_bout_table');
}, 30000);