def calculo(arg_txt,salario):
    dicionario = {}
    for lin in arg_txt:
        pct = arg_txt[lin]/100
        res = salario * pct
        dicionario[lin] = f'R${round(res,2)}'
    return dicionario