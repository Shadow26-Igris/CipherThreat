document.getElementById("vulnerability-upload-form").addEventListener("submit", function(e) {
    e.preventDefault();

    const formData = new FormData(this);
    const loadingText = document.getElementById("loading");
    const resultSection = document.getElementById("result");
    const riskLevelElement = document.getElementById("risk-level");
    const vulnerabilitiesList = document.getElementById("vulnerabilities-list");

    // Show loading message
    loadingText.style.display = "block";
    resultSection.style.display = "none";

    // Check if file is selected
    if (!formData.has("file")) {
        alert("No file selected!");
        loadingText.style.display = "none";
        return;
    }

    // Send the file to the backend for vulnerability scanning
    fetch("/scan_vulnerability", {
        method: "POST",
        body: formData,
    })
    .then(response => response.json())
    .then(data => {
        // Hide loading message
        loadingText.style.display = "none";

        if (data.vulnerabilities) {
            // Show the scan results
            riskLevelElement.textContent = data.risk_level;
            vulnerabilitiesList.innerHTML = '';

            data.vulnerabilities.forEach(function(vulnerability) {
                const listItem = document.createElement("li");
                listItem.textContent = vulnerability;
                vulnerabilitiesList.appendChild(listItem);
            });
        } else {
            riskLevelElement.textContent = "Error";
            vulnerabilitiesList.innerHTML = "Unable to scan the file. Please try again.";
        }

        resultSection.style.display = "block";
    })
    .catch(error => {
        loadingText.style.display = "none";
        riskLevelElement.textContent = "Error";
        vulnerabilitiesList.innerHTML = "Something went wrong.";
        resultSection.style.display = "block";
    });
});
