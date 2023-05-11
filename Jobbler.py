import PySimpleGUI as sg
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

df = pd.read_csv('[Python] Data Set Project/Jobbler-Dataset-Project/Salary Data.csv')
sg.theme('DarkTeal9')
font = ("Arial", 20)

jobSet = ['Software Engineer', 'Data Analyst', 'Senior Manager', 'Sales Associate', 'Director', 'Marketing Analyst', 'Product Manager', 'Sales Manager', 'Marketing Coordinator', 'Senior Scientist', 'Software Developer', 'HR Manager', 'Financial Analyst', 'Project Manager', 'Customer Service Rep', 'Operations Manager', 'Marketing Manager', 'Senior Engineer', 'Data Entry Clerk', 'Sales Director', 'Business Analyst', 'VP of Operations', 'IT Support', 'Recruiter', 'Financial Manager', 'Social Media Specialist', 'Software Manager', 'Junior Developer', 'Senior Consultant', 'Product Designer', 'CEO', 'Accountant', 'Data Scientist', 'Marketing Specialist', 'Senior Manager', 'Technical Writer', 'HR Generalist', 'Project Engineer', 'Customer Success Rep', 'Sales Executive', 'UX Designer', 'Operations Director', 'Network Engineer', 'Administrative Assistant', 'Strategy Consultant', 'Copywriter', 'Account Manager', 'Director of Marketing', 'Senior Scientist', 'Help Desk Analyst', 'Customer Service Manager', 'Business Intelligence Analyst', 'Event Coordinator', 'VP of Finance', 'Graphic Designer', 'Sales Manager', 'UX Researcher', 'Senior Engineer', 'Social Media Manager', 'Product Manager', 'Director of Operations', 'Marketing Analyst', 'HR Manager', 'Senior Data Scientist', 'Junior Accountant', 'Digital Marketing Manager', 'IT Manager', 'Customer Service Representative', 'Business Development Manager', 'Senior Financial Analyst', 'Web Developer', 'Recruiter', 'Research Director', 'Technical Support Specialist', 'Creative Director', 'Project Manager', 'Operations Manager', 'Senior Software Engineer', 'Human Resources Director', 'Content Marketing Manager', 'Technical Recruiter', 'Data Analyst', 'Sales Representative', 'Chief Technology Officer', 'Junior Designer', 'Financial Advisor', 'Junior Account Manager', 'HR Generalist', 'Senior Project Manager', 'Marketing Coordinator', 'Principal Scientist', 'Sales Associate', 'Supply Chain Manager', 'Senior Marketing Manager', 'Business Analyst', 'Training Specialist', 'Research Scientist', 'Junior Software Developer', 'Public Relations Manager', 'Operations Analyst', 'Event Coordinator', 'Product Marketing Manager', 'Senior HR Manager', 'Junior Web Developer', 'Senior Project Coordinator', 'Chief Data Officer', 'Digital Content Producer', 'IT Support Specialist', 'Senior Marketing Analyst', 'Customer Success Manager', 'Senior Graphic Designer', 'Software Project Manager', 'Supply Chain Analyst', 'Senior Business Analyst', 'Junior Marketing Analyst', 'Senior Financial Analyst', 'Office Manager', 'Principal Engineer', 'Junior HR Generalist', 'Senior Product Manager', 'Sales Manager', 'Director of Marketing', 'Junior Operations Analyst', 'Customer Service Manager', 'Senior Scientist', 'Junior Accountant', 'Senior HR Generalist', 'Sales Operations Manager', 'Marketing Coordinator', 'Senior Software Developer', 'Director of Operations', 'Junior Web Designer', 'Senior Training Specialist', 'Senior Research Scientist', 'Junior Sales Representative', 'Administrative Assistant', 'Senior Project Manager', 'Junior Marketing Manager', 'Junior Data Analyst', 'Senior Product Marketing Manager', 'Junior Business Analyst', 'Senior Marketing Manager', 'Junior Software Developer', 'Senior Sales Manager', 'Junior Marketing Specialist', 'Senior Business Analyst', 'Senior Data Scientist', 'Junior Project Manager', 'Senior Accountant', 'Director of Sales', 'Junior Recruiter', 'Senior Business Development Manager', 'Senior Product Designer', 'Junior Customer Support Specialist', 'Senior Marketing Analyst', 'Senior IT Support Specialist', 'Junior Financial Analyst', 'Senior Operations Manager', 'Director of Human Resources', 'Junior Software Engineer', 'Senior Sales Representative', 'Director of Product Management', 'Junior Copywriter', 'Senior Marketing Coordinator', 'Senior Human Resources Manager', 'Junior Business Development Associate', 'Senior Account Manager', 'Senior Researcher', 'Junior HR Coordinator', 'Senior Software Engineer', 'Director of Finance', 'Junior Marketing Coordinator', 'NaN', 'Senior Project Manager', 'Junior Data Scientist', 'Senior Operations Analyst', 'Senior Marketing Manager', 'Junior Accountant', 'Senior Human Resources Coordinator', 'Director of Operations', 'Junior Sales Representative', 'Senior Business Analyst', 'Senior UX Designer', 'Junior Product Manager', 'Senior Marketing Specialist', 'Senior IT Project Manager', 'Senior Financial Analyst', 'Senior Quality Assurance Analyst', 'Director of Sales and Marketing', 'Junior Operations Analyst', 'Senior Account Executive', 'Director of Business Development', 'Junior Social Media Manager', 'Senior Product Manager', 'Senior Human Resources Specialist', 'Junior Business Analyst', 'Senior Marketing Coordinator', 'Senior Data Analyst', 'Junior Account Manager', 'Senior Software Developer', 'Director of Human Capital', 'Junior Advertising Coordinator', 'Senior Sales Manager', 'Junior UX Designer', 'Senior Accountant', 'Senior Marketing Director', 'Junior HR Generalist', 'Senior Operations Manager', 'Director of Finance', 'Junior Marketing Coordinator', 'Senior IT Consultant', 'Senior Product Designer', 'Junior Business Development Associate', 'Senior Marketing Analyst', 'Senior Software Engineer', 'Senior Financial Advisor', 'Senior Project Coordinator', 'Director of Operations', 'Junior Business Operations Analyst', 'Senior Sales Representative', 'Director of Marketing', 'Junior Social Media Specialist', 'Senior Product Development Manager', 'Senior Human Resources Manager', 'Junior Financial Analyst', 'Senior Marketing Manager', 'Senior Data Scientist', 'Junior Operations Manager', 'Senior Software Architect', 'Director of Human Resources', 'Junior Marketing Specialist', 'Senior Project Manager', 'Junior Research Scientist', 'Senior Operations Analyst', 'Senior Marketing Manager', 'Junior Sales Representative', 'Senior Financial Analyst', 'Senior Software Developer', 'Junior Operations Analyst', 'Senior Marketing Specialist', 'Senior HR Manager', 'Junior Business Analyst', 'Senior Product Manager', 'Senior Data Analyst', 'Junior Marketing Analyst', 'Senior Operations Manager', 'Director of Marketing', 'Junior Financial Analyst', 'Senior Project Coordinator', 'Director of Operations', 'Junior Marketing Coordinator', 'Senior IT Consultant', 'Senior Product Designer', 'Junior Business Development Associate', 'Senior Marketing Analyst', 'Senior Software Engineer', 'Senior Financial Advisor', 'Senior Project Coordinator', 'Director of Operations', 'Junior Business Operations Analyst', 'NaN', 'Senior Financial Manager', 'Senior Data Scientist', 'Junior Marketing Coordinator', 'Senior Operations Manager', 'Junior Sales Representative', 'Senior Marketing Specialist', 'Senior HR Specialist', 'Junior Operations Manager', 'Senior Marketing Coordinator', 'Senior Data Engineer', 'Junior Marketing Manager', 'Senior Financial Analyst', 'Director of Marketing', 'Junior Business Analyst', 'Senior Project Manager', 'Senior Data Analyst', 'Junior Financial Analyst', 'Senior Product Manager', 'Director of Operations', 'Junior Operations Analyst', 'Senior Project Coordinator', 'Director of Marketing', 'Junior Business Development Associate', 'Senior Financial Manager', 'Senior Product Designer', 'Junior Business Analyst', 'Senior Marketing Analyst', 'Senior Software Engineer', 'Junior Product Manager', 'Senior Business Analyst', 'Director of Operations', 'Junior Marketing Specialist', 'Senior Business Development Manager', 'Senior HR Manager', 'Junior Financial Analyst', 'Senior Marketing Manager', 'Senior Data Scientist', 'Junior Operations Coordinator', 'Senior Marketing Analyst', 'Director of HR', 'Junior Project Manager', 'Senior Operations Coordinator', 'Senior Data Engineer', 'Junior Marketing Manager', 'Senior Business Analyst', 'Director of Marketing', 'Junior Operations Analyst', 'Senior Project Manager', 'Director of Marketing', 'Junior Business Development Associate', 'Senior Financial Manager', 'Senior Product Designer', 'Junior Business Analyst', 'Senior Marketing Analyst', 'Senior Software Engineer', 'Senior Financial Advisor', 'Senior Marketing Specialist', 'Junior HR Coordinator', 'Senior Business Development Manager', 'Senior Marketing Manager', 'Junior Financial Advisor', 'Senior Project Manager', 'Director of Engineering', 'Junior Marketing Analyst', 'Senior Operations Manager', 'Senior Data Scientist', 'Junior Marketing Coordinator', 'Senior Business Analyst', 'Director of Marketing', 'Junior Business Development Associate', 'Senior Financial Analyst', 'Senior UX Designer', 'Junior Product Manager', 'Senior Marketing Manager', 'Director of Operations', 'Junior Project Manager', 'Senior Operations Coordinator', 'Senior Business Analyst', 'Junior Marketing Specialist', 'Senior Financial Manager', 'Director of Marketing', 'Junior Financial Analyst', 'Senior Product Manager', 'Senior Data Engineer', 'Junior Business Analyst', 'Senior Marketing Analyst', 'Director of Engineering', 'Junior Operations Manager', 'Senior Business Development Manager', 'Senior Data Scientist', 'Junior Marketing Coordinator', 'Senior Business Analyst', 'Director of Marketing', 'Junior Business Development Associate', 'Senior Financial Analyst', 'Senior UX Designer', 'Junior Product Manager', 'Senior Marketing Manager', 'Director of Operations', 'Junior Project Manager', 'Senior Operations Coordinator', 'Senior Business Analyst', 'Junior Marketing Specialist', 'Senior Financial Manager', 'Director of Marketing', 'Junior Financial Analyst', 'Senior Product Manager', 'Senior Data Engineer', 'Junior Business Analyst', 'Senior Marketing Analyst', 'Director of Operations', 'Junior Project Manager', 'Senior Operations Coordinator', 'Senior Business Analyst']

layout = [[sg.Text('Jobbler', size=(20, 1), key='-text-', font=font)],
          [sg.Text('An app developed by Luis Wettre\nto find the salary for tons of different jobs!')],
          [sg.Text('Jobb')],[sg.Combo(jobSet)],
          [sg.Button('Go!')]+[sg.Button('Cancel')]+[sg.Button('Graph')],
          [sg.Text('Salaries for the job')],
          [sg.Output(size=(50,10))] 
]

#Icon is from https://icons8.com/icon/eKxawYaWrcEZ/job
window = sg.Window('Jobbler', layout,size=(350,450), icon="[Python] Data Set Project/Jobbler-Dataset-Project/icons8_job_64__1__wgs_icon.ico")
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel    
        break

    elif event == 'Go!':
        result = df.loc[(df['Job Title'] == values[0])].sort_values(by='Salary', ascending=False).head(5)
        print(result[['Age','Job Title', 'Salary']])
   
    elif event == 'Graph':
        result = df.loc[(df['Job Title'] == values[0])].sort_values(by='Salary', ascending=False).head(5)
        result.plot(x='Age', y='Salary', kind='line', xlim=(result['Age'].min(), result['Age'].max()))      
        plt.show()  
        
window.close()