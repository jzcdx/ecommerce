let cards = document.getElementsByClassName("card");

for (let i = 0; i < cards.length; i++) {
    cards[i].addEventListener("click", (event) => {
        var clicked_id = event.currentTarget.id.split("_")[1];
    }); 
}
