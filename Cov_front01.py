# Biblioteca de front-end 01 com funções para exibição na tela dos menus aos usuários

# Importação de bibliotecas necessárias
from Cov_back00_v10 import erro_menu_user as errmnuser
import random as rd

# Função para imprimir saudações e realizar login do usuário (com parâmetros "saud, autuser, cidadaos" e retorno "opc")
def logar(saud,autuser,cidadaos):
	print("\n\t\t--- TELA INICIAL ---")
	# Chamada da função randint da biblioteca random
	intx=rd.randint(0,len(saud)-1)
	# Impressão de saudação aleatória 
	print("\n",saud[intx])
	# Tela de login dos usuários
	inic=-1
	while inic != "0":
		inic=input("\nDigite: [0]Sair ou [1]Entrar\n")
		if inic=="1":
			# Validação de usuário especial (administrador ou gestor) e cidadãos
			log=input("\nDigite o login de usuário especial ou nome: ")
			tkn=input("\nDigite a senha de usuário especial ou CPF: ")
			if (log,tkn) in [(autuser[0][k],autuser[1][k]) for k in autuser[0].keys() if autuser[0][k][:3]=='ADM'] or len(autuser[0])==0:
				print("\n\t\t####### MENU DO ADMINISTRADOR #######")
				# Exibição das 4 opções do menu de administrador
				ent=f"\nDigite a opção desejada: [0]Sair, [1]Cadastrar, [2]Listar, [3]Questionário, [4]Relatórios.\n"
				opc=errmnuser(ent,input(ent),['0','1','2','3','4'])
			elif (log,tkn) in [(autuser[0][k],autuser[1][k]) for k in autuser[0].keys() if autuser[0][k][:3]=='GER']: 
				print("\n\t\t####### MENU DO GESTOR #######")
				# Exibição das 2 opções do menu de gestor
				ent=f"\nDigite a opção desejada: [0]Sair, [4]Relatórios.\n"
				opc=errmnuser(ent,input(ent),['0','4'])
			elif (log,tkn) in [(cidadaos[0][k],k) for k in cidadaos[0].keys()]:
				print("\n\t\t####### MENU DO CIDADÃO #######")
				# Exibição das 2 opções do menu de cidadão
				ent=f"\nDigite a opção desejada: [0]Sair, [3]Questionário.\n"
				opc=errmnuser(ent,input(ent),['0','3'])
			else:
				print("\nInformações de acesso inconsistentes!")
				opc=-1
		else:
			opc=-1
		return opc
	return "0"

# Função para exibir o menu dos cadastros ao usuário (sem parâmetro e com retorno "opc")
def menu_cadastros():
	print("\n\t\t####### MENU DE CADASTROS #######")
	# Exibição das 4 opções do menu de cadastros
	opc=input("\nDigite a opção desejada: [1]Cadastrar Cidadãos, [2]Cadastrar Perguntas dos Sintomas, [3]Cadastrar Cumprimentos, [4]Cadastrar Usuários, [5]Sair.\n")
	return opc

# Função para exibir o menu dos tipos de cadastros dos cidadãos ao usuário (sem parâmetro e com retorno "opc")
def menu_cidadaos():
	print("\n\t\t####### MENU DE ENTRADA DOS CIDADÃOS #######")
	# Exibição das 3 opções do menu de cadastros
	opc=input("\nDigite a opção desejada: [1]Importação de Arquivo, [2]Cadastro Manual, [3]Sair.\n")
	return opc

# Função para exibir o menu das listas ao usuário (sem parâmetro e com retorno "opc")
def menu_listas():
	print("\n\t\t####### MENU DE LISTAS #######")
	# Exibição das 4 opções do menu de listas
	opc=input("\nDigite a opção desejada: [1]Listar Cidadãos Cadastrados, [2]Listar Perguntas dos Sintomas, [3]Listar Cumprimentos, [4]Listar Usuários, [5]Sair.\n")
	return opc

# Função para exibir o menu dos relatórios ao usuário (sem parâmetro e com retorno "opc")
def menu_relatorios():
	print("\n\t\t####### MENU DE RELATÓRIOS #######")
	# Exibição das 3 opções do menu de listas
	opc=input("\nDigite a opção desejada: [1]Consolidados de Cidadãos, [2]Consolidados de Sintomas, [3]Sair.\n")
	return opc