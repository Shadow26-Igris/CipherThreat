// Add an event listener to the "Scan Another File" button for animation effect
document.getElementById("scan-again").addEventListener("click", function() {
    this.classList.add("bounce");
    setTimeout(() => {
        this.classList.remove("bounce");
    }, 1000);
});

// Add bounce animation class to button
document.styleSheets[0].insertRule(`
    .bounce {
        animation: bounce 0.5s ease;
    }
`, document.styleSheets[0].cssRules.length);

// Bounce keyframe animation
document.styleSheets[0].insertRule(`
    @keyframes bounce {
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }
`, document.styleSheets[0].cssRules.length);

// Interactive file upload form - Show a loading spinner after file selection
document.getElementById("file-upload").addEventListener("change", function() {
    const loadingText = document.createElement("p");
    loadingText.textContent = "Scanning... Please wait.";
    loadingText.classList.add("loading-text");
    document.querySelector("form").appendChild(loadingText);

    setTimeout(() => {
        loadingText.remove(); // Remove loading text after a short delay (simulating file scan time)
    }, 2000); // Adjust the time based on your server response time
});
