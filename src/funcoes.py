# Esse programa usa uma def com parâmetros e outra def com return
# também poderíamso ter uma def com as duas coisas juntas: parâmetros e return 

# Funções (defs) do programa
def gerar_tabuada(parNumeroTabuada):
    print(f"Tabuada do {parNumeroTabuada}:")
    for contador in range(1, 11):
        resultado = multiplicar(parNumeroTabuada, contador)
        print(f"{parNumeroTabuada} x {contador} = {resultado}")
    return resultado

def multiplicar(x,y):
    return x * y


def menu(resposta = 0): 
    print("1. Mostrar tabuada")
    print("2. Sair")
    if not resposta:   
        resposta = input("Escolha uma opção: ")
    return resposta

def main(opcao = 0, resposta = 0):

# Programa Principal
   
    opcao = menu(opcao)
    if opcao == '1':
        print("De qual número você quer ver a tabuada?")
        if resposta: 
            print(resposta)
        else:
            resposta = int(input())
        return gerar_tabuada(resposta)
    elif opcao == '2':
        print("Saindo do programa...")
    else:
        print("Opção inválida.")