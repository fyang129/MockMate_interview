# Question Generator

#  Interview Question Generator API

##  Base URL
The API is hosted on **Render**, and all requests should be made to:
```
https://question-generator-mockmate.onrender.com
```

## ** Generate Interview Questions **
### 🔹 Endpoint
```bash
POST /question_generator
```
#### Description
Generates **10** unique job interview questions based on the provided job role, interview type, experience level, and job description.

#### Request Body (JSON)

| Parameter      | Type   | Required | Description |
|---------------|--------|----------|-------------|
| `job_role`    | string | Yes   | Job title (e.g., \"Software Engineer\") |
| `interview_type` | string |  No  | Type of interview (e.g., \"Technical\") |
| `exp_level`   | string |  No  | Experience level (e.g., \"Senior\") |
| `job_desc`    | string |  No  | Additional job details |


##  Example Request 
```bash

curl -X POST https://your-app-name.onrender.com/question_generator \
     -H "Content-Type: application/json" \
     -d '{
          "job_role": "Data Scientist",
          "interview_type": "Technical",
          "exp_level": "Mid-Level",
          "job_desc": " "
         }'
```

## Example Response 

```json
{
    "job_role": "Data Scientist",
    "questions": [
        "Can you explain the concept of overfitting in machine learning?",
        "How would you optimize a slow SQL query?",
        "What are some common data cleaning techniques in Python?",
        "Explain the difference between supervised and unsupervised learning.",
        "What metrics would you use to evaluate a machine learning model?",
        "How do you handle imbalanced datasets?",
        "Can you explain the bias-variance tradeoff?",
        "What is the importance of feature engineering?",
        "How do you deploy a machine learning model?",
        "Describe a challenging data analysis problem you've solved."
    ]
}
```

### Possible Error Responses
| Status Code	| Message     |
|---------------|--------|
| 400 Bad Request    | {"error": "Please enter your job role or description"} | 
| 500 Internal Server Error | 	{"error": "Failed to get a valid response from Gemini API"}| 


#### Call API in JavaScript (Frontend)
```javascript

async function fetchInterviewQuestions() {
    const response = await fetch("https://your-app-name.onrender.com/question_generator", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            job_role: "Software Engineer",
            interview_type: "Technical",
            exp_level: "Senior",
            job_desc: "Working with cloud services and microservices."
        })
    });

    const data = await response.json();
    console.log("Generated Questions:", data.questions);
}

// Call the function to fetch questions
fetchInterviewQuestions();

```
