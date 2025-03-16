import requests

# Define the API URL (Update if running on a different port)
API_URL = "http://127.0.0.1:5000/question_generator"

# Test data
test_payload = {
    "job_role": "Software Engineer",
    "interview_type": "Technical",
    "job_desc": "Design and develop scalable backend systems."
}

# Send a POST request to Flask API
try:
    response = requests.post(API_URL, json=test_payload)

    # Check if request was successful
    if response.status_code == 200:
        print("API Call Successful!\n")

        # Print the response in a readable format
        data = response.json()
        print("Generated Questions:")
        for idx, question in enumerate(data.get("questions", []), start=1):
            print(f"{idx}. {question}")

    else:
        print(f"API Error! Status Code: {response.status_code}")
        print(response.json())

except requests.exceptions.RequestException as e:
    print(f" Request failed: {e}")
