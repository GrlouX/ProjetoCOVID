# Biblioteca de back-end 03 com funções para gerar relatórios dos dados coletados

import itertools as it
from prettytable import PrettyTable as pt

# Função para imprimir relatórios consolidados de cidadãos por idade e faixa etária (com parâmetro "cidadão" e sem retorno)
def relatorios_cidadaos(cid):
	print("\n\n\t~~~~RELATÓRIOS DOS CIDADÃOS~~~~\n")
	if len(cid[0])==0:
		print("Não é possível exibir os relatórios consolidados, pois não há cidadãos cadastrados.")
	else:
	# Agrupamento dos cidadãos por faixas etárias e gêneros	
		faixas = {'Crianças':[], 'Adolescentes':[], 'Adultos':[], 'Idosos':[]}
		generos = {'Masculino':[], 'Feminino':[], 'LGBTQIA+':[]}
		for cad in cid[0].keys():
			if int(cid[1][cad])<12:
				faixas['Crianças'].append(cad)
			if int(cid[1][cad])>=12 and int(cid[1][cad])<18:
				faixas['Adolescentes'].append(cad)
			if int(cid[1][cad])>=18 and int(cid[1][cad])<60:
				faixas['Adultos'].append(cad)
			if int(cid[1][cad])>=60:
				faixas['Idosos'].append(cad)
			if cid[2][cad]=='M':
				generos['Masculino'].append(cad)
			if cid[2][cad]=='F':
				generos['Feminino'].append(cad)
			if cid[2][cad]=='X':
				generos['LGBTQIA+'].append(cad)
	# Impressão do relatório consolidado dos gêneros
		print("\n\nSUMARIZAÇÃO DOS CIDADÃOS CADASTRADOS POR GÊNEROS:\n")
		for elem in generos.items():
			print('\n',elem[0],':',elem[1])
		print('\n',list(generos.keys())[0],':',len(list(generos.items())[0][1]),'\n',list(generos.keys())[1],':',len(list(generos.items())[1][1]),'\n',list(generos.keys())[2],':',len(list(generos.items())[2][1]))
	# Impressão do relatório consolidado das faixas etárias
		print("\n\nSUMARIZAÇÃO DOS CIDADÃOS CADASTRADOS POR FAIXAS ETÁRIAS:\n")
		for elem in faixas.items():
			print('\n',elem[0],':',elem[1])
		print('\n',list(faixas.keys())[0],':',len(list(faixas.items())[0][1]),'\n',list(faixas.keys())[1],':',len(list(faixas.items())[1][1]),'\n',list(faixas.keys())[2],':',len(list(faixas.items())[2][1]),'\n',list(faixas.keys())[3],':',len(list(faixas.items())[3][1]))
	# Impressão do relatório consolidado de gêneros por faixas etárias
		mat_gf = [[pf for pf in list(generos.values())[a] if pf in list(faixas.values())[b]] for (a,b) in it.product(range(len(generos)),range(len(faixas)))]
		print("\n\nSUMARIZAÇÃO DOS CADASTRADOS POR GÊNERO E FAIXA ETÁRIA:\n\n")
		for (a,b) in it.product(range(len(generos)),range(len(faixas))):
			print('Gênero',list(generos.keys())[a],'Faixa',list(faixas.keys())[b],':',mat_gf[a*len(faixas)+b])
		tab = pt(["Gêneros/Faixas",list(faixas.keys())[0],list(faixas.keys())[1],list(faixas.keys())[2],list(faixas.keys())[3],"Subtotais por gênero"])
		tab.align["Gêneros/Faixas"] = "l"
		tab.align[list(faixas.keys())[0]],tab.align[list(faixas.keys())[1]],tab.align[list(faixas.keys())[2]],tab.align[list(faixas.keys())[3]] = "c","c","c","c"
		tab.align["Subtotais por gênero"] = "r"
		tab.add_row([list(generos.keys())[0],len(mat_gf[0]),len(mat_gf[1]),len(mat_gf[2]),len(mat_gf[3]),sum(len(mat_gf[i]) for i in range(len(faixas)))])
		tab.add_row([list(generos.keys())[1],len(mat_gf[4]),len(mat_gf[5]),len(mat_gf[6]),len(mat_gf[7]),sum(len(mat_gf[4+i]) for i in range(len(faixas)))])
		tab.add_row([list(generos.keys())[2],len(mat_gf[8]),len(mat_gf[9]),len(mat_gf[10]),len(mat_gf[11]),sum(len(mat_gf[8+i]) for i in range(len(faixas)))])
		tab.add_row(["Subtotais por faixa",sum(len(mat_gf[4*j]) for j in range(len(generos))),sum(len(mat_gf[1+4*j]) for j in range(len(generos))),sum(len(mat_gf[2+4*j]) for j in range(len(generos))),sum(len(mat_gf[3+4*j]) for j in range(len(generos))),sum(len(mat_gf[k]) for k in range(len(generos)*len(faixas)))])
		tab_lin = tab.get_string().split('\n')
		print("\n".join(tab_lin[:-2]))
		print(tab_lin[0])
		print("\n".join(tab_lin[-2:]))

