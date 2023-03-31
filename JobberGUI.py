import PySimpleGUI as sg
import pandas as pd

df = pd.read_csv('[Python] Data Set Project/Jobbler-Dataset-Project/train.csv')

sg.theme('DarkTeal9')
font = ("Arial", 20)
layout = [[sg.Text('Jobbler', size=(20, 1), key='-text-', font=font)],
          [sg.Text('An app developed by Luis Wettre\nto find the highest paying job for you!')],
          [sg.Text('Age')],[sg.InputText()],[sg.Text('Gender')],[sg.InputText()],[sg.Text("Country")],[sg.InputText()],
          [sg.Button('Go!')]+[sg.Button('Cancel')]
          
]

window = sg.Window('Jobber', layout,size=(300,300))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    ageInput = values[0]
    genderInput = values[1]
    countryInput = values[2]

    age = (df.loc[df['age'] == int(ageInput)])
    print(age.head(5))

    gender = (df.loc[df['gender'] == genderInput])
    print(gender.head(5))

    country = (df.loc[df['native-country'] == countryInput])
    print(country.head(5))
   

'''
while True:
    if value in collumn[0] == ageInput and value in collumn[9] == genderInput and value in collumn[13] == countryInput:
        print()

'''

window.close()
