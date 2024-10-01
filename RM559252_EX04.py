def calcularJuros(valor, dias):
    
    aliquota = 0
    
    if(dias <= 180):
        aliquota = 0.225;
    elif(dias <= 360):
        aliquota = 0.2;
    elif(dias <= 720):
        aliquota = 0.175;
    else:
        aliquota = 0.15;
        
    valor *= aliquota;
    
    return valor

while(True):
    imposto = 0.00;
    choose = 0;
    resgate = 0.00;
    dias = 0;
    
    while(True):
        try:
            choose = int(input("Escolha o tipo de investimento:\n"
            "1 - CDB\n"
            "2 - LCI\n"
            "3 - LCA\n\n"
            "Digite (1, 2 ou 3):\n-> "));
            
            
            if(choose != 1 and choose != 2 and choose != 3):
                raise Exception("Digite uma opção válida...");
            else:
                break;
                
        except ValueError:
            print("Digite um valor númerico!");
        except Exception as error:
            print(error);
            
    print('\n');        
    while(True):
        try:
            resgate = float(input("Digite o valor a ser resgatado:\n->"));
            
            if(resgate > 0):
                break;
            else:
                raise Exception("Valor deve ser maior que zero");
        except ValueError:
            print("Digite um valor númerico");
        except Exception as error:
            print(error);
    
    print('\n');
    
    while(True):
        try:
            dias = int(input("Digite o número de dias que o valor permaneceu investido:\n->"));
            break;
        except ValueError:
            print("Digite um valor válido");
    
    print('\n');
         
    match(choose):
        case 1:
            imposto = calcularJuros(resgate, dias);
            print(f"O valor do imposto de renda a ser pago é: {imposto:.2f}");
        case _:
            print("Tipo de investimento isento de imposto de renda...");

    print('\n');
    
    while(True):
        resposta = input("Deseja calcular outra vez? (s/n)\n->").lower();
        
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
    
    