var items = document.getElementById("e_config_items").innerHTML
document.getElementById("e_config_items").innerHTML = JSON.stringify(items, undefined, 2)
console.log(items)