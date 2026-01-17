import requests
from flask import Blueprint, render_template, request

scan_routes = Blueprint('scan_routes', __name__)

# Replace with your VirusTotal API key or other scanning service API key
API_KEY = "ae556191930cc3d88ebf22c1240835d5e4da6e41a10827a4fa489628ab07ce2f"
API_URL = "https://www.virustotal.com/api/v3/files"

@scan_routes.route('/scan', methods=['GET', 'POST'])
def scan_file():
    if request.method == 'POST':
        # Get the uploaded file
        uploaded_file = request.files.get('file')
        if not uploaded_file:
            return "No file uploaded!", 400

        # Send the file to the VirusTotal API
        files = {"file": (uploaded_file.filename, uploaded_file.stream, uploaded_file.content_type)}
        headers = {"x-apikey": API_KEY}

        try:
            response = requests.post(API_URL, files=files, headers=headers)
            if response.status_code == 200:
                # Parse the API response
                data = response.json()
                scan_results = [
                    {"name": scanner, "result": details["result"] or "Safe", "method": "External Scan"}
                    for scanner, details in data.get("data", {}).get("attributes", {}).get("last_analysis_results", {}).items()
                ]

                # Calculate summary counts
                safe_count = sum(1 for result in scan_results if result["result"] == "Safe")
                malicious_count = sum(1 for result in scan_results if result["result"] == "Malicious")
                unsupported_count = len(scan_results) - safe_count - malicious_count

                # Determine final verdict
                verdict = "Potential risk detected." if malicious_count > 0 else "The file appears safe."

                # Render the results page
                return render_template(
                    "scan_results.html",
                    scan_results=scan_results,
                    safe_count=safe_count,
                    malicious_count=malicious_count,
                    unsupported_count=unsupported_count,
                    verdict=verdict
                )
            else:
                # Handle API errors
                return f"Error from API: {response.status_code} - {response.text}", 500
        except requests.RequestException as e:
            return f"Error connecting to the API: {str(e)}", 500

    # Render the file upload form for GET requests
    return render_template("scan_file.html")
