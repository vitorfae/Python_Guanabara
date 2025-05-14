from django.template.defaultfilters import title

cidade = input('Digite o nome da sua cidade: ')
dividido = cidade.split()[0]
print(dividido)
dividido = dividido.lower()
print(dividido)
if 'santo' in dividido:
    print('Sim, ela começa com {}'.format(title(dividido)))
else:
    print('Não, ela não começa com {}'.format(title(dividido)))