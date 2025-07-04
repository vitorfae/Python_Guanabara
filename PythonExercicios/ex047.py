import time
print('='*23)
print('Números pares de 1 a 50')
print('='*23)
for c in range(1, 51):
    if c % 2 == 0:
        print(c)
        time.sleep(0.3)
