def calculo(arg_txt):
    salario = int(input('Digite seu salário: R$'))
    for lin in arg_txt:
        pct = arg_txt[lin]/100
        res = salario * pct
        print(f'{lin} : R${res}')