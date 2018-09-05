


// //COOKIE SYSTEM
// document.cookie = "userdata="+JSON.stringify({money: 1000, baz: 'poo'});


//PRICE UPDATING BASED ON API

//BITCOIN
function send_request(){

    // CoinCompare API ACCESS
    var request = new XMLHttpRequest();

    request.open("GET","https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD", true);

    request.onload= function(){

        // GET data access
        var data = JSON.parse(this.response);

        document.getElementById("BTC_price").innerHTML = "$ "+data.USD;
        document.getElementById("transact_price").value = data.USD;
        console.log("transact_price =", document.getElementById("transact_price").value)
    }

    request.send();

}

send_request();

setInterval(function(){

    send_request();

//UPDATE EVERY 10 SECONDS
},10*1000);



