print("Bem-vindo!\n");

#decidi usar dicionário aqui 

parcelas = {
    "6": 3,
    "12": 6,
    "18": 9,
    "24": 12,
    "30": 15,
    "36": 18,
    "42": 21,
    "48": 24,
    "54": 27,
    "60": 30
}

while(True):
    valor_carro = 0.00;
    resposta = "";
    
    while(True):
        try:
            valor_carro = float(input("Digite o valor do carro\n->"));
            break;
        except ValueError:
            print("Digite apenas valores numéricos\n");
            
    print("\n");
    print(f"O preço final à vista com desconto 20% é: {valor_carro * 0.8:.2f}");
    for qtd_parcela, valor_parcela in parcelas.items():
        
        acrescimo = valor_carro * (valor_parcela / 100);
        valor_final = valor_carro + acrescimo;
        valor_parcela = valor_final / int(qtd_parcela);
        
        print(f"O preço final parcelado em {qtd_parcela}x  é de : {valor_final:.2f} com parcelas de R$ {valor_parcela:.2f}");
    
    print("\n");
    
    while(True):
        resposta = input("Deseja calcular um novo valor?(s/n)\n->").lower();
        
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

