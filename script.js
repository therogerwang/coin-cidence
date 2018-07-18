
//console.log("script loaded");

// Coinmarket Cap API Access
var request = new XMLHttpRequest();

request.open("GET","https://api.coinmarketcap.com/v2/listings/", true);

request.onload= function(){

    // GET data access
    var data = JSON.parse(this.response);

    console.log(data);

    // data.forEach(thing => {
    //     console.log(thing.data);
    // });


}

request.send();