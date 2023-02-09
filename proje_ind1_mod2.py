######################################
#  Davi de Moraes Novaes             #
#  Modulo 2 - Projeto Individual 1   #
######################################
def avaliação():
    sair = 's'  #menu de sair
    while sair != 'n':  #puxando o while para atribuir mais de 1 elementa para a lista
        lista_n.append(input('Nome do candidato: ')) #adicionando nome da lista 
        e = float(input('Nota do candidato referente a ENTREVISTA: '))
        t = float(input('Nota do candidato referente a TESTE TEÓRICO: '))
        p = float(input('Nota do candidato referente a TESTE PRÁTICO: '))
        s = float(input('Nota do candidato referente a AVALIÇÃO SOFT SKILLS: '))
        lista_not.append(f'e{e}_t{t}_p{p}_s{s}') #adicionando os valores de e,t,p e s na lista
        print(f'Candidato {lista_n} adicionado na lsita com nota: {lista_not}')        
        print('Continuar? [S]im ou [N]ão? ')
        sair = input().lower()

lista_not = []
lista_n = []
avaliação()
print('*'*45)

def pesquisa(): #função def para realizar as pesquisas
    sair = ''
    while sair != 'n':          
        e = float(input('Pesquisa de nota da ENTREVISTA: '))
        t = float(input('Pesquisa de nota do TESTE TEÓRICO: '))
        p = float(input('Pesquisa de nota do TESTE PRÁTICO: '))
        s = float(input('Pesquisa de nota da AVALIÇÃO SOFT SKILLS: '))
        procura = f'e{e}_t{t}_p{p}_s{s}'
        for i,cand in enumerate(lista_not): #Usando for com enumerate para realizar a busca
            if cand == procura:
                print(f'O canditato aprovado seguindo os parâmetros estabelecidos foi : {lista_n[i]}')      
        print('Continuar? [S]im ou [N]ão? ')
        sair = input().lower()
    print('*'*45)


pesquisa()