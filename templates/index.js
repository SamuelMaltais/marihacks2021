// for(var i = 0; i< "insertFelixshithere".rows.length; i++){
//     var div = document.createElement('div');
//     var textnode = document.createTextNode("Name: {0}\n"+"Address: {1}\n"+"Longitude: {2}\n"+"Latitude: {3}\n"+"Phone Number: {4}", name, address, longitude, latitude, phoneNumber);
//     div.class = 'location';
//     document.getElementById("locations").appendChild(div);

//     var a = document.createElement('a');
//     a.class = 'name';
//     document.getElementById("dropdown-content").appendChild(a);
// }

function myFunction(newitemh) {
    var x = document.createElement("INPUT");
    x.setAttribute("type", "radio");
    x.addAttribute("name", "item");
    x.addAttribute("value", newitemh);
    document.newitems.appendChild(x);
  }   