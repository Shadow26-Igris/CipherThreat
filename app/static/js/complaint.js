document.getElementById('complaintForm').addEventListener('submit', function (event) {
    event.preventDefault();

    const complaintText = document.getElementById('complaint').value;

    fetch('/complaint/complaint', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ complaint: complaintText })
    })
    .then(response => {
        // Check if the response is JSON
        if (!response.ok) {
            return response.text().then(text => {
                throw new Error(text || 'Error submitting complaint');
            });
        }
        return response.json(); // Parse the response as JSON
    })
    .then(data => {
        alert(data.message);  // Show success message from JSON response
    })
    .catch(error => {
        console.error('Error:', error.message);
        alert(error.message);  // Show the error message
    });
});
