print('Olá, seja bem vindo a calculadora lhmontech!')
N = 1
while N != 0:
    opcao = int(input('\nDigite qual Calculo gostaria de realizar: \n1- Sequência de Fibonacci \n2- Sequência de Tribonacci \n3- Sequência Geométrica \n4- Fatorial \n5- Quadrados perfeitos \n6- Numeros primos'
                      '\n7- Sequência alternada \n8- Cubos \n9- Sair \n'))
    match opcao:
##Cálculo da sequência de Fibonacci
        case 1:
            print('Bem vindo ao calculo de Fibonacci.')

##Cálculo para a sequência de Tribonacci
        case 2:
            print('Bem vindo ao calculo de Tribonacci.')

##Cálculo para a sequência geométrica
        case 3:
            print('Bem vindo ao calculo da sequência geométrica.')

##Cálculo do número fatorial
        case 4:
            print('Bem vindo ao calculo da fatorial.')

#Cálculo dos quadrados perfeitos
        case 5:
            print('Bem vindo ao calculo dos quadrados perfeitos.')

##Sequência de numeros primos
        case 6:
            print('Bem vindo ao calculo da sequência de numeros primos.')

##Sequência alternada
        case 7:
            print('Bem vindo ao calculo da sequência alternada.')

##Sequência de cubos
        case 8:
            print('Bem vindo ao calculo dos cubos.')

##Opção de saída
        case 9:
            print('Fim do programa!')
            N = 0

##Opção para caso o usuário digite um valor fora das opções válidas
        case _:
            print('Erro! Digite um valor válido.')
