from ex111.utilidadesCeV import moeda
from ex111.utilidadesCeV import dado

preco = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(preco, 35, 22)