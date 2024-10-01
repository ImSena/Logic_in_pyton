print("Bem-vindo!\n");

diasValidos = ['segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira'];

while(True):
    qtdColaboradores = 0;
    diasVotados = [];
    diasMaisVotados = [0] * len(diasValidos);
    diasComMaiorVoto = [];
    resposta = '';
        
    while(True):
        try:
            qtdColaboradores = int(input("Digite quantos colaboradores irão participar\n->"));
            break;
        except ValueError:
            print("DIGITE UM VALOR NUMÉRICO E INTEIRO\n");
    
    for collaborador in range(1,qtdColaboradores+1,1):

        while(True):
            print('\n');
            dia = input("Digite um dia da semana ('segunda-feira', 'terça-feira', 'quarta-feira', 'quinta-feira', 'sexta-feira')\n->");
            
            try:
                if(dia.lower() in diasValidos):
                    diasVotados.append(dia.lower());
                    break;
                else:
                    raise Exception("DIGITE O DIA CORRETAMENTE\n");
            except Exception as error:
                print(error);
        restanteVoto = qtdColaboradores - collaborador        
        plural =  f"Restam {restanteVoto} votos" if(restanteVoto) > 1 else f"Resta {restanteVoto} voto";
        if(restanteVoto > 0): print(plural);
    
    print("\n")
    
    for voto in diasVotados:
        if(voto in diasValidos):
            index = diasValidos.index(voto);
            diasMaisVotados[index] += 1;
    
    maiorVoto = 0;
    for votos in diasMaisVotados:
        if votos > maiorVoto:
            maiorVoto = votos;
    
    for count in range(len(diasValidos)):
        if(diasMaisVotados[count] == maiorVoto):
            diasComMaiorVoto.append(diasValidos[count]);
    
    if(len(diasComMaiorVoto) > 1):
        print(f"Houve um empate entre os dias: {diasComMaiorVoto}");
    else:
        print(f"O dia escolhido pelos colaboradores foi: {diasComMaiorVoto} com {maiorVoto} votos");
    
    while(True):
        resposta = input("Deseja refazer os votos?(s/n)\n->").lower();
        
        try:
            if(resposta != 's' and resposta != 'n'):
                raise Exception("Por favor, digite 's' para sim ou 'n' para não");
            else:
                break;
        except Exception as error:
            print(error);
    
    if(resposta == 'n'):
        print("Até mais!");
        break;
    
        
"""
pontos melhorias:
refatorar o código
usar dicionário

"""
    
        



