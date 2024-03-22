from lib import calc,info
import PySimpleGUI as sg
dicionario = info.despesas(Despesas=60,Investimento=30,Fundo_Emergencial=5,Pode_gastar=5)

selected_theme = 'Reddit'
sg.theme(selected_theme)

layout_login = [
        [sg.Text('Salário:\t'),sg.Stretch(),sg.Input(size=(6,1),key='salario'),sg.Btn('ok',size=(3,1))],
        [sg.Output(size=(25,6), key = '_output_')],
        ]

window = sg.Window('Divisão', icon=' ',layout=layout_login, keep_on_top=True, finalize = True)

while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair': 
            break
        
        if event == 'ok':
            window.FindElement('_output_').Update('')
            calc.calculo(dicionario,int(values['salario']))

window.close()



