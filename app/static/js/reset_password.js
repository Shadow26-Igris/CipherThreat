// reset_password.js
document.addEventListener('DOMContentLoaded', function() {
    const resetPasswordForm = document.getElementById('reset-password-form');
    if (resetPasswordForm) {
        resetPasswordForm.addEventListener('submit', function(event) {
            const password = document.getElementById('password').value;
            const confirmPassword = document.getElementById('confirm-password').value;

            if (password !== confirmPassword) {
                event.preventDefault();
                alert('Passwords do not match.');
            } else if (password.length < 8) {
                event.preventDefault();
                alert('Password must be at least 8 characters long.');
            }
        });
    }
});
