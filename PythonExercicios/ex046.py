import time
print('='*38)
print('CONTAGEM REGRESSIVA FOGOS DE ARTIFICIO')
print('='*38)
for c in range(10, -1, -1):
    time.sleep(1)
    print(c)
print('FIM')