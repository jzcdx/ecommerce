function addToCart(productId, productName) {
    var productQtty = document.getElementById("qttyInput").value
    if (productQtty > 0) {
        console.log("adding " + productId + " to cart " + productName);
        var newCartItemData = {
            "product_qtty": productQtty,
            "product_name": productName, 
            "product_id": productId
        };

        $.ajax({
            type: "POST", //method
            url: "/addToCart", //this is the flask route
            data: JSON.stringify(newCartItemData), //I have no idea what this is
            contentType: "application/json",
            dataType: 'json', 
            success: function(result) { //when the response comes back and it's successful, run the code below
                //This updates the description with the new value from the textarea
                console.log("request made");
            } 
        });
    } else {
        console.log("req not sent, prod qtty <= 0");
    }
}

function increaseQtty() {
    var qttyInput = document.getElementById("qttyInput");
    var curQtty = parseInt(qttyInput.value);

    qttyInput.value = curQtty + 1;
}

function decreaseQtty() {
    var qttyInput = document.getElementById("qttyInput");
    var curQtty = parseInt(qttyInput.value);
    if (curQtty > 1) {
        qttyInput.value = curQtty - 1;
    }
}