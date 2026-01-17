// Smooth Scroll for Internal Links
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Get the navigation bar element
const navbar = document.querySelector('.links-section');

// Function to toggle the fixed class
const toggleFixedNavbar = () => {
    if (window.scrollY > navbar.offsetTop) {
        navbar.classList.add('fixed');
    } else {
        navbar.classList.remove('fixed');
    }
};

// Listen to the scroll event
window.addEventListener('scroll', toggleFixedNavbar);

// Category Table View More Interaction
document.querySelectorAll('.cell').forEach(cell => {
    cell.addEventListener('mouseenter', () => {
        cell.querySelector('.view-more').style.display = 'inline-block';
    });

    cell.addEventListener('mouseleave', () => {
        cell.querySelector('.view-more').style.display = 'none';
    });
});
