from random import randrange, choice

TURNOS = 6
OPERADORES = ['==', '!=', '<', '>', '<=', '>=']

print('%' * 20, 'COMPAREITOR TABAJARA', '%' * 20)

acertos = 0

for i in range(TURNOS):
    a = randrange(10)
    b = randrange(10)
    op = choice(OPERADORES)
    expressao = str(a) + ' ' + op + ' ' + str(b)
    print('_' * 50, 'questão', i+1)
    print('a =', a)
    print('b =', b)
    pergunta = 'a ' + op + ' b\t\t(s/n)? '
    resposta = input(pergunta)
    resposta = resposta == 's'
    if eval(expressao) == resposta:
        print('\t\t\tcerto!')
        acertos = acertos + 1
    else:
        print('\t\t\terrado...')

print('%' * 62)
porcentagem = acertos / TURNOS * 100
mensagem = 'acertos (%.1f)' % porcentagem + '%'
print('RESULTADO:\t', acertos, mensagem)
print('%' * 62)
if porcentagem == 100:
    print('Parabéns, você acertou todas!!!')
elif porcentagem > 50:
    print('Acertou mais da metade, continue praticando.')
elif porcentagem == 0:
    print('Você sabe tudo, mas tá de sacanagem.')
else:
    print('Você precisa praticar mais.')
