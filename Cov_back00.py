# Biblioteca de back-end 00 com funções para tratamento de erros e operações auxiliares

# Função para informar o usuário sobre escolha errada nos menus principais: 5 opções (com parâmetro "opc" e retorno "res_opc")
def erro_menu_princ(opc):
    # Previsão de erro para opções digitadas fora das 5 possíveis no menu principal
	if(opc!="1" and opc!="2" and opc!="3" and opc!="4" and opc!="5"):
		res_opc = "\n" + "Opção inválida!"
		print("\nOpção inválida!")
	# Retorno como resposta de uma opção possível no menu principal	
	else:
		res_opc = opc
	return res_opc

# Função para informar o usuário sobre escolha errada nos menus secundários: 4 opções (com parâmetro "opc" e retorno "res_opc")
def erro_menu_secund(opc):
        # Previsão de erro para opções digitadas fora das 4 possíveis nos menus secundários
	if(opc!="1" and opc!="2" and opc!="3" and opc!="4"):
		res_opc = "\n" + "Opção inválida!"
		print("\nOpção inválida!")
	# Retorno como resposta de uma opção possível nos menus secundários	
	else:
		res_opc = opc
	return res_opc

# Função para informar o usuário sobre escolha errada nos menus terciários: 3 opções (com parâmetro "opc" e retorno "res_opc")
def erro_menu_terci(opc):
    # Previsão de erro para opções digitadas fora das 3 possíveis nos menus terciários
	if(opc!="1" and opc!="2" and opc!="3"):
		res_opc = "\n" + "Opção inválida!"
		print("\nOpção inválida!")
	# Retorno como resposta de uma opção possível nos menus terciários	
	else:
		res_opc = opc
	return res_opc

# Função para retornar apenas opções válidas nos menus de usuários (com parâmetros "ent,opc,lst" e retorno "opc")
def erro_menu_user(ent,opc,lst):
    # Verificação de erros para opções digitadas fora das listadas
	while opc not in lst:
		print("\nOpção inválida!")
		opc=input(ent)
	return opc

# Função para validar entradas de textos sem caracteres especiais (com parâmetros "texto, cham" e retorno "texto_norm")
def valid_tex(texto,cham):
	if 'CPF' in cham.split():
		texto_aux=texto.replace(".","")
		while not texto.isnumeric() or texto_aux != texto or len(texto) != 11 or sum(int(i) for i in texto) not in {11*i for i in range(1,10)} or texto == "":
			print(f"\nO CPF '{texto}' é inválido!")
			texto=input(cham)
			texto_aux=texto.replace(".","")
		texto_norm=str(texto)
	elif 'nome' in cham.split():
		texto_aux=texto+"."
		while texto_aux != texto:
			for char in ".,;:!?*$%@+=()[]{}<>\/|_0123456789":
				texto_aux = texto_aux.replace(char,"")
			if texto_aux != texto or texto_aux.isnumeric() or texto_aux == "":
				print(f"\nO nome '{texto}' é inválido!")
				texto=input(cham)
				texto_aux=texto+"."
		texto_norm=str(texto)
	else:
		texto_aux=texto+"."
		while texto_aux != texto:
			for char in ".,;:!?*$%@+=()[]{}<>\/|_":
				texto_aux = texto_aux.replace(char,"")
			if texto_aux != texto or texto_aux.isnumeric() or texto_aux == "":
				print(f"\nO texto '{texto}' é inválido!")
				texto=input(cham)
				texto_aux=texto+"."
		texto_norm=str(texto)
	return texto_norm

# Função para validar entradas de números inteiros (com parâmetros "num, cham" e retorno "num_nat")
def valid_num(num,cham):
	if 'idade' in cham.split():
		num_aux=num.replace(".","")
		while not num.isnumeric() or num_aux!=num or num_aux == "" or num_aux=="0":
			print(f"\nA idade '{num}' anos é inválida!")
			num=input(cham)
			num_aux=num.replace(".","")
		num_nat=str(num)
	elif 'grupo' in cham.split():
		num_aux=num.replace(".","")
		while not num.isnumeric() or num_aux!=num or num_aux == "" or num_aux=="0":
			print(f"\nA quantidade '{num}' é inválida!")
			num=input(cham)
			num_aux=num.replace(".","")
		num_nat=str(num)
	else:
		num_aux=num.replace(".","")
		while not num.isnumeric() or num_aux!=num:
			print(f"\nO número '{num}' é inválido!")
			num=input(cham)
			num_aux=num.replace(".","")
		num_nat=str(num)
	return num_nat