# Biblioteca de back-end 01 com funções para cadastros

from Cov_back00_v10 import valid_num as valn, valid_tex as valt
import random as rd

# Função para cadastrar saudações e despedidas (com parâmetro e retorno "cump")
def cadastrar_cumprimentos(cump):
	print("\n\t\t--- CADASTRO DE SAUDAÇÕES ---")        
    # Impressão das saudações pré-cadastradas
	for i in cump[0]:
		print("\n",i)
    # Controle para evitar quantidade de saudações não numérica ou decimal
	ent="\nIndique o número de saudações que deseja cadastrar além das predefinidas no sistema : "        
	qte=valn(input(ent),ent)
    # Definição de uma quantidade válida de saudações como um número inteiro
	qte=int(qte)
    # Controle do cadastro de novas saudações        
	if qte>0:
		for j in range(qte):
			ent=input("\n\nDigite uma nova saudação: ")
			cump[0].append(ent)
    # Controle para pular o caso em que não se deseja cadastrar saudações                
	else:
		pass
	print("\n\t\t--- CADASTRO DE DESPEDIDAS ---")
    # Impressão das despedidas pré-cadastradas
	for i in cump[1]:
		print("\n",i)
    # Controle para evitar quantidade de despedidas não numérica ou decimal
	ent="\nIndique o número de despedidas que deseja cadastrar além das predefinidas no sistema : "        
	qte=valn(input(ent),ent)
    # Definição de uma quantidade válida de despedidas como um número inteiro        
	qte=int(qte)
    # Controle do cadastro de novas despedidas
	if qte>0:
		for j in range(qte):
			ent=input("\n\nDigite uma nova despedida: ")
			cump[1].append(ent)
    # Controle para pular o caso em que não se deseja cadastrar despedidas
	else:
		pass
	return cump

# Função para importar e tratar arquivo com dados dos cidadãos (com parâmetros "cid, num" e retorno "cid")
def importar_arquivo(cid):
	print("\n\t\t--- CADASTRO AUTOMÁTICO DE CIDADÃOS ---")
	# Leitura dos dados no padrão UTF-8 
	arq = open("Base_Cidadaos.txt",mode="r",encoding="utf-8").readlines()
	# Inicialização de lista para armazenar os dados dos cidadãos
	listr = []
	# Laço para percorrer cada linha do arquivo
	for lin in arq:
		# Separação de cada registro em CPF, nome, idade, sexo
		l = lin.split(',')
		# Coleta dos dados cadastrais do cidadão
		listr.append(l)
	#arq.close()
	# Testes de validação das entradas do arquivo e preenchimento dos dados dos cidadãos
	for ind, rg in enumerate(listr):
		# Validação do CPF
		ent=f"\nEntre com o documento correto na linha {ind+1}: "
		cpf=valn(rg[0],ent)
		# Validação do nome
		ent=f"\nEntre com o nome correto na linha {ind+1}: "
		nome=valt(rg[1],ent)
		# Validação da idade
		ent=f"\nEntre com a idade correta na linha {ind+1}: "	
		idade=valn(rg[2],ent)
		# Validação do gênero
		sexo=rg[3].replace("\n","")
		while sexo not in {'M','F','X'}:
			print(f"\nA informação de gênero '{sexo}' é inválida!")
			sexo=input(f"\nDigite na linha {ind+1} o gênero: [M]Masculino ou [F]Feminino ou [X]LGBTQIA+ ")
			sexo=sexo.upper()
		# Atualização dos registros cadastrais dos cidadãos
		cid[0].update({cpf:nome})
		cid[1].update({cpf:idade})
		cid[2].update({cpf:sexo})
	return cid

