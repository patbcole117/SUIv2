$(document).ready(function(){
    $("#filterInput").on("keyup", function() {
      var value = $(this).val().toLowerCase();
      $("#filterBody tr").filter(function() {
        $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
      });
    });
  });
  
$(function() {
    $("#filterTable").tablesorter();
});

$(function() {
    $("#filterTable").tablesorter({ sortList: [[0,0], [1,0]] });
});