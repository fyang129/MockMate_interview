import requests
import json


def test_question_generator(payload, test_case_desc):
    url = "http://127.0.0.1:5000/question_generator"
    headers = {"Content-Type": "application/json"}
    # payload = {
    #     "job_role": "Data Analyst",
    #     "interview_type": "Technical",
    #     "job_desc": "Responsible for data analysis, SQL queries, and reporting."
    # }

    print(f"\nRunning Test: {test_case_desc}")
    response = requests.post(url, data=json.dumps(payload), headers=headers)

    if response.status_code == 200:
        print("Success! Here are the generated questions:")
        print(response.text)
    else:
        print(f"Error: {response.status_code}")
        print(response.json())


if __name__ == "__main__":

    # senior
    test_question_generator({
        "job_role": "Senior Product Analyst",
        "interview_type": "Behavior",
        "job_desc": "",
        "exp_level": ""
    }, "senior")

    # junior
    test_question_generator({
        "job_role": "Product Analyst",
        "interview_type": "Behavior",
        "job_desc": "",
        "exp_level": ""
    }, "")

    # Senior but with exp lvl
    test_question_generator({
        "job_role": "Product Analyst",
        "interview_type": "Behavior",
        "job_desc": "",
        "exp_level": "senior level"
    }, "senior level")



    test_question_generator({
        "job_role": "Product Analyst Intern ",
        "interview_type": "HR Screening",
        "job_desc":

        '''You’ll be responsible for: 

Assisting with product development activities including creation of forecasts, budgets, strategies, opportunity assessments and business cases. 
Assisting with product delivery by working and consulting with internal & external stakeholders to ensure quality deliverables are produced in a timely manner.Gathering appropriate competitive knowledge by exploring global and domestic market trends and be expert in industry landscape. 
Identifying market opportunities for Interac. 
Collaborating with the product team and software engineers with various projects by helping keep track of development issues, communicating priorities and solve various problems as they arise 
Assisting with product training, including creation of material for internal or external audiences. 
Monitoring and track product adoption by assembling data from multiple sources (internal and external) and prepare summary reports. 
Participating in special projects and perform additional duties to help achieve departmental objectives. 
Developing a detailed understanding customer segments through the use data analytics. 
Supporting the creation and implementation of marketing plans in line with product strategy. 

You bring: 

Currently completing an undergraduate degree from a creditable Canadian institution with a focus on Business, Economics, Finances, Engineering or similar field 
You possess solid critical thinking, analytical and problem resolution skills to analyze trends and impacts, identify options and implications, and propose practical solutions. 
You have the ability to communicate the results of analyses in a clear and effective manner. 
You are self motivated, results oriented with a proven track record in the payments industry or a similarly regulated industry. 
You have strong planning and analytical skills 
You are comfortable with the fast-paced dynamic atmosphere of a technical organization. 
You possess the ability to work collaboratively with others to achieve a common goal. 
Excellent communication skills (oral and written). 
Understanding and familiarity with tools like Figma, Jira or Tableau 
Ability to eliminate obstacles through creative and adaptive approaches. 
Although not required, you have some familiarity or previous experience with the following: 
Proven experience working directly with technology teams to implement systemic improvements 
Technical fluency; comfort understanding and discussing technology concepts, schedule tradeoffs and new opportunities with technical team members. 
Previous experience or knowledge in payments – or at minimum interest 
'''

    }, "Valid Input - Product Analyst Intern")

    # Test Case 2: No job role provided - Risk Analyst
    test_question_generator({
        "job_role": "",
        "interview_type": "Technical",
        "job_desc":
        '''
Risk Analyst



About Toyota Financial Services

Toyota Financial Services (TFS) provides retail, leasing and wholesale financial services to Toyota and Lexus dealerships and customers across Canada. TFS is a member of Toyota Financial Services Corporation (TFSC), a wholly owned subsidiary of Toyota Motor Corporation in Japan. The Canadian headquarters of TFS are in Markham, Ontario.



What Sets Us Apart?

At Toyota Financial Services (TFS), you will help create best in class customer experiences in an innovative, collaborative and team focused environment. TFS is an important part of the Toyota family, an award-winning global company, recognized worldwide for our technological leadership and superior standards of quality, continuous improvement and environmental responsibility.



TFS currently has an exciting permanent opportunity as a Risk Analyst, reporting to the Manager, Risk Management. This role resides in our Markham Office.



What You Will Be Doing:

Produce proposals for the establishment of lease end residual values based on vehicle pricing and re- sale value data. Duties include data gathering and formatting as well as analysis and interpretation.
Support the company’s retail pricing decisions by preparing lending rate proposals based on risk-adjusted profitability analyses.
Provide analytical support to the development, implementation and maintenance of decision models such as scorecards and automated credit adjudication as well as delinquency and credit loss forecasting models.
Utilize the company’s statistical models to prepare lease-end loss forecasts used to determine residual value loss reserve requirements; contribute to the development and refinement of these models.
Produce various scheduled and ad hoc reports using database queries and spreadsheet reporting tools.
Assist with the creation and modification of residual value and credit risk management policies and procedures, as well as process maps used to ensure risk control.
Maintain and develop various databases, technical models and reports required to gather and analyze data.


What You Will Bring:

A bachelor's degree with a quantitative focus in an applied context, such as applied math, statistics, economics, engineering or finance.
FRM, PRM or CFA designation is preferred.
2 to 4 years of progressive experience in an analyst role, preferably in financial risk management.
Demonstrated experience in applying programming languages such as SQL, Python and SAS to the extraction, transformation and analysis of data.
Knowledge and understanding of statistical modeling and forecasting techniques such as regression analysis and machine learning algorithms.
Understanding of the fundamental concepts of financial accounting, including financial statement analysis.
Knowledge of the lending lifecycle, including credit analysis, underwriting, portfolio management, collections and asset remarketing.
Strong interpersonal, verbal and written communication skills.
Automotive lending experience is preferred but not required.
An interest in automobiles is preferred.
'''
    }, "Missing Job Role")

    # Test Case 3: Valid Input - Risk Analyst
    test_question_generator({
        "job_role": "Risk Analyst",
        "interview_type": "Technical",
        "job_desc": '''

    Risk Analyst



    About Toyota Financial Services

    Toyota Financial Services (TFS) provides retail, leasing and wholesale financial services to Toyota and Lexus dealerships and customers across Canada. TFS is a member of Toyota Financial Services Corporation (TFSC), a wholly owned subsidiary of Toyota Motor Corporation in Japan. The Canadian headquarters of TFS are in Markham, Ontario.



    What Sets Us Apart?

    At Toyota Financial Services (TFS), you will help create best in class customer experiences in an innovative, collaborative and team focused environment. TFS is an important part of the Toyota family, an award-winning global company, recognized worldwide for our technological leadership and superior standards of quality, continuous improvement and environmental responsibility.



    TFS currently has an exciting permanent opportunity as a Risk Analyst, reporting to the Manager, Risk Management. This role resides in our Markham Office.



    What You Will Be Doing:

    Produce proposals for the establishment of lease end residual values based on vehicle pricing and re- sale value data. Duties include data gathering and formatting as well as analysis and interpretation.
    Support the company’s retail pricing decisions by preparing lending rate proposals based on risk-adjusted profitability analyses.
    Provide analytical support to the development, implementation and maintenance of decision models such as scorecards and automated credit adjudication as well as delinquency and credit loss forecasting models.
    Utilize the company’s statistical models to prepare lease-end loss forecasts used to determine residual value loss reserve requirements; contribute to the development and refinement of these models.
    Produce various scheduled and ad hoc reports using database queries and spreadsheet reporting tools.
    Assist with the creation and modification of residual value and credit risk management policies and procedures, as well as process maps used to ensure risk control.
    Maintain and develop various databases, technical models and reports required to gather and analyze data.


    What You Will Bring:

    A bachelor's degree with a quantitative focus in an applied context, such as applied math, statistics, economics, engineering or finance.
    FRM, PRM or CFA designation is preferred.
    2 to 4 years of progressive experience in an analyst role, preferably in financial risk management.
    Demonstrated experience in applying programming languages such as SQL, Python and SAS to the extraction, transformation and analysis of data.
    Knowledge and understanding of statistical modeling and forecasting techniques such as regression analysis and machine learning algorithms.
    Understanding of the fundamental concepts of financial accounting, including financial statement analysis.
    Knowledge of the lending lifecycle, including credit analysis, underwriting, portfolio management, collections and asset remarketing.
    Strong interpersonal, verbal and written communication skills.
    Automotive lending experience is preferred but not required.
    An interest in automobiles is preferred.

            '''
    }, "Valid - Risk")

    # Test Case 4: No job description provided
    test_question_generator({
        "job_role": "Product Manager",
        "interview_type": "Behavior",
        "job_desc": ""
    }, "Missing Job Description")
    
    # Test Case 5: Both job role and job description missing
    test_question_generator({
        "job_role": "",
        "interview_type": "Technical",
        "job_desc": ""
    }, "Missing Both Job Role and Job Description")

