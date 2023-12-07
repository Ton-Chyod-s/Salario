def calculo(arg_txt,salario):
    for lin in arg_txt:
        pct = arg_txt[lin]/100
        res = salario * pct
        print(f'{lin} : R${res}')