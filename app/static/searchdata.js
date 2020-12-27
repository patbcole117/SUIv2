$('#clock').load('/e_clock');
$('#current_bout').load('/e_current_bout_table');
$('#top').load('/e_top');

if (document.title == "Bouts"){
    $('#table').load('/e_bouts');
} else {
    $('#table').load('/e_fighters');
}



setInterval(function(){
    $('#clock').load('/e_clock');
}, 500);

setInterval(function(){
    $('#current_bout').load('/e_current_bout_table');
}, 30000);
