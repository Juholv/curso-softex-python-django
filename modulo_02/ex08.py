acesso = [('pedro', 'sucesso'),
          ('ana', 'falha'),
          ('maria', 'sucesso'),
          ('pedro', 'falha'),
          ('ana', 'falha'),
          ]
usuario_aceito = set()
usuario_falha = set()

for usuario, status in acesso:
    if status == "sucesso":
        usuario_aceito.add(usuario)

    else:
        usuario_falha.add(usuario)

    falha = usuario_falha.difference(usuario_aceito)

print(f"os usuarios com falhas sao {falha} e os aceitos sao {usuario_aceito}")

      

