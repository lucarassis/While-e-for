def imprimir_maior_numero():
    numero1 = input("Digite o primeiro número: ")

    numero2 = input("Digite o segundo número: ")

    try:
        numero1 = int(numero1)
        numero2 = int(numero2)
        if numero1 > numero2:
            print("O número", numero1, "é maior que o número", numero2)
        elif numero1 == numero2:
            print("Os números são iguais")
        else:
            print("O número", numero2, "é maior que o número", numero1)
    except Exception:
        print("Você não digitou um número válido")
        exit()


def verificar_valor_positivo():
    # Faça um Programa que peça um valor e mostre na tela se o valor é positivo 
    # ou negativo.

    valor = int(input("Digite um valor: "))

    if valor > 0:
        print("O valor é positivo")
    elif valor == 0:
        print("O valor é neutro")
    else:
        print("O valor é negativo")

# Criar um menu para mostrar as funções disponíveis e o usuário selecionar qual
# função ele quer executar.
def menu():
    opcao = 1  
    while opcao != 0:
        print('----Seja bem vindo ao meu Super Menu----')
        print('Escolha uma opção abaixo:')
        print('1 - Imprimir maior número')
        print('2 - Verificar se o valor é positivo ou negativo')
            
        opcao = int(input('Digite uma das opções ou 0 para sair:'))
        if opcao == 1:
            print('---Iniciando a função imprimir_maior_numero---')
            imprimir_maior_numero()
            print('---Fim da função imprimir_maior_numero---')
        elif opcao == 2:
            print('---Iniciando a função verificar_valor_positivo---')
            verificar_valor_positivo()
            print('---Fim da função verificar_valor_positivo---')
        else:
            print('Opção inválida')

        print('----Fim do menu ----')
        
# Chamar função de menu
menu()