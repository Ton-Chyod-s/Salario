from lib import calc,info,BD, tempo
from asyncio import run
import os
import PySimpleGUI as sg

dicionario = info.despesas(Despesas=60,Investimento=30,Fundo_Emergencial=5,Pode_gastar=5)

selected_theme = 'Reddit'
sg.theme(selected_theme)

layout = [
        [sg.Text('Salário:\t'),sg.Stretch(),sg.Input(size=(6,1),key='salario'),sg.Btn('ok',size=(3,1))],
        [sg.Output(size=(35,6), key = '_output_')],
        [sg.Button('%',size=(5,1)),sg.Button('BD',size=(5,1))],
        ]

window = sg.Window('Divisão', icon=' ',layout=layout, keep_on_top=True, finalize = True)

while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED or event == 'Sair': 
            break
        
        if event == 'ok':
            caminho_bd = os.path.abspath('salario.db')
            window.FindElement('_output_').Update('')
            dict_salario = calc.calculo(dicionario,int(values['salario']))
            print(f'Despesas: {dict_salario['Despesas']}\nInvestimentos: {dict_salario['Investimento']}\nFundo de Emergencia: {dict_salario['Fundo_Emergencial']}\nPode gastar a toa fih: {dict_salario['Pode_gastar']}')
            
            if os.path.exists(caminho_bd):
                run(BD.inserir_dados(values['salario'],tempo.data(),dict_salario['Despesas'],dict_salario['Investimento'],dict_salario['Fundo_Emergencial'],dict_salario['Pode_gastar']))
            else:
                run(BD.create_database())
                run(BD.inserir_dados(values['salario'],tempo.data(),dict_salario['Despesas'],dict_salario['Investimento'],dict_salario['Fundo_Emergencial'],dict_salario['Pode_gastar']))

        if event == 'BD':
            caminho_bd = os.path.abspath('salario.db')
            if os.path.exists(caminho_bd):
                print('Você ja tem um Banco de Dados!!')
            else:   
                run(BD.create_database())

        if event == '%':
            layout_porc = [
                    [sg.Text('Despesas:\t'),sg.Stretch(),sg.Input(size=(6,1),key='desp')],
                    [sg.Text('Investimento:\t'),sg.Stretch(),sg.Input(size=(6,1),key='inv')],
                    [sg.Text('Fundo Emergencial:\t'),sg.Stretch(),sg.Input(size=(6,1),key='fe')],
                    [sg.Text('Pode gastar:\t'),sg.Stretch(),sg.Input(size=(6,1),key='pg')],
                    [sg.Button('confimar',size=(8,1))],
                    ]

            window_porc = sg.Window('porcentagem', icon=' ',layout=layout_porc, keep_on_top=True, finalize = True)

            while True:
                event,values = window_porc.read()
                if event == sg.WIN_CLOSED or event == 'Sair': 
                    break

                if event == 'confimar':
                    despesas = float(values['desp'])
                    investimento = float(values['inv'])
                    fundo_emergencial = float(values['fe'])
                    pode_gastar = float(values['pg'])
                    soma = despesas + investimento + fundo_emergencial + pode_gastar

                    if soma > 100 or soma < 100:
                        print('Soma dos valores incorreta!!\nEra esperado 100%')
                    else:
                        info.despesas(Despesas=float(values['desp']),Investimento=float(values['inv']),Fundo_Emergencial=float(values['fe']),Pode_gastar=float(values['pg']))
                    
            window_porc.close()
window.close()



