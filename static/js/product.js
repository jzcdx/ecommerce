function addToCart(productId, productName) {
    console.log("adding " + productId + " to cart " + productName);

    var newItemData = {
        "product_name": productName, 
        "product_id": productId
    };

    $.ajax({
        type: "POST", //method
        url: "/addToCart", //this is the flask route
        data: JSON.stringify(newItemData), //I have no idea what this is
        contentType: "application/json",
        dataType: 'json', 
        success: function(result) { //when the response comes back and it's successful, run the code below
            //This updates the description with the new value from the textarea
            console.log("request made");
        } 
    });
}