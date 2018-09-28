

console.log("coin_type =", document.getElementById("coin_type").value)

//PRICE UPDATING BASED ON API

//BITCOIN

if ( document.getElementById("coin_type").value == "BTC" ) {
    
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
    
} else if (document.getElementById("coin_type").value == "ETH") {
    //ETHERUM
    
    
    function send_request(){

        // CoinCompare API ACCESS
        var request = new XMLHttpRequest();
    
        request.open("GET","https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD", true);
    
        request.onload= function(){
    
            // GET data access
            var data = JSON.parse(this.response);
    
            document.getElementById("BTC_price").innerHTML = "$ "+data.USD;
            document.getElementById("transact_price").value = data.USD;
            console.log("transact_price =", document.getElementById("transact_price").value)
        }
    
        request.send();
    }  
} else if (document.getElementById("coin_type").value == "NANO") {
    
    //NANOCOIN
    
    function send_request(){

        // CoinCompare API ACCESS
        var request = new XMLHttpRequest();
    
        request.open("GET","https://min-api.cryptocompare.com/data/price?fsym=NANO&tsyms=USD", true);
    
        request.onload= function(){
    
            // GET data access
            var data = JSON.parse(this.response);
    
            document.getElementById("BTC_price").innerHTML = "$ "+data.USD;
            document.getElementById("transact_price").value = data.USD;
            console.log("transact_price =", document.getElementById("transact_price").value)
        }
    
        request.send();
    }  

}






send_request();

setInterval(function(){

    send_request();

//UPDATE EVERY 10 SECONDS
},10*1000);



