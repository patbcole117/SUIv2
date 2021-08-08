$('#current_bout').load('/e_current_bout_table');
$('#latest_bouts').load('/e_latest_bouts_table');
$('#latest_fighters').load('/e_latest_fighters_table');
$('#clock').load('/e_clock');
$('#sbo').load('/e_sbo_config');
$('#sdc').load('/e_sdc_config');
$('#sui').load('/e_sui_config');

setInterval(function(){
    $('#clock').load('/e_clock');
}, 500);

setInterval(function(){
    $('#current_bout').load('/e_current_bout_table');
}, 10000);

setInterval(function(){
    $('#latest_bouts').load('/e_latest_bouts_table');
}, 60000);

setInterval(function(){
    $('#latest_fighters').load('/e_latest_fighters_table');
}, 60000);
