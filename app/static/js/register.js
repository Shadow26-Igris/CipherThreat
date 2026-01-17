document.getElementById('registerForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('/register', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            alert('Registration successful! You can now login.');
            window.location.href = 'login.html';  // Redirect to login page after successful registration
        } else {
            alert('Registration failed. Please try again.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('An error occurred. Please try again.');
    });
});
document.querySelector('form').addEventListener('submit', (e) => {
    const phone = document.getElementById('phone').value;
    const age = document.getElementById('age').value;
    
    // Validate phone number
    if (!/^\d{10}$/.test(phone)) {
        alert("Phone number must be 10 digits.");
        e.preventDefault();
    }

    // Validate age
    if (age < 1 || age > 120) {
        alert("Please enter a valid age.");
        e.preventDefault();
    }
});
