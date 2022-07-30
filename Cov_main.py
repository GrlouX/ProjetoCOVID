# Código principal de aplicativo para registrar e fornecer respostas sobre COVID-19 a um grupo de pessoas

# Importação das bibliotecas de front-end e back-end
from Cov_front01_v10 import logar as lgr, menu_cadastros as mncad, menu_cidadaos as mncid, menu_listas as mnlist, menu_relatorios as mnrel #Biblioteca front-end de menus
from Cov_front02_v10 import listar_cumprimentos as listcump, listar_cidadaos as listcid, listar_perguntas as listperg, listar_usuarios as listusu, despedir as dpr #Biblioteca front-end de listagens
from Cov_back00_v10 import erro_menu_princ as errmnpri, erro_menu_secund as errmnsec, erro_menu_terci as errmnter #Biblioteca back-end para tratamento de erros e operações auxiliares
from Cov_back01_v10 import cadastrar_cumprimentos as cadcump, cadastrar_cidadaos as cadcid, importar_arquivo as imparq, cadastrar_perguntas as cadperg, cadastrar_usuarios as cadusu #Biblioteca back-end de cadastros
from Cov_back02_v10 import questionario as quest, diagnostico as diag #Biblioteca back-end de entrevista e diagnóstico
from Cov_back03_v10 import relatorios_cidadaos as relatcid, relatorios_sintomas as relatsint #Biblioteca back-end de relatórios

