favoritos = []

def add_favorito():
    favorito_id = input("ID favorito: ")
    usuario_id = input("ID usuario: ")
    musica_id = input("ID musica: ")
    
    favoritos.append({
        'id': favorito_id,
        'usuario_id': usuario_id,
        'musica_id': musica_id,
        'data': 'hoje'
    })
    print("Musica favoritada!")

def ver_favoritos():
    for f in favoritos:
        print(f"ID: {f['id']}")
        print(f"Usuario: {f['usuario_id']}")
        print(f"Musica: {f['musica_id']}")
        print(f"Data: {f['data']}")
        print("-" * 20)

while True:
    print("\nMUSICAS FAVORITAS")
    print("1. Add favorito")
    print("2. Ver favoritos")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        add_favorito()
    elif op == "2":
        ver_favoritos()
    elif op == "3":
        break
    else:
        print("Invalido!")
