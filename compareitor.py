from random import randrange, choice

TURNOS = 10
OPERADORES = ['==', '!=', '<', '>', '<=', '>=']

print('%' * 20, 'COMPAREITOR TABAJARA', '%' * 20)

acertos = 0

for i in range(TURNOS):
    a = randrange(10)
    b = randrange(10)
    op = choice(OPERADORES)
    expressao = '%s %s %s' % (a, op, b)
    print('_' * 50, 'questão', i+1)
    print('a =', a)
    print('b =', b)
    pergunta = 'a {} b\t\t(s/n)? '.format(op)
    resposta = input(pergunta)
    resposta = resposta == 's'
    if eval(expressao) == resposta:
        print('\t\t\tcerto!')
        acertos += 1
    else:
        print('\t\t\terrado...')

print('%' * 62)
porcentagem = acertos / TURNOS * 100
mensagem = 'acertos (%.1f%%)' % porcentagem
print('RESULTADO:\t', acertos, mensagem)
print('%' * 62)
