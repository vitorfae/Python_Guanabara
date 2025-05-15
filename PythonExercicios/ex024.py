from django.template.defaultfilters import title

cidade = input('Digite o nome da sua cidade: ')
dividido = cidade.split()[0]
dividido = dividido.lower()
if 'santo' in dividido:
    print('Sim, ela começa com Santo que é {}'.format(title(dividido)))
else:
    print('Não, ela não começa com Santo')