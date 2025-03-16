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

    if not job_role and not job_desc:
        return jsonify({"error": "Please enter your job role or description"}), 400

    prompt = ("""
              Use this exact JSON schema for the response.
              {
              "Generated_questions": {
                  "job_role": "<job_role>",
                  "interview_type": "<interview_type>",
                  "experience_level" :"<exp_level>",
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

    if job_role:
        prompt += f" The job role is {job_role}."
    if interview_type:
        prompt += f" The interview type is {interview_type}."
    if job_desc:
        prompt += f" Here is the job description: {job_desc}"
    if exp_level:
        prompt += f" The exprience level is {exp_level}"


    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt
    )
    if not response or not hasattr(response, "text"):
        return jsonify({"error": "Failed to get a valid response from Gemini API"}), 500

    answer = response.text

    return answer



if __name__ == '__main__':
    app.run(debug=True,port = 5000)



