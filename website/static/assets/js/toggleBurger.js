const toggleBurger = () => {
    const burger = document.querySelector('.toggle-navbar')
    const navMenu = document.querySelector('.navbar-nav')
    burger.addEventListener('click', () => {
        navMenu.classList.toggle('navbar-nav-toggle')
    })
}
toggleBurger()