function addToCart(productId, productName, productStock) {
    var productQtty = document.getElementById("qttyInput").value
    
    if (productQtty > 0 && productStock >= productQtty) { /*should probably make the stock check server side later too lol*/
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
                var addedLabel = document.getElementById("added-label")
                addedLabel.style.display = "block";
            } 
        });
    } else {
        if (productQtty <= 0) {
            console.log("cart request qtty <= 0");
        } else if (productStock < productQtty) {
            console.log("not enough stock");
        }
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