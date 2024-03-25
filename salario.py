from lib import calc,info,BD
from asyncio import run
import os
import PySimpleGUI as sg

dicionario = info.despesas(Despesas=60,Investimento=30,Fundo_Emergencial=5,Pode_gastar=5)

selected_theme = 'Reddit'
sg.theme(selected_theme)

layout = [
        [sg.Text('Salário:\t'),sg.Stretch(),sg.Input(size=(6,1),key='salario'),sg.Btn('ok',size=(3,1))],
        [sg.Output(size=(25,6), key = '_output_')],
        [sg.Button('%',size=(5,1)),sg.Button('BD',size=(5,1))],
        ]

window = sg.Window('Divisão', icon=' ',layout=layout, keep_on_top=True, finalize = True)

while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair': 
            break
        
        if event == 'ok':
            window.FindElement('_output_').Update('')
            calc.calculo(dicionario,int(values['salario']))
            run(BD.salario(values['salario']))

        if event == 'BD':
            caminho_bd = os.path.abspath('salario.db')
            if os.path.exists(caminho_bd):
                pass
            else:   
                run(BD.create_database())

        if event == '%':
            layout_porc = [
                    [sg.Text('Despesas:\t'),sg.Stretch(),sg.Input(size=(6,1),key='desp')],
                    [sg.Text('Investimento:\t'),sg.Stretch(),sg.Input(size=(6,1),key='inv')],
                    [sg.Text('Fundo_Emergencial:\t'),sg.Stretch(),sg.Input(size=(6,1),key='fe')],
                    [sg.Text('Pode_gastar:\t'),sg.Stretch(),sg.Input(size=(6,1),key='pg')],
                    [sg.Button('confimar',size=(8,1))],
                    ]

            window_porc = sg.Window('porcentagem', icon=' ',layout=layout_porc, keep_on_top=True, finalize = True)

            while True:
                event,values = window_porc.read()
                if event == sg.WIN_CLOSED or event == 'Sair': 
                    break

                if event == 'confimar':
                    info.despesas(Despesas=int(values['desp']),Investimento=int(values['inv']),Fundo_Emergencial=int(values['fe']),Pode_gastar=int(values['pg']))
                    
            window_porc.close()
window.close()



