'''tuplas e conjuntos
lista em cinjunto coloca set'''

vendas = [('celular',1000,2), ("fone",50,10), ('carregador',150,5)] #celular 1000 reais 2 unidades

vendas_filtradas = []
unicos = set()


for nome, valor,quantidade in vendas:

    total = quantidade * valor
if total >=100:
    vendas_filtradas.append((nome, valor,quantidade))

unicos.add(nome)

print("Vendas filtradas (valor total >= 100):")
print(vendas_filtradas)
print("\nProdutos únicos:")
print(unicos)