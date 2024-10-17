window.addEventListener('scroll', function() {
    var navbar = document.querySelector('.navbar');

    // Si el usuario se ha desplazado más de 50 píxeles
    if (window.scrollY > 10) {
        navbar.classList.add('scrolled');
    } else {
        navbar.classList.remove('scrolled');
    }
});