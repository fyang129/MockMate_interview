import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import requests
from dotenv import load_dotenv
from google import genai
from google.genai import types

app = Flask(__name__)
CORS(app)

load_dotenv()

GEMINI_API_KEY= os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

# genai.configure(api_key=GEMINI_API_KEY)
# model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# job_role = data.get("job_role", "").strip()
# interview_type = data.get("interview_type", "").strip()
# job_desc = data.get("job_desc", "").strip()

@app.route('/questions', methods=['POST'])
def gen_q(): # generate questions from request
    pass



prompt = ("""
           "Please generate 10 job interview questions base on the information below."
           "Only provide the questions.
           """)

job_role = 'Project Manager'
interview_type = 'HR Screening'
job_desc = ''

if not job_role and not job_desc:
    print({"error": "Please enter your job role or description"})

# if job_role:
prompt += f" The job role is {job_role}."
# if interview_type:
prompt += f" The interview type is {interview_type}."
# if job_desc:
prompt += f" Here is the job description: {job_desc}"

print(prompt)

response = client.models.generate_content(
    model = "gemini-2.0-flash",
    contents = prompt
)

answer = response.text

print(answer)

print('end')

