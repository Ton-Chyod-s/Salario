def calculo(arg_txt,nome):
    salario = int(input(f'Digite seu salário: R${nome}'))
    for lin in arg_txt:
        pct = arg_txt[lin]/100
        res = salario * pct
        print(f'{lin} : R${res}')