import PySimpleGUI as sg
import pandas as pd

df = pd.read_csv('[Python] Data Set Project/Jobbler-Dataset-Project/train.csv')

sg.theme('DarkTeal9')
font = ("Arial", 20)
layout = [[sg.Text('Jobbler', size=(20, 1), key='-text-', font=font)],
          [sg.Text('An app developed by Luis Wettre\nto find the highest paying job for you!')],
          [sg.Text('Age')],[sg.InputText()],[sg.Text('Gender')],[sg.InputText()],[sg.Text("Country")],[sg.InputText()],
          [sg.Button('Go!')]+[sg.Button('Cancel')],
          [sg.Text('Best Paying Jobs for you!')],
          [sg.Output(size=(50,10))]
          
]

window = sg.Window('Jobbler', layout,size=(300,500))

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    ageInput = values[0]
    genderInput = values[1]
    countryInput = values[2]

    result = df.loc[(df['age'] == int(ageInput)) & (df['gender'] == genderInput) & (df['native-country'] == countryInput)]
    result_sorted = result.sort_values(by='capital-gain', ascending=False).head(5)
    print(result_sorted[['occupation', 'capital-gain']])


window.close()