# Função para imprimir relatórios consolidados de sintomas encontrados entre os entrevistados (com parâmetros "cidadão,respostas,sintomas" e sem retorno)
def relatorios_sintomas(cid,resp,sint):
	print("\n\n\t~~~~RELATÓRIOS DOS SINTOMAS~~~~\n")
	if len(cid[0])==0 or len(resp)==0:
		print("Não é possível exibir os relatórios consolidados, pois não há cidadãos cadastrados ou respostas ao questionário.")
	else:
	# Agrupamento dos cidadãos por principais sintomas informados	
		positivos = {'Febre':[], 'Tosse':[], 'Ageusia':[], 'Anosmia':[], 'Ageusia & Anosmia':[]} # Ageusia = perda de paladar, anosmia = perda de olfato
		for cad in cid[0].keys():
			try:
				if resp[cad][1]=='s':
					positivos['Febre'].append(cad)
				if resp[cad][2]=='s':
					positivos['Tosse'].append(cad)
				if resp[cad][3]=='s':
					positivos['Ageusia'].append(cad)
				if resp[cad][4]=='s':
					positivos['Anosmia'].append(cad)
				if resp[cad][3]=='s' and resp[cad][4]=='s':
					positivos['Ageusia & Anosmia'].append(cad)
			except:
				continue
	# Impressão do relatório consolidado dos sintomas
		print("\n\nSUMARIZAÇÃO DOS SINTOMAS DETECTADOS NOS CIDADÃOS CADASTRADOS:\n")
		print('\n',list(positivos.keys())[0],':',len(list(positivos.items())[0][1]),'\n',list(positivos.keys())[1],':',len(list(positivos.items())[1][1]),'\n',list(positivos.keys())[2],':',len(list(positivos.items())[2][1]),'\n',list(positivos.keys())[3],':',len(list(positivos.items())[3][1]),'\n',list(positivos.keys())[4],':',len(list(positivos.items())[4][1]))

# Linhas válidas de código da biblioteca de back-end 03: 70
# Comandos da linguagem (10): "print(str)", "input()", "upper(str)", "enumerate(list)", "len(str/list)", "range(num_ini,num_fin)", "int(str)", "lower(str)", "count(str)", "replace(str_ext,str_int)", "isnumeric(str)", "pass", "exit"
# Variáveis (20): "faixas" - list(str), "pessoas_faixas" - list(str), "generos" - list(str), "pessoas_generos" - list(str), "sintomas" - list(str), "pessoas_sintomas" - list(str), "ind" - int, "val" - str, "pes" - int, "sub" - int, "eta" - list, "gen_dados" - str, "fxe_dados" - str, "f" - str , "mat_gfe" - list(list), "id" - set, "elem" - tuple, "mat_gf" - list(list), "tab" - obj, "tab_lin" - list(obj).
