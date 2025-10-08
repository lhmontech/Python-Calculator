print('Hello! Welcome to the lhmontech calculator!')
N = 1
while N != 0:
    option = int(input('\nType which calculation you would like to perform: \n1- Fibonacci Sequence \n2- Tribonacci Sequence \n3- Geometric Sequence \n4- Factorial \n5- Perfect Squares \n6- Prime Numbers'
                       '\n7- Alternating Sequence \n8- Cubes \n9- Exit \n'))
    match option:
        ## Fibonacci Sequence Calculation
        case 1:
            print('Welcome to the Fibonacci calculation. To perform this sequence, enter two positive integers as the initial values of the sequence:\n')
            try:
                Value1 = int(input('Enter the first number: '))
                Value2 = int(input('Enter the second number: '))
                limit = int(input('Enter the limit: '))
                if limit < (Value1 or Value2):
                    print('Invalid limit! Enter a limit greater than the initial values!')
                elif Value1 == 0 and Value2 == 0:
                    print(f'Error! You entered {Value1} for both values, this creates an infinite sequence!')
                else:
                    while Value1 <= limit:
                        print(Value1, end=' ')
                        next = Value1 + Value2
                        Value1 = Value2
                        Value2 = next
            except ValueError:
                print('Error! Enter a valid number!')

        ## Tribonacci Sequence Calculation
        case 2:
            print('Welcome to the Tribonacci calculation. To perform this sequence, enter three positive integers as the initial values of the sequence:\n')
            try:
                Value1 = int(input('Enter the first number: '))
                Value2 = int(input('Enter the second number: '))
                Value3 = int(input('Enter the third number: '))
                limit = int(input('Enter the limit: '))
                if Value1 == 0 and Value2 == 0 and Value3 == 0:
                    print(f'Error! You entered {Value1} for all three values, this creates an infinite sequence!')
                elif limit < (Value1 or Value2 or Value3):
                    print('Invalid limit! Enter a limit greater than the initial values!')
                else:
                    while Value1 <= limit:
                        print(Value1, end=' ')
                        next = Value1 + Value2 + Value3
                        Value1 = Value2
                        Value2 = Value3
                        Value3 = next
            except ValueError:
                print('Error! Enter a valid number!')

        ## Geometric Sequence Calculation
        case 3:
            print('Welcome to the geometric sequence calculation. Enter the initial value and the ratio. The ratio cannot be -1, 0, or 1:')
            try:
                Value1 = int(input('Enter the initial number: '))
                Ratio = int(input('Enter the ratio: '))
                Value2 = int(input('Enter how many terms: '))
                if Ratio == 1 or Ratio == 0 or Ratio == -1:
                    print(f'Error! You entered {Ratio} as the ratio, this creates an infinite sequence!')
                else:
                    for i in range(Value1, Value2 + 1):
                        print(Value1, end=' ')
                        Value1 = Value1 * Ratio
            except ValueError:
                print('Error! Enter a valid number!')

        ## Factorial Calculation
        case 4:
            print('Welcome to the factorial calculation. Enter the number you want the factorial of:')
            try:
                Value1 = int(input('Enter the number: '))
                numbers = []
                result = 1
                for i in range(1, Value1 + 1):
                    result = result * i
                    numbers.append(i)
                print(*numbers, sep=' x ', end=' = ')
                print(result)
            except ValueError:
                print('Error! Enter a valid number!')

        ## Perfect Squares Calculation
        case 5:
            print('Welcome to the perfect squares calculation. Enter the initial and final values of the interval:')
            try:
                Value1 = int(input('Enter the initial number: '))
                Value2 = int(input('Enter the final number: '))
                if Value1 > Value2:
                    print('Invalid limit! Enter a limit greater than the initial value!')
                else:
                    print('The perfect squares within the interval you defined are:')
                    for i in range(Value1, Value2 + 1):
                        result = i**2
                        if (result >= Value1) and (result <= Value2):
                            print(f'{i} x {i} = {result}')
                        i += 1
            except ValueError:
                print('Error! Enter a valid number!')

        ## Prime Numbers Sequence
        case 6:
            print('Welcome to the prime numbers sequence calculation. Enter the initial number (greater than 1) and the final number of the interval:')
            try:
                Value1 = int(input('Enter the initial number: '))
                Value2 = int(input('Enter the final number: '))
                primes = []
                if Value1 > Value2:
                    print('Invalid limit! Enter a limit greater than the initial value!')
                else:
                    print('The prime numbers within the interval you defined are:')
                    for i in range(Value1, Value2 + 1):
                        is_prime = i > 1
                        for j in range(2, i-1):
                            if i % j == 0:
                                is_prime = False
                                break
                        if is_prime:
                            primes.append(i)
                    print(*primes, sep=', ', end=' ')
            except ValueError:
                print('Error! Enter a valid number!')

        ## Alternating Sequence
        case 7:
            print('Welcome to the alternating sequence calculation. Enter the initial and final values of the interval:')
            try:
                Value1 = int(input('Enter the initial number: '))
                Value2 = int(input('Enter how many terms: '))
                if Value1 > Value2:
                    print('Invalid limit! Enter a limit greater than the initial value!')
                else:
                    print('The alternating sequence within the interval you defined is:')
                    for i in range(Value1, Value2 + 1):
                        print(Value1, end=' ')
                        Value1 = Value1*2
                        Value1 = Value1*-1
            except ValueError:
                print('Error! Enter a valid number!')

        ## Cubes Sequence
        case 8:
            print('Welcome to the cubes calculation. Enter the initial and final values of the interval:')
            try:
                Value1 = int(input('Enter the initial number: '))
                Value2 = int(input('Enter the final number: '))
                if Value1 > Value2:
                    print('Invalid limit! Enter a limit greater than the initial value!')
                else:
                    print('The cubes within the interval you defined are:')
                    for i in range(Value1, Value2 + 1):
                        result = i**3
                        print(f'{i} x {i} x {i} = {result}')
                        i += 1
            except ValueError:
                print('Error! Enter a valid number!')

        ## Exit Option
        case 9:
            print('End of program!')
            N = 0

        ## Invalid Option
        case _:
            print('Error! Enter a valid option.')


