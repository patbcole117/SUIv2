$('#clock').load('/e_clock');
$('#current_bout').load('/e_current_bout_table');
$('#latest_bouts').load('/e_latest_bouts_table');
$('#latest_fighters').load('/e_latest_fighters_table');
$('#top').load('/e_top');

setInterval(function(){
    $('#clock').load('/e_clock');
}, 500);

setInterval(function(){
    $('#current_bout').load('/e_current_bout_table');
}, 30000);

setInterval(function(){
    $('#latest_bouts').load('/e_latest_bouts_table');
}, 60000);

setInterval(function(){
    $('#latest_fighters').load('/e_latest_fighters_table');
}, 60000);