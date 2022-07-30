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
		faixas_chaves = {'Crianças':[], 'Adolescentes':[], 'Adultos':[], 'Idosos':[]}
		faixas_valores = {'Crianças':[], 'Adolescentes':[], 'Adultos':[], 'Idosos':[]}
		generos_chaves = {'Masculino':[], 'Feminino':[], 'LGBTQIA+':[]}
		generos_valores = {'Masculino':[], 'Feminino':[], 'LGBTQIA+':[]}
		for cad in cid[0].keys():
			if int(cid[1][cad])<12:
				faixas_chaves['Crianças'].append(cad)
				faixas_valores['Crianças'].append(int(cid[1][cad]))
			if int(cid[1][cad])>=12 and int(cid[1][cad])<18:
				faixas_chaves['Adolescentes'].append(cad)
				faixas_valores['Adolescentes'].append(int(cid[1][cad]))
			if int(cid[1][cad])>=18 and int(cid[1][cad])<60:
				faixas_chaves['Adultos'].append(cad)
				faixas_valores['Adultos'].append(int(cid[1][cad]))
			if int(cid[1][cad])>=60:
				faixas_chaves['Idosos'].append(cad)
				faixas_valores['Idosos'].append(int(cid[1][cad]))
			if cid[2][cad]=='M':
				generos_chaves['Masculino'].append(cad)
				generos_valores['Masculino'].append(int(cid[1][cad]))
			if cid[2][cad]=='F':
				generos_chaves['Feminino'].append(cad)
				generos_valores['Feminino'].append(int(cid[1][cad]))
			if cid[2][cad]=='X':
				generos_chaves['LGBTQIA+'].append(cad)
				generos_valores['LGBTQIA+'].append(int(cid[1][cad]))
	# Impressão do relatório consolidado dos gêneros
		print("\n\nSUMARIZAÇÃO DOS CIDADÃOS CADASTRADOS POR GÊNEROS:\n")
		for elem in generos_chaves.items():
			print('\n',elem[0],':',elem[1])
		print('\n',list(generos_chaves.keys())[0],':',len(list(generos_chaves.items())[0][1]),'\n',list(generos_chaves.keys())[1],':',len(list(generos_chaves.items())[1][1]),'\n',list(generos_chaves.keys())[2],':',len(list(generos_chaves.items())[2][1]))
	# Impressão do relatório consolidado das faixas etárias
		print("\n\nSUMARIZAÇÃO DOS CIDADÃOS CADASTRADOS POR FAIXAS ETÁRIAS:\n")
		for elem in faixas_chaves.items():
			print('\n',elem[0],':',elem[1])
		print('\n',list(faixas_chaves.keys())[0],':',len(list(faixas_chaves.items())[0][1]),'\n',list(faixas_chaves.keys())[1],':',len(list(faixas_chaves.items())[1][1]),'\n',list(faixas_chaves.keys())[2],':',len(list(faixas_chaves.items())[2][1]),'\n',list(faixas_chaves.keys())[3],':',len(list(faixas_chaves.items())[3][1]))
	# Impressão do relatório consolidado de gêneros por faixas etárias
		mat_gf = [[pf for pf in list(generos_chaves.values())[a] if pf in list(faixas_chaves.values())[b]] for (a,b) in it.product(range(len(generos_chaves)),range(len(faixas_chaves)))]
		print("\n\nSUMARIZAÇÃO DOS CADASTRADOS POR GÊNERO E FAIXA ETÁRIA:\n\n")
		for (a,b) in it.product(range(len(generos_chaves)),range(len(faixas_chaves))):
			print('Gênero',list(generos_chaves.keys())[a],'Faixa',list(faixas_chaves.keys())[b],':',mat_gf[a*len(faixas_chaves)+b])
		tab = pt(["Gêneros/Faixas",list(faixas_chaves.keys())[0],list(faixas_chaves.keys())[1],list(faixas_chaves.keys())[2],list(faixas_chaves.keys())[3],"Subtotais por gênero"])
		tab.align["Gêneros/Faixas"] = "l"
		tab.align[list(faixas_chaves.keys())[0]],tab.align[list(faixas_chaves.keys())[1]],tab.align[list(faixas_chaves.keys())[2]],tab.align[list(faixas_chaves.keys())[3]] = "c","c","c","c"
		tab.align["Subtotais por gênero"] = "r"
		tab.add_row([list(generos_chaves.keys())[0],len(mat_gf[0]),len(mat_gf[1]),len(mat_gf[2]),len(mat_gf[3]),sum(len(mat_gf[i]) for i in range(len(faixas_chaves)))])
		tab.add_row([list(generos_chaves.keys())[1],len(mat_gf[4]),len(mat_gf[5]),len(mat_gf[6]),len(mat_gf[7]),sum(len(mat_gf[4+i]) for i in range(len(faixas_chaves)))])
		tab.add_row([list(generos_chaves.keys())[2],len(mat_gf[8]),len(mat_gf[9]),len(mat_gf[10]),len(mat_gf[11]),sum(len(mat_gf[8+i]) for i in range(len(faixas_chaves)))])
		tab.add_row(["Subtotais por faixa",sum(len(mat_gf[4*j]) for j in range(len(generos_chaves))),sum(len(mat_gf[1+4*j]) for j in range(len(generos_chaves))),sum(len(mat_gf[2+4*j]) for j in range(len(generos_chaves))),sum(len(mat_gf[3+4*j]) for j in range(len(generos_chaves))),sum(len(mat_gf[k]) for k in range(len(generos_chaves)*len(faixas_chaves)))])
		tab_lin = tab.get_string().split('\n')
		print("\n".join(tab_lin[:-2]))
		print(tab_lin[0])
		print("\n".join(tab_lin[-2:]))
	# Impressão das idades extremas por faixas
		print('\nCrianças com maior idade:',[cid[0][cad] for cad in faixas_chaves['Crianças'] if int(cid[1][cad])==max(faixas_valores['Crianças'])],max(faixas_valores['Crianças']),'anos')
		print('\nCrianças com menor idade:',[cid[0][cad] for cad in faixas_chaves['Crianças'] if int(cid[1][cad])==min(faixas_valores['Crianças'])],min(faixas_valores['Crianças']),'anos')
		print('\nAdolescentes com maior idade:',[cid[0][cad] for cad in faixas_chaves['Adolescentes'] if int(cid[1][cad])==max(faixas_valores['Adolescentes'])],max(faixas_valores['Adolescentes']),'anos')
		print('\nAdolescentes com menor idade:',[cid[0][cad] for cad in faixas_chaves['Adolescentes'] if int(cid[1][cad])==min(faixas_valores['Adolescentes'])],min(faixas_valores['Adolescentes']),'anos')
		print('\nAdultos com maior idade:',[cid[0][cad] for cad in faixas_chaves['Adultos'] if int(cid[1][cad])==max(faixas_valores['Adultos'])],max(faixas_valores['Adultos']),'anos')
		print('\nAdultos com menor idade:',[cid[0][cad] for cad in faixas_chaves['Adultos'] if int(cid[1][cad])==min(faixas_valores['Adultos'])],min(faixas_valores['Adultos']),'anos')
		print('\nIdosos com maior idade:',[cid[0][cad] for cad in faixas_chaves['Idosos'] if int(cid[1][cad])==max(faixas_valores['Idosos'])],max(faixas_valores['Idosos']),'anos')
		print('\nIdosos com menor idade:',[cid[0][cad] for cad in faixas_chaves['Idosos'] if int(cid[1][cad])==min(faixas_valores['Idosos'])],min(faixas_valores['Idosos']),'anos')	
	# Impressão das idades extremas por gêneros
		print('\nPessoas do gênero masculino com maior idade:',[cid[0][cad] for cad in generos_chaves['Masculino'] if int(cid[1][cad])==max(generos_valores['Masculino'])],max(generos_valores['Masculino']),'anos')
		print('\nPessoas do gênero masculino com menor idade:',[cid[0][cad] for cad in generos_chaves['Masculino'] if int(cid[1][cad])==min(generos_valores['Masculino'])],min(generos_valores['Masculino']),'anos')
		print('\nPessoas do gênero feminino com maior idade:',[cid[0][cad] for cad in generos_chaves['Feminino'] if int(cid[1][cad])==max(generos_valores['Feminino'])],max(generos_valores['Feminino']),'anos')
		print('\nPessoas do gênero feminino com menor idade:',[cid[0][cad] for cad in generos_chaves['Feminino'] if int(cid[1][cad])==min(generos_valores['Feminino'])],min(generos_valores['Feminino']),'anos')
		print('\nPessoas do gênero LGBTQIA+ com maior idade:',[cid[0][cad] for cad in generos_chaves['LGBTQIA+'] if int(cid[1][cad])==max(generos_valores['LGBTQIA+'])],max(generos_valores['LGBTQIA+']),'anos')
		print('\nPessoas do gênero LGBTQIA+ com menor idade:',[cid[0][cad] for cad in generos_chaves['LGBTQIA+'] if int(cid[1][cad])==min(generos_valores['LGBTQIA+'])],min(generos_valores['LGBTQIA+']),'anos')	# Ln 7-82


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