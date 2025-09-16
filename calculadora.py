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
                elif Valor1 == 0 and Valor2 == 0:
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
            print('Bem vindo ao calculo de Tribonacci. Para realizar esta sequência, digite três valores inteiros e positivos, para serem os valores iniciais da sequência:\n')
            try:
                Valor1 = int(input('Digite o numero inicial: '))
                Valor2 = int(input('Digite o segundo numero: '))
                Valor3 = int(input('Digite o terceiro numero: '))
                limite = int(input('Digite o limite: '))
                if Valor1 == 0 and Valor2 == 0 and Valor3 == 0:
                    print(f'Erro! você digitou {Valor1} nos três valores, isso da uma sequência infinita!')
                elif limite < (Valor1 or Valor2 or Valor3):
                    print('Valor limite inválido! insira um valor limite maior do que os valores iniciais!')
                else:
                    while Valor2 <= limite:
                        print(Valor1, Valor2, Valor3, end=' ')
                        Valor1 = Valor1 + Valor2 + Valor3
                        Valor2 = Valor1 + Valor2 + Valor3
                        Valor3 = Valor1 + Valor2 + Valor3
            except ValueError:
                print('Erro! Digite um número válido!')
##Cálculo para a sequência geométrica
        case 3:
            print('Bem vindo ao calculo da sequência geométrica. Para realizar esta sequência, digite o valor inicial e qual número será a razão, não podendo a razão ser -1, 0 ou 1:')
            try:
                Valor1 = int(input('Digite o número inicial: '))
                Razao = int(input('Digite o número da razão: '))
                limite = int(input('Digite o limite: '))
                if Razao == 1 or Razao == 0 or Razao == -1:
                    print(f'Erro! você digitou {Razao} na razão, isso da uma sequência infinita!')
                else:
                    while Valor1 <= limite:
                        print(Valor1, end=' ')
                        Valor1 = Valor1 * Razao
            except ValueError:
                print('Erro! Digite um número valido!')
##Cálculo do número fatorial
        case 4:
            print('Bem vindo ao calculo da fatorial. Para realizar esta calculo, digite qual número você gostaria de saber o fatorial:')
            try:
                Valor1 = int(input('Digite o numero: '))
                lista = []
                resultado = 1
                for i in range(1, Valor1 + 1):
                    resultado = resultado * i
                    lista.append(i)
                print(*lista, sep=' x ', end=' = ')
                print(resultado)
            except ValueError:
                print('Erro! Digite um número valido!')
#Cálculo dos quadrados perfeitos
        case 5:
            print('Bem vindo ao calculo dos quadrados perfeitos, digite o valor inicial e final do intervalo que gostaria.')
            try:
                Valor1 = int(input('Digite o número inicial: '))
                Valor2 = int(input('Digite o número final: '))
                if Valor1 > Valor2:
                    print('Valor limite inválido! insira um valor limite maior do que o valor inicial!')
                else:
                    print('Os quadrados perfeitos dentro do intervalo que você definiu são os seguintes:')
                    for i in range(Valor1, Valor2 + 1):
                        resultado = i**2
                        print(f'{i} x {i} = {resultado}')
                        i += 1
            except ValueError:
                print('Erro! Digite um valor valido!')
##Sequência de numeros primos
        case 6:
            print('Bem vindo ao calculo da sequência de numeros primos, digite o valor inicial maior que 1 e o valor final do intervalo que gostaria.')
            try:
                Valor1 = int(input('Digite o número inicial: '))
                Valor2 = int(input('Digite o número final: '))
                lista = []
                if Valor1 > Valor2:
                    print('Valor limite inválido! insira um valor limite maior do que o valore inicial!')
                else:
                    print('Os números primos dentro do intervalo que você definiu são os seguintes:')
                    for i in range(Valor1, Valor2 + 1):
                        nr_primo = i > 1
                        for j in range(2, i-1):
                            if i%j == 0:
                                nr_primo = False
                                break
                        if nr_primo == True:
                            lista.append(i)
                    print(*lista, sep=', ', end=' ')
            except ValueError:
                print('Erro! Digite um valor valido!')
##Sequência alternada
        case 7:
            print('Bem vindo ao calculo da sequência alternada, digite valor inicial e final do intervalo que gostaria.')
            try:
                Valor1 = int(input('Digite o número inicial: '))
                Valor2 = int(input('Digite o número final: '))
                if Valor1 > Valor2:
                    print('Valor limite inválido! insira um valor limite maior do que o valore inicial!')
                else:
                    print('A sequência alternada dentro do intervalo que você definiu é a seguinte:')
                    for i in range(Valor1, Valor2 + 1):
                        print(Valor1, end=' ')
                        Valor1 = Valor1*2
                        Valor1 = Valor1*-1

            except ValueError:
                print('Erro! Digite um valor valido!')

##Sequência de cubos
        case 8:
            print('Bem vindo ao calculo dos cubos, digite o valor inicial e final do intervalo que gostaria.')
            try:
                Valor1 = int(input('Digite o número inicial: '))
                Valor2 = int(input('Digite o número final: '))
                if Valor1 > Valor2:
                    print('Valor limite inválido! insira um valor limite maior do que o valore inicial!')
                else:
                    print('Os cubos dentro do intervalo que você definiu são os seguintes:')
                    for i in range(Valor1, Valor2 + 1):
                        resultado = i**3
                        print(f'{i} x {i} x {i} = {resultado}')
                        i += 1
            except ValueError:
                print('Erro! Digite um valor valido!')
##Opção de saída
        case 9:
            print('Fim do programa!')
            N = 0
##Opção para caso o usuário digite um valor fora das opções válidas
        case _:
            print('Erro! Digite um valor válido.')

