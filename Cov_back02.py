# Biblioteca de back-end 02 com funções para entrevista e diagnóstico

from Cov_back00_v10 import valid_num as valn, valid_tex as valt

# Função para capturar as respostas no questionário (com parâmetros "cid, bat" e retorno "resp")
def questionario(cid,bat):
	# Inicialização do dicionário de todas as respostas
	resp={}
	# Tratamento do caso em que não há perguntas cadastradas
	if len(bat)==0:
		print("\nÉ necessário cadastrar perguntas primeiro!")
		exit
	else:
		print("\n\t\t--- QUESTIONÁRIO AOS CIDADÃOS ---")
		# Controle para evitar quantidade de cidadãos não numérica, nula ou decimal ou maior que o número de cidadãos cadastrados
		tot=0
		while tot==0 or int(tot)>len(cid[0]):
			ent="\nIndique o total de cidadãos respondentes : "
			tot=valn(input(ent),ent)
		# Definição de uma quantidade válida de entrevistados como número inteiro	
		tot=int(tot)
		# Controle da entrevista aos cidadãos
		for j in range(tot):
			# Controle para garantir que o CPF digitado seja um número com 11 dígitos válidos entre os já cadastrados
			cpf=""
			while not cpf in cid[0].keys():
				ent=f"\nDigite o CPF de um cidadão cadastrado : "
				cpf=valn(input(ent),ent)
			# Inicialização do subdicionário das respostas do cidadão identificado
			respcid={}
			# Controle do fluxo das respostas
			print("\n\nPerguntas para",cid[0][cpf],":\n")
			k = 0
			for perg in bat.items():
				k += 1
				print("\nQuestão",k,":",perg[1],"[S]Sim ou [N]Não\n")
				r=input().lower()
				if(r=='s' or r=='si' or r=='sim' or r=='siim' or r=='simm' or r=='sim sim' or r=='isso isso isso'):
					r = "s"
				# Tratamento de todas as demais respostas como negativas	
				else:
					r = "n"
				respcid.update({k:r})
			resp.update({cpf:respcid})
			print("\nRespostas coletadas com sucesso!")
	return resp                

# Função para exibir o diagnóstico de acordo com cada entrevista (com parâmetros "cid, resp" e retorno "result")
def diagnostico(cid,resp):
	# Inicialização do dicionário dos resultados recomendados
	result={}
	# Teste para ausência de respostas
	if resp == None:
		result = "\nNão há respostas ao questionário para fornecer um diagnóstico."
	else:
		print("\n\t\t--- RECOMENDAÇÕES AOS CIDADÃOS ---")
		for elem in resp.items():
			# Inicialização da lista de respostas do cidadão aos sintomas críticos (4 primeiros)
			lista=["","","",""]
			num_resp=len(elem[1])
			# Construção da lista completa de respostas aos sintomas questionados 
			for i in range(num_resp):
				if i<4:
					lista[i]=elem[1][i+1].upper()
				else:
					lista.append(elem[1][i+1].upper())
			# Tratamento para o caso em que menos de 4 perguntas foram cadastradas		
			if lista.count("")>0:
				r = "Não há elementos suficientes para fornecer um diagnóstico conclusivo. Informe pelo menos 4 sintomas!"
			# Evidenciação do diagnóstico com base nos 4 sintomas críticos
			else:
				for item in lista:
					if lista[:4]==["S","S","S","S"]:
						r = cid[0][elem[0]] + ", vá imediatamente ao médico, é uma emergência!"
					elif lista[2]=="N" and lista[3]=="N":
						r = cid[0][elem[0]] + ", aguarde em casa e continue monitorando os sintomas."
					else:
						r = cid[0][elem[0]] + ", vá ao médico tão logo possível, é uma urgência!"
			result.update({elem[0]:r})
		for part in result.items():
			print("\nResultado para " + part[0] + ": ")
			print("\nRespostas: ",resp[part[0]])
			print("\nRecomendação: ",part[1],"\n")
	return result