dados = {
    'Tipo sanguíneo':['O+', 'O-', 'A+','A-','B+','B-','AB+','AB-' ],
    'Hemácias':'As hemácias, também denominadas eritrócitos ou glóbulos vermelhos, são as células mais numerosas do sangue,\n cuja forma é de disco bicôncavo com espessura maior da margem (2,6 µm) e espessura menor no centro (0,8 µm)',    
    'Globulos Brancos':'Os glóbulos brancos constituem um conjunto de células produzidas na medula óssea e que fazem parte do sistema imunológico do organismo.\n Também chamadas de leucócitos, os glóbulos brancos podem ser encontrados no sangue, linfa, órgãos linfóides e vários tecidos conjuntivos.',
    'Plaquetas':'As plaquetas, também chamadas de trombócitos, são estruturas presentes no sangue que, diferentemente do que muitos pensam, não são células completas. '
}

dic_sangue = {
    'O+':'36% ',
    'O-':'9%',
    'A+':'34%',
    'A-':'8%',
    'B+':'8%',
    'B-':'2%',
    'AB+':'2,5%',
    'AB-':'0,5%'
}


def forca_opcao_dados(msg, msg_erro = None):
        opcao = ['Tipo sanguíneo','Hemácias', 'Globulos Brancos','Plaquetas']
        resposta = input(msg)
        while resposta not in opcao:
            print('\nEscolha uma opção válida!\n')
            if msg_erro:
                for i in range(len(opcao)):
                    print(opcao[i])
            resposta = input(msg)
        return resposta

def forca_opcao_dic_sangue(msg, msg_erro = None):
    opcao = ['O+', 'O-', 'A+','A-','B+','B-','AB+','AB-']
    resposta = input(msg)
    while resposta not in opcao:
        print('\nEscolha uma opção válida!\n')
        if msg_erro:
            print(msg_erro)
        resposta = input(msg)
    return resposta


def mostra_chave(dicionario,indice=None):
    chaves = dicionario.keys()
    chaves = list(chaves)
    if indice == None:
        return chaves
    else:
        return chaves[indice]




def menu():
    opcoes = ['Tipo sanguíneo','Hemácias', 'Globulos Brancos','Plaquetas','Sair']
    while True:
        opcao = forca_opcao_dados('O que deseja saber ?', dados)
        if opcao == opcoes[0]:
            while True:
                sangues_chaves = ['O+', 'O-', 'A+','A-','B+','B-','AB+','AB-']
                input_sangue = (forca_opcao_dic_sangue('Qual seu tipo sanguíneo ?','\n'.join(sangues_chaves)))
                if input_sangue in dic_sangue.keys():
                    sangue_populacao = dic_sangue[input_sangue]
                    print(f"O tipo de sangue escolhido foi o {input_sangue}, este tipo compôe cerca de {sangue_populacao} da população brasileira")
                    return False
                
        elif opcao == opcoes[1]:
            print(f"{dados[opcao]}")

        elif opcao == opcoes[2]:
            print(f"{dados[opcao]}")

        elif opcao == opcoes[3]:
            print(f"{dados[opcao]}")

        elif opcao == opcao[4]:
            break
            
        
menu()