# Função para realizar cadastro manual dos cidadãos (com parâmetros "cid, num" e retorno "cid")
def cadastrar_cidadaos(cid,num):
	print("\n\t\t--- CADASTRO MANUAL DE CIDADÃOS ---")
    # Controle para evitar quantidade de cidadãos não numérica, nula ou decimal
	ent="\nIndique o total de cidadãos a adicionar ao grupo de respondentes : "
	tot=valn(input(ent),ent)
	# Definição de uma quantidade válida de cidadãos como número inteiro	
	tot=int(tot)
	# Controle do fluxo de cadastro dos cidadãos
	for j in range(tot):
        # Ordem de cada novo cidadão cadastrado
		c = num+j+1 
		print("\n")
		# Controles para evitar a digitação de caracteres inválidos no nome do cidadão
		ent=f"\nDigite o nome do cidadão {c} : "
		nome=valt(input(ent),ent)
		# Controle para evitar idade não numérica, nula ou decimal
		ent=f"\nDigite a idade do cidadão {c} em anos: "	
		idade=valn(input(ent),ent)
		sexo=input("\nDigite o sexo de %s [M]Masculino ou [F]Feminino ou [X]LGBTQIA+: " %c)
        # Controles para prever possíveis variações na digitação dos sexos masculino e feminino, considerando os demais casos como LGBTQIA+
		sexo_aux=sexo.lower()
		sexo_bin="masculino-feminino"
		if(sexo_aux==sexo_bin[:len(sexo_aux)]):
			sexo='M'
		elif(sexo_aux==sexo_bin[10:(10+len(sexo_aux))]):
			sexo='F'
		else:
			sexo='X'
		# Controle para garantir que o CPF digitado seja um número com 11 dígitos válidos distintos dos já cadastrados
		cpf=""
		while cpf=="" or cpf in cid[0].keys():
			ent=f"\nDigite o CPF do novo cidadão {c} : "
			cpf=valt(input(ent),ent)
		# Agregação dos dados cadastrais do cidadão nos dicionários contidos na tupla cid	
		cid[0].update({cpf : nome})
		cid[1].update({cpf : idade})
		cid[2].update({cpf : sexo})		
	return cid

# Função para realizar cadastro das perguntas sobre os sintomas (com parâmetros "bat, num, sint" e retorno "bat")
def cadastrar_perguntas(bat,num,sint):
	print("\n\t\t--- CADASTRO DE PERGUNTAS ---")    
	qte=input("\nIndique o número de perguntas que deseja cadastrar: ")
	# Controle para evitar quantidade de perguntas não numérica, nula, decimal ou superior à quantidade de sintomas possíveis
	qte_aux=qte.replace(".","")
	while not qte.isnumeric() or qte_aux!=qte or qte_aux=="0" or qte_aux=="" or num+int(qte)>len(sint):
		print("\nQuantidade inválida! O número total de perguntas deve estar entre 1 e a quantidade de sintomas catalogados: ",len(sint))
		qte=input("\nIndique o número de perguntas que deseja cadastrar: ")
		qte_aux=qte.replace(".","")
    # Definição de uma quantidade válida de perguntas como número inteiro
	qte=int(qte)
	# Tratamento do caso em que não se deseja cadastrar perguntas
	if qte==0:
		exit
	# Controle do cadastro de novas perguntas para cada sintoma	
	else:
		for j in range(qte):
			# Tratamento de cada nova pergunta cadastrada
			p = num+j+1
			print("\n\nSintoma:",sint[p])
			ent = f"\nDigite a pergunta {p} sem ponto de interrogação incluindo o sintoma acima : "
			sai = valt(input(ent),ent) + "?"
			while not sint[p].lower() in sai.lower():
				print("\n\nSintoma:",sint[p])
				ent = f"\nDigite a pergunta {p} sem ponto de interrogação incluindo o sintoma acima : "
				sai = valt(input(ent),ent) + "?"
			bat.update({p:sai})
	return bat

# Função para realizar cadastro de usuários credenciados no sistema (com parâmetros "usu, num" e retorno "usu")
def cadastrar_usuarios(usu,num,cid):
	print("\n\t\t--- CADASTRO DE USUÁRIOS ---")
    # Controle para evitar quantidade de usuários não numérica, nula ou decimal
	ent="\nIndique o total de usuários a adicionar ao grupo : "
	tot=valn(input(ent),ent)
	# Definição de uma quantidade válida de usuários como número inteiro	
	tot=int(tot)
	# Controle do fluxo de cadastro dos usuários
	for j in range(tot):
        # Ordem de cada novo usuário cadastrado
		c = num+j+1 
		print("\n")
		# Controles para evitar entradas inválidas no login do usuário
		ent=f"\nDigite o nome do usuário {c} : "
		adm="administrador"
		ger="gerente"
		login=""
		while(login==""):
			tipo=input(f"\nDigite o tipo de usuário credenciado {c} : Administrador(ADM) ou Gerente(GER)\n")
			if(tipo.lower()==adm[:len(tipo)]):
				login="ADM-"+valt(input(ent),ent)
				print("\nSeu nome de usuário para login é:",login)
			elif(tipo.lower()==ger[:len(tipo)]):
				login="GER-"+valt(input(ent),ent)
				print("\nSeu nome de usuário para login é:",login)
			else:
				print("\nTipo inválido de usuário!")
		# A senha não possui qualquer restrição de caracteres
		ent=input(f"\nDigite a senha do usuário {c} : ")	
		senha=ent
		# Agregação dos dados cadastrais do usuário nos dicionários contidos na tupla usu	
		usu[0].update({c : login})
		usu[1].update({c : senha})	
	return usu