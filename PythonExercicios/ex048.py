import time
print('='*42)
print('Números ímpares de 1 a 50 e múltiplos de 3')
print('='*42)
for c in range (1, 501):
    if c % 3 == 0:
        print(c)
        time.sleep(0.1)
