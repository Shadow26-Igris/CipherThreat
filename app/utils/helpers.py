# helpers.py
import random

# Function to check if a file has a valid extension
def allowed_file(filename, allowed_extensions):
    """
    Checks if the file extension is allowed.
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

# Mock function to simulate vulnerability scanning
def scan_vulnerabilities(file_path):
    """
    This function simulates a vulnerability scan.
    In a real-world scenario, this function would scan the file for vulnerabilities
    and return a list of detected issues along with their severity.
    """
    vulnerabilities = {
        'Safe': [],
        'High': ['Buffer Overflow', 'SQL Injection'],
        'Medium': ['Cross-Site Scripting', 'Directory Traversal'],
        'Low': ['Information Disclosure']
    }

    # Simulate a random scan result (replace with real scan logic or API call)
    risk_level = random.choice(['High', 'Medium', 'Low', 'Safe'])
    return vulnerabilities[risk_level], risk_level
