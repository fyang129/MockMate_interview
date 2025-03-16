import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
from dotenv import load_dotenv
# import google.generativeai as genai
from google import genai
from google.genai import types


load_dotenv()

app = Flask(__name__)
CORS(app)

#Gemini api
GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/question_generator', methods=['POST'])
def get_questions():

    data = request.json
    job_role = data.get("job_role", "").strip()
    interview_type = data.get("interview_type", "").strip()
    job_desc = data.get("job_desc", "").strip()
    exp_level = data.get("exp_level", "").strip()

    # Validate: At least one input should be provided
    if not job_role and not job_desc:
        return jsonify({"error": "Please enter your job role or description"}), 400

    # Construct a dynamic prompt based on provided inputs
    prompt = ("""

              Use this exact JSON schema for the response.
              {
              "Generated_questions": {
                  "job_role": "<job_role>",
                  "interview_type": "<interview_type>",
                  "questions": [
                      "Question 1",
                      "Question 2",
                      "Question 3",
                      ...
                      "Question 10",
                      
                  ]
              }
          }
              - Ensure the response follows the JSON format exactly.
              - Do NOT add unnecessary quotation marks or special characters.
              - Only return the JSON object, no extra text.
              - Only include **job-relevant** technical and behavioral interview questions.
              - **DO NOT** include questions related to salary expectations, work authorization, personal information, or legal status.
              - The questions must assess **skills, experience, and problem-solving abilities** related to the job role.
              - Do NOT include duplicate or overly generic questions.
              
              - Please generate 10 unique job interview questions base on the information below.
              
              """)

    # Generated_questions = {'job_role': str, 'questions': list[str]}
    # Return: questions]


    if job_role:
        prompt += f" The job role is {job_role}."
    if interview_type:
        prompt += f" The interview type is {interview_type}."
    if job_desc:
        prompt += f" Here is the job description: {job_desc}"
    if exp_level:
        prompt += f" The exprience level is {exp_level}"


    # print(prompt)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    answer = response.text
    # print(answer)

    if not response or not hasattr(response, "text"):
        return jsonify({"error": "Failed to get a valid response from Gemini API"}), 500


    return answer

    # chat = model.start_chat(history=[])
    # response = chat.send_message(prompt)
    # print(response.text)


    #return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True,port = 5000)

    # # API request to Gemini (local testing)
    # headers = {
    #     "Authorization": f"Bearer {GEMINI_API_KEY}",
    #     "Content-Type": "application/json"
    # }
    #
    # payload = {
    #     "model": model,
    #     "messages": [{"role": "user", "content": prompt}]
    # }
    #
    # # Send request to Gemini API (local endpoint for testing)
    # try:
    #     response = requests.post("http://localhost:8080/v1/chat/completions", json=payload, headers=headers)
    #
    #     print("Response Status Code:", response.status_code)
    #     print("Response Text:", response.text)
    #
    #     if response.status_code == 200:
    #         return jsonify(response.json())  # Directly return entire API response
    #         # generated_text = response.json()["choices"][0]["message"]["content"]
    #         # #
    #         # # Convert text response into a structured list of questions
    #         # questions = [q.strip() for q in generated_text.split("\n") if q.strip()]
    #
    #         return jsonify({"questions": generated_text})
    #     else:
    #         return jsonify({"error": "Failed to fetch questions from local Gemini API"}), 500
    #
    # except requests.exceptions.RequestException as e:
    #     return jsonify({"error": f"Request to Gemini API failed: {str(e)}"}), 500
    #
    # # # Handle API response
    # # if response.status_code == 200:
    # #     generated_text = response.json()["choices"][0]["message"]["content"]
    # #
    # #     # Convert text response into a structured list of questions
    # #     questions = [q.strip() for q in generated_text.split("\n") if q.strip()]
    # #
    # #     return jsonify({"questions": questions})
    # # else:
    # #     return jsonify({"error": "Failed to fetch questions from Gemini API"}), 500
    #
    #
    #
    #

# def ask():
#     user_question = request.form.get('question')
#     if not user_question:
#         return jsonify({'error': 'No question provided'}), 400
#
#     try:
#         # Interact with Gemini API
#         chat = model.start_chat(history=[])
#         response = chat.send_message(user_question)
#         answer = response.text
#         return jsonify({'answer': answer})
#     except Exception as e:
#         return jsonify({'error': str(e)}), 500

#C:\Users\episo\OneDrive\Documents\Python Scripts\Mock1\.venv\Scripts