print('Olá, seja bem vindo a calculadora lhmontech!')
N = 1
while N != 0:
    opcao = int(input('\nDigite qual Calculo gostaria de realizar: \n1- Sequência de Fibonacci \n2- Sequência de Tribonacci \n3- Sequência Geométrica \n4- Fatorial \n5- Quadrados perfeitos \n6- Numeros primos'
                      '\n7- Sequência alternada \n8- Cubos \n9- Sair \n'))
    match opcao:
##Cálculo da sequência de Fibonacci
        case 1:
           print('Bem vindo ao calculo de Fibonacci. Para realizar esta sequência, digite dois valores inteiros e positivos, para serem os valores iniciais da sequência:\n')
           try:
                Valor1 = int(input('Digite o numero inicial: '))
                Valor2 = int(input('Digite o segundo numero: '))
                limite = int(input('Digite o limite: '))
                if limite < (Valor1 or Valor2):
                    print('Valor limite inválido! insira um valor limite maior do que os valores iniciais!')
                elif (Valor1 and Valor2) == 0:
                    print(f'Erro! você digitou {Valor1} nos dois valores, isso da uma sequência infinita!')
                else:
                    while Valor2 <= limite:
                        print(Valor1, Valor2, end=' ')
                        Valor1 = Valor1 + Valor2
                        Valor2 = Valor1 + Valor2
            except ValueError:
                print('Erro! Digite um número válido!')

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

