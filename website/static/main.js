const liczby = document.getElementsByClassName("card-text");
for (let i = 0; i < liczby.length; i++) {
    const x = parseFloat(liczby[i].innerHTML);
    const y = Math.floor(x * 2);
    const half = y % 2;
    const full = (y - half) / 2;
    liczby[i].innerHTML += '<i class="bi bi-star-fill" style="color: #FF9E00"></i>'.repeat(full);
    if (half >0){
        liczby[i].innerHTML += '<i class="bi bi-star-half" style="color: #FF9E00"></i>';
        liczby[i].innerHTML += '<i class="bi bi-star" style="color: #FF9E00"></i>'.repeat(5-(full+half));
    }
    if (full === 0.0){
        liczby[i].innerHTML="Brak ocen"
    }

}