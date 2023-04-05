import PySimpleGUI as sg
import pandas as pd
import matplotlib as plt
import numpy as np

df = pd.read_csv('[Python] Data Set Project/Jobbler-Dataset-Project/train.csv')
sg.theme('DarkTeal9')
font = ("Arial", 20)
layout = [[sg.Text('Jobbler', size=(20, 1), key='-text-', font=font)],
          [sg.Text('An app developed by Luis Wettre\nto find the highest paying job for you!\n\nIf you dont want to enter a value in a sertain field leave it blank!')],
          [sg.Text('Age')],[sg.InputText()],[sg.Text('Gender')],[sg.Combo(["Male","Female"])],[sg.Text("Native-Country")],[sg.Combo(['United-States'])],[sg.Text("Race")],[sg.Combo(["Black","White","Asian"])],[sg.Text("Hours-Per-Week")],[sg.Combo([25,30,35,40,45,50,55,60,65,70,75,80,85,90])],
          [sg.Text('Occupation')],[sg.Combo(["Exec-managerial","Other-service","Transport-moving"])],[sg.Text('Marital Status')],[sg.Combo(["Maried"])],
          [sg.Button('Go!')]+[sg.Button('Cancel')],
          [sg.Text('Best Paying Jobs for you!')],
          [sg.Output(size=(50,10))]
]

window = sg.Window('Jobbler', layout,size=(700,700))    

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    ageInput = values[0]
    genderInput = values[1]
    countryInput = values[2]
    # Add search for occupation, marital status

    if not ageInput:
        result = df.loc[(df['gender'] == genderInput) & (df['native-country'] == countryInput)]
        result_sorted = result.sort_values(by='capital-gain', ascending=False).head(5)
        print(result_sorted[['occupation', 'capital-gain']])

    else:
        result = df.loc[(df['age'] == int(ageInput)) & (df['gender'] == genderInput) & (df['native-country'] == countryInput)]
        result_sorted = result.sort_values(by='capital-gain', ascending=False).head(5)
        print(result_sorted[['occupation', 'capital-gain']])

def CheckForInputs():
    while True:
        if not ageInput:
            continue
        if not genderInput:
            continue
        if not countryInput:
            continue

window.close()