# Criar algoritmo que liste toda a sequência de Fibonacci até o número 100:

# Sequência dos centésimos primeiros números de Fibonacci
sequence_100th = [0, 1]
for i in range(2, 100):
    sequence_100th.append(sequence_100th[i-2] + sequence_100th[i-1])

print(sequence_100th)
print('---')

# Sequência dos números de Fibonacci menores ou iguais a 100
sequence_under_100 = [0, 1]
while True:
    next_fib = sequence_under_100[-2] + sequence_under_100[-1]
    if next_fib > 100:
        break
    sequence_under_100.append(next_fib)

print(sequence_under_100)
print('---')

# Criar algoritmo que faça a fatoração do número 1024. (Exemplo de fatoração: 6! = 6*5*4*3*2*1)

n = 1024
result = 1

while n > 1:
    result *= n-1
    n -= 1

print(result)
print('---')

# Criar uma lista de frutas (bananas, maçãs, peras, uvas, laranjas) e fazer um algoritmo para consultar se uma fruta existe na lista. 
# Caso não exista, adicionar a nova fruta. O programa só deve encerrar a brincadeira quando o usuário informar o número 999.

fruits = ['bananas', 'maçãs', 'peras', 'uvas', 'laranjas']

while True:

    print('Digite uma fruta para ver se ela está na lista, ou digite 999 para acabar.')
    user_input = str(input()).lower()

    if user_input == '999':
        print('Obrigado por jogar! A lista de frutas finais foi:')
        print(fruits)
        break
    elif user_input in fruits:
        print(f"A fruta {user_input} já está na lista!")
        print('')
    else:
        print(f"A fruta {user_input} não estava na lista! Adicionando ela agora...")
        fruits.append(user_input)
        print('')
