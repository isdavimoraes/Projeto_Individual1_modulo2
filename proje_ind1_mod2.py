'''
Criar com Python uma lista para armazenar esses resultados
(e outros resultados que quiser no mesmo formato, o código
precisa funcionar para qualquer lista que seja inserida nesse
formato) e depois uma função que busca o candidato de
acordo com os critérios digitados pelo usuário.
candidato = input('Nome do candidato: ')

'''

def avaliação():
    sair = 's'
    while sair != 'n':
        lista_n.append(input('Nome do candidato: '))
        e = float(input('Nota do candidato referente a ENTREVISTA: '))
        t = float(input('Nota do candidato referente a TESTE TEÓRICO: '))
        p = float(input('Nota do candidato referente a TESTE PRÁTICO: '))
        s = float(input('Nota do candidato referente a AVALIÇÃO SOFT SKILLS: '))
        lista_not.append(f'e{e}_t{t}_p{p}_s{s}')
        print(f'Candidato {lista_n} adicionado na lsita com nota: {lista_not}')        
        print('Continuar? [S]im ou [N]ão? ')
        sair = input().lower()

lista_not = []
lista_n = []
avaliação()
print('*'*45)

def pesquisa():
    sair = ''
    while sair != 'n':          
        e = float(input('Pesquisa de nota da ENTREVISTA: '))
        t = float(input('Pesquisa de nota do TESTE TEÓRICO: '))
        p = float(input('Pesquisa de nota do TESTE PRÁTICO: '))
        s = float(input('Pesquisa de nota da AVALIÇÃO SOFT SKILLS: '))
        procura = f'e{e}_t{t}_p{p}_s{s}'
        for i,cand in enumerate(lista_not):
            if cand == procura:
                print(f'O canditato aprovado seguindo os parâmetros estabelecidos foi : {lista_n[i]}')      
        print('Continuar? [S]im ou [N]ão? ')
        sair = input().lower()
    print('*'*45)


pesquisa()