albuns = []

def add_album():
    album_id = input("ID album: ")
    artista_id = input("ID artista: ")
    titulo = input("Titulo: ")
    ano = input("Ano lancamento: ")
    
    print("Genero:")
    print("1 - Rock")
    print("2 - Pop")
    print("3 - Eletronica")
    print("4 - Hip Hop")
    print("5 - Sertanejo")
    genero_op = input("Escolha (1-5): ")
    
    genero_map = {"1": "Rock", "2": "Pop", "3": "Eletronica", "4": "Hip Hop", "5": "Sertanejo"}
    genero = genero_map.get(genero_op, "Pop")
    
    capa = input("Capa album: ")
    
    albuns.append({
        'id': album_id,
        'artista_id': artista_id,
        'titulo': titulo,
        'ano': ano,
        'genero': genero,
        'capa': capa
    })
    print("Album adicionado!")

def ver_albuns():
    for a in albuns:
        print(f"ID: {a['id']}")
        print(f"Artista: {a['artista_id']}")
        print(f"Titulo: {a['titulo']}")
        print(f"Ano: {a['ano']}")
        print(f"Genero: {a['genero']}")
        print(f"Capa: {a['capa']}")
        print("-" * 20)

while True:
    print("\nSISTEMA DE ALBUNS")
    print("1. Add album")
    print("2. Ver albuns")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        add_album()
    elif op == "2":
        ver_albuns()
    elif op == "3":
        break
    else:
        print("Invalido!")
