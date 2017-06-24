ana = float(input('Quanto gastou Ana? '))
bia = float(input('Quanto gastou Bia? '))
total = ana + bia
print('Total: R$', total)
por_pessoa = total / 2
saldo_ana = ana - por_pessoa
saldo_bia = bia - por_pessoa
print('Saldo de Ana: R$', saldo_ana)
print('Saldo de Bia: R$', saldo_bia)
