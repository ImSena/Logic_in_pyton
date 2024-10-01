#decidi usar dicionário aqui também

parcela_juros = {
    "1": 0,
    "3": 10,
    "6": 15,
    "9": 20,
    "12": 25
}

while(True):
    
    divida = 0.00;
    resposta = "";
    
    while(True):
        try:
            divida = float(input("Digite o valor atual da divida\n->"));
            break;
        except ValueError:
            print("Digite um valor númerico");
    print('\n');
    
    print("Agora vamos negociar sua divida...");
    
    for qtd_parcelas, juros in parcela_juros.items():
        
        valor_juros = divida * (juros / 100);
        
        if(juros == 0):
            valor_juros = 0;
            
        total_divida = divida + valor_juros;
        
        parcela = total_divida / int(qtd_parcelas);
        
        
        print(f"Total: {total_divida} Juros: {valor_juros} Número de parcelas: {qtd_parcelas} Valor da Parcela: {parcela:.2f}");
    
    print('\n');
    
    while(True):
        resposta = input("Deseja calcular outra divida?(s/n)\n->").lower();
        
        try:
            if(resposta != 'n' and resposta != 's'):
                raise Exception("Por favor, digite 's' para sim ou 'n' para não");
            else:
                break;
        except Exception as error:
            print(error);
            
    if(resposta == 'n'):
        print("Até mais!");    
        break;
    
    
    
    