# Listas de saudações e despedidas pré-cadastradas, para possibilitar cumprimentos na primeira iteração do algoritmo
saudacoes=["\nBem-vindos(as) ao app MonitoraCOVID!","\nOlá pessoas! App MonitoraCOVID na área.","\nOi pessoal! Teste do app MonitoraCOVID para a galera!"]
despedidas=["\nObrigado por testarem o app e usem máscara!","\nA equipe do MonitoraCOVID deseja a todo(a)s muita saúde!","\nAgradecemos por usarem o MonitoraCOVID e fiquem bem!"]
# Inicialização da tupla de cumprimentos, contendo saudações e despedidas
cumprimentos=(saudacoes,despedidas)
# Dicionário de sintomas possíveis para a COVID-19*
sintomas={1: 'Febre', 2: 'Tosse', 3: 'Sem paladar', 4: 'Sem olfato', 5: 'Cefaleia', 6: 'Dor de garganta', 7: 'Coriza', 8: 'Diarreia'}
# Inicialização dos dicionários de dados dos usuários 
login={}
senha={}
# Inicialização da tupla de identificação de usuários, contendo os dados de autenticação
autuser = (login,senha)
# Inicialização dos dicionários de dados dos cidadãos
nomes={}
idades={}
generos={}
# Inicialização da tupla de cidadãos, contendo todos os dados identificados por chave (CPF)
cidadaos = (nomes,idades,generos)
# Inicialização do dicionário de perguntas a cadastrar
perguntas={}
# Inicialização do dicionário de respostas dos usuários
respostas={}
# Inicialização do dicionário de recomendações aos usuários
recomend={}
# Inicialização para as opções dos menus possíveis: administrador/gestor/cidadãos, cadastros, listas, entrevistas e relatórios
opc=[None,None,None,None,None]
opc[0]=-1
# Controle das opções de acesso no menu principal
while(opc[0] != "0"):
    # Chamada da função logar da biblioteca de front-end 01
    opc[0]=lgr(cumprimentos[0],autuser,cidadaos)
    # Opções de cadastros possíveis
    if(opc[0]=="1"):
        # Chamada da função menu_cadastros da biblioteca de front-end 01
        opc[1]=mncad()
        # Chamada da função erro_menu_princ da biblioteca de back-end 00
        errmnpri(opc[1])
        # Opção cadastrar cidadãos
        if(opc[1]=="1"):
            # Variável de controle da quantidade de cidadãos previamente cadastrados em cada iteração
            quantidade_cid = len(nomes)
            # Chamada da função menu_cidadaos da biblioteca de front-end 01
            opc[2]=mncid()
            # Chamada da função erro_menu_terci da biblioteca de back-end 00
            errmnter(opc[2])
            # Opção de cadastro automático
            if(opc[2]=="1"):
                # Chamada da função importar_arquivo da biblioteca de back-end 01
                cidadaos = imparq(cidadaos)
            # Opção de cadastro manual
            if(opc[2]=="2"):
                # Chamada da função cadastrar_cidadaos da biblioteca de back-end 01
                cidadaos = cadcid(cidadaos,quantidade_cid)
            # Opção sair
            if(opc[2]=="3"):
                exit
        # Opção cadastrar perguntas da biblioteca de back-end 01  
        if(opc[1]=="2"):
            # Variável de controle da quantidade de perguntas previamente cadastradas em cada iteração
            quantidade_perg = len(perguntas)
            # Chamada da função cadastrar_perguntas da biblioteca de back-end 01
            perguntas = cadperg(perguntas,quantidade_perg,sintomas)
        # Opção cadastrar cumprimentos (saudações e despedidas) da biblioteca de back-end 01  
        if(opc[1]=="3"):
            cumprimentos = cadcump(cumprimentos)
        # Opção cadastrar usuários da biblioteca de back-end 01
        if(opc[1]=="4"):
            # Variável de controle da quantidade de usuários previamente credenciados em cada iteração
            quantidade_usu = len(login)
            # Chamada da função cadastrar_usuarios da biblioteca de back-end 01
            autuser = cadusu(autuser,quantidade_usu,cidadaos)
        # Opção sair    
        if(opc[1]=="5"):
            exit
    # Opções de listagens possíveis        
    if(opc[0]=="2"):
        # Chamada da função menu_listas da biblioteca de front-end 01
        opc[2]=mnlist()
        # Chamada da função erro_menu_secund da biblioteca de back-end 00
        errmnpri(opc[2])
        # Opção listar cidadãos da biblioteca de front-end 02
        if(opc[2]=="1"):
            listcid(cidadaos)
        # Opção listar perguntas da biblioteca de front-end 02   
        if(opc[2]=="2"):
            listperg(perguntas)
        # Opção listar cumprimentos (saudações e despedidas) da biblioteca de front-end 02  
        if(opc[2]=="3"):
            print(listcump(cumprimentos))
        # Opção listar usuários da biblioteca de front-end 02
        if(opc[2]=="4"):
            autuser = listusu(autuser)
        # Opção sair    
        if(opc[2]=="5"):
            exit
    # Entrevistas e resultados        
    if(opc[0]=="3"):
        # Controle de fluxo dos cidadãos entrevistados
        total=len(nomes)
        # Tratamento do caso em que nenhum cidadão foi cadastrado
        if total==0:
            print("\nNão há cidadãos cadastrados!")
            exit
        # Rotina de entrevistas e respostas para cada cidadão cadastrado    
        else:
            respostas = quest(cidadaos,perguntas)
            recomend = diag(cidadaos,respostas)
    if(opc[0]=="4"):
        # Chamada da função menu_relatorios da biblioteca de front-end 01
        opc[3]=mnrel()
        # Chamada da função erro_menu_terci da biblioteca de back-end 00
        errmnter(opc[3])
        # Opção relatórios dos cidadãos  
        if(opc[3]=="1"):
            # Chamada da função relatorios_cidadaos da biblioteca de back-end 03
            relatcid(cidadaos)
        # Opção relatórios dos sintomas   
        if(opc[3]=="2"):
            # Chamada da função relatorios_sintomas da biblioteca de back-end 03
            relatsint(cidadaos,respostas,sintomas)
        # Opção sair    
        if(opc[3]=="3"):
            exit
print("."*60)
# Chamada da função despedir da biblioteca de front-end 02
dpr(cumprimentos[1])
print("."*60)