import PySimpleGUI as sg
import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.read_csv('[Python] Data Set Project/Jobbler-Dataset-Project/Salary Data.csv')
sg.theme('DarkTeal9')
font = ("Arial", 20)

ageList = [23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53]
genderList = ["Male","Female"]
educationList = ['''Bachelor's''','''PhD''','''Master's''']
experienceList = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

layout = [[sg.Text('Jobbler', size=(20, 1), key='-text-', font=font)],
          [sg.Text('An app developed by Luis Wettre\nto find the highest paying job for you!\n\nIf you dont want to enter a value in a sertain field leave it blank!')],
          [sg.Text('Age')],[sg.Combo(ageList)],[sg.Text('Gender')],[sg.Combo(genderList)],[sg.Text('Education')],[sg.Combo(educationList)],[sg.Text('Years of Experience')],[sg.Combo(experienceList)],
          [sg.Button('Go!')]+[sg.Button('Cancel')],
          [sg.Text('Best Paying Jobs for you!')],
          [sg.Output(size=(50,10))] 
]

window = sg.Window('Jobbler', layout,size=(500,600))    

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break


    inputDict = {
        "age":values[0],
        "gender":values[1],
        "edu":values[2],
        "exp":values[3],
    }
   
    result = df.loc[(df['Age'] == int(inputDict["age"])) & (df['Gender'] == inputDict["gender"]) & (df['Education Level'] == inputDict["edu"]) & (df['Years of Experience'] == inputDict["exp"])]
    result_sorted = result.sort_values(by='Salary', ascending=False).head(5)
    print(result_sorted[['Job Title', 'Salary']])


window.close()