# Biblioteca de front-end 02 com funções para listar resultados na tela aos usuários

# Importação da biblioteca random da linguagem para gerar respostas pseudoaleatórias
import random as rd

# Função para imprimir os cidadãos cadastrados (com parâmetro "cid" e sem retorno)
def listar_cidadaos(cid):
    print("\n\t\t--- LISTA DOS CIDADÃOS CADASTRADOS ---")
    # Tratamento do caso em que não há cidadãos cadastrados
    if len(cid[0])==0:
        print("\nÉ necessário cadastrar cidadãos primeiro!")
    # Exibição dos cidadãos cadastrados (nome e CPF)        
    else:
        j = 0 
        for pes in cid[0].items():
            res_cid = pes[1] + " - " + pes[0]
            j += 1
            print("\nPessoa",j,": ",res_cid,"\n")

# Função para imprimir as perguntas sobre os sintomas cadastradas (com parâmetro "perg" e sem retorno)
def listar_perguntas(perg):
    print("\n\t\t--- LISTA DE PERGUNTAS CADASTRADAS ---")
    # Tratamento do caso em que não há perguntas cadastradas
    if len(perg)==0:
        print("\nÉ necessário cadastrar perguntas primeiro!")
    # Exibição das perguntas cadastradas
    else:
        k = 0
        for que in perg.items():
            res_perg = que[1]
            k += 1
            print("\nPergunta",k,": ",res_perg,"\n")

# Função para imprimir os usuários credenciados do sistema (com parâmetro "usu" e sem retorno)
def listar_usuarios(usu):
    print("\n\t\t--- LISTA DE USUÁRIOS CREDENCIADOS ---")
    # Tratamento do caso em que não há usuários credenciados
    if len(usu[0])==0:
        print("\nÉ necessário credenciar usuários como administradores ou gerentes!")
    # Exibição dos usuários credenciados
    else:
        l = 0
        for ind in usu[0].items():
            res_usu = "nome - " + ind[1].split("-")[1] + ", perfil - " + ind[1].split("-")[0]
            l += 1
            print("\nUsuário",l,":",res_usu,"\n")

# Função para imprimir as perguntas de perfil cadastradas (com parâmetro "cump" e retorno "res_cump")
def listar_cumprimentos(cump):
    # Exibição dos cumprimentos cadastrados
    print("\n\nSaudações: ")
    for elem in cump[0]:
        print("\n",elem)
    print("\n\nDespedidas: ")
    for elem in cump[1]:
        print("\n",elem)
    res_cump = "\n\n*Cumprimentos cadastrados*"
    return res_cump

# Função para imprimir despedidas (com parâmetro "desp" e sem retorno)
def despedir(desp):
    # Chamada da função randint da biblioteca random
	intx=rd.randint(0,len(desp)-1)
	# Impressão de despedida aleatória
	print("\n",desp[intx])