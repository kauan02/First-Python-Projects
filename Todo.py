import PySimpleGUI as sg

def create_new_task():
    sg.theme('darkamber')
    line = [
        [sg.Checkbox(''), sg.Input()]
    ]
    layout = [
        [sg.Frame("Tasks", layout=line, key="container")],  # Adicione uma vírgula aqui
        [sg.Button('New Task'), sg.Button('Reset')]  # Corrigido para 'Button' em maiúsculo
    ]
    
    return sg.Window('Todo list', layout=layout, finalize=True)

# Criação da janela
window = create_new_task()

# Criação das regras da janela
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'New Task':  # Corrigido para 'New Task' com "N" maiúsculo
        window.extend_layout(window["container"], [[sg.Checkbox(''), sg.Input('')]])
    elif event == 'Reset':
        window.close()
        window = create_new_task()

