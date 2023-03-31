import PySimpleGUI as sg


sg.theme('DarkTeal9')

layout = [[sg.Text('Jobber')],
          [sg.Text('Age')]+[sg.Text('Gender')]+[sg.Text("Country")],    
          [sg.InputText()]+[sg.InputText()]+[sg.InputText()],
          [sg.Button('Go!')],
          [sg.Button('Cancel')]
]

window = sg.Window('Jobber', layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        break
    ageInput = values[0]
    genderInput = values[1]
    countryInput = values[2]

window.close()
