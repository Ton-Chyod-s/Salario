from lib import calc,info
import PySimpleGUI as sg

selected_theme = 'Reddit'
sg.theme(selected_theme)

layout_login = [
        [sg.Text('Salário:\t'),sg.Stretch(),sg.Input(size=(6,1),key='salario'),sg.Btn('ok',size=(3,1))],
        [sg.Output(size=(25,6))],
        ]

window = sg.Window('Divisão', icon=' ',layout=layout_login, keep_on_top=True, finalize = True)

while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair': # if user closes window or clicks cancel
            break
        
        if event == 'ok':
            pass

window.close()


dicionario = info.despesas(Despesas=50,Investimento=30,Fundo_Emergencial=10,Pode_gastar=10)
calc.calculo(dicionario)