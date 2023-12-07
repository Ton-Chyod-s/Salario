dicionario = {}
def despesas(**kwargs):
    """-> Monta um dicionario com argumentos/valor passado.
    :param **kwargs: argumentos e numero correspondete ao que se pede.
    :return: retorna um dicionario."""
    for valor, num in kwargs.items():
        dicionario[valor] = num
    return dicionario


def mudar_conteudo_valor():
	"""-> Modifica um dicionario.
    :numero pede ao usuario a confirmação/alteração de valores.
    :return: retorna um dicionario modificado."""
	dicionario = despesas().copy()
	for num, valor in dicionario.items():
		numero = int(input(f'Digite um valor para {num} o atual é {valor}: '))
		dicionario[num] = numero
	return print(dicionario)
		

if __name__ == '__main__':
	print(despesas(Despesas=50,Investimento=30,Fundo_Emergencial=10,Pode_gastar=10))
	mudar_conteudo_valor()