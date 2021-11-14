var liczby = document.getElementsByClassName("card-text");
for (i = 0; i < liczby.length; i++) {
    console.log(liczby[i].innerHTML);
    var x = parseFloat(liczby[i].innerHTML);
    var y = Math.floor(x * 2);
    var half = y % 2;
    const full = (y - half) / 2;
    console.log(5-(full+half))
    liczby[i].innerHTML += '<i class="bi bi-star-fill" style="color: #FF9E00"></i>'.repeat(full);
    if (half >0){
        liczby[i].innerHTML += '<i class="bi bi-star-half" style="color: #FF9E00"></i>';
    }
    if (isNaN(x)){
        liczby[i].innerHTML="Brak ocen"
    }
    liczby[i].innerHTML += '<i class="bi bi-star" style="color: #FF9E00"></i>'.repeat(5-(full+half));
}