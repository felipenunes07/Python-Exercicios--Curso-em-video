print('='*30)
print(' 10 TERMOS DE UMA PA')
print('='*30)
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
for c in range(1,11):
    print(primeiro+(razao*(c-1)),end='->')
print('Acabou')

   # an = a1+(r*(n-1))