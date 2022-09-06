from time import sleep

# "LOGOTIPO DO SISTEMA"
print('-*-' * 18)
print('-*-' * 18)
print('*' * 19 + ' CINEMA PYTHON ' + '*' * 20)
print('-*-' * 18)
print('-*-' * 18)
print('ABRINDO SISTEMA AGUARDE...')
# USANDO O TIME PARA "CARREGAR O SISTEMA"
sleep(2)
# INSERÇÃO DEDADOS NO ISTEMA
nome = str(input('Digite Seu Nome:'))
i = int(input('Digite Sua idade: '))
# CONDIÇÃO PARA ENTRADA DE MAIOR OU MENOR IDADE
if i <= 18:
    print('Sua idade não é permitida para acessar a taréfa !')
else:
    s = str(input('Usuário maior de idade, Continuar no processo ? SIM ou NAO :'))
    # OPÇÃO DE ENTRADA E INFORMAÇÕES DE VALORES
    if s != 'NAO':
        print('-*-' * 18)
        print('-*-' * 18)
        print('\033[31mValores de ingresso :\033[m')
        print('\033[7;32m1 - Adulto 25 Reais\033[m')
        print('\033[7;36m2 - Criança 10 Reais\033[m')
        print('\033[7;34m3 - Estudante 15 Reais\033[m')
        print('Qual é a forma de ingresso de 1 ao 3')
        print('-*-' * 18)
        print('-*-' * 18)
        # ESCOLHENDO AS OPÇÕES APRESENTADAS
        a = int(input('Insira o código de entrada:'))
        # CONDIÇÃO PARA CADA OPÇÃO ESCOLHIDA
        if a == 1:
            d = int(input('Qual dinheiro recebido ?'))
            if d < 25:
                print('\033[31mValor inferior\033[m, Favor reiniciar a operação com o valor correto!')
            else:
                v = d - 25
                print('Troco do ingresso é de : {} Reais, Ingresso liberado divirta-se'.format(v))
        elif a == 2:
            d = int(input('Qual dinheiro recebido ?'))
            if d < 10:
                print('\033[31mValor inferior\033[m, Favor reiniciar a operação com o valor correto!')
            else:
                v = d - 10
                print('Troco do ingresso é de : {} Reais, Ingresso liberado divirta-se'.format(v))
        elif a == 3:
            d = int(input('Qual dinheiro recebido ?'))
            if d < 15:
                print('\033[31mValor inferior\033[m, Favor reiniciar a operação com o valor correto!')
            else:
                v = d - 15
                print('Troco do ingresso é de : {} Reais, Ingresso liberado divirta-se'.format(v))
        # CASO NÃO INSIRA UM CÓDIGO VÁLIDO, SISTEMA SE ENCERRA
        else:
            print('Código nao encontrado, reinicie a operação')
    else:
        print('Saindo do Sistema!')
