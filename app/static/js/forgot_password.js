// forgot_password.js
document.addEventListener('DOMContentLoaded', function() {
    const forgotPasswordForm = document.getElementById('forgot-password-form');
    if (forgotPasswordForm) {
        forgotPasswordForm.addEventListener('submit', function(event) {
            const email = document.getElementById('email').value;
            if (!validateEmail(email)) {
                event.preventDefault();
                alert('Please enter a valid email address.');
            }
        });
    }

    // Email validation function
    function validateEmail(email) {
        const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        return re.test(String(email).toLowerCase());
    }
});
