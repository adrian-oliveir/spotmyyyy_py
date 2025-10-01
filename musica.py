musicas = []

def add_musica():
    musica_id = input("ID musica: ")
    album_id = input("ID album: ")
    titulo = input("Titulo: ")
    duracao = input("Duracao (ex: 3:45): ")
    
    print("Genero:")
    print("1 - Rock")
    print("2 - Pop")
    print("3 - Eletronica")
    print("4 - Hip Hop")
    print("5 - Sertanejo")
    genero_op = input("Escolha (1-5): ")
    
    genero_map = {"1": "Rock", "2": "Pop", "3": "Eletronica", "4": "Hip Hop", "5": "Sertanejo"}
    genero = genero_map.get(genero_op, "Pop")
    
    musicas.append({
        'id': musica_id,
        'album_id': album_id,
        'titulo': titulo,
        'duracao': duracao,
        'genero': genero,
        'data': 'hoje'
    })
    print("Musica adicionada!")

def ver_musicas():
    for m in musicas:
        print(f"ID: {m['id']}")
        print(f"Album: {m['album_id']}")
        print(f"Titulo: {m['titulo']}")
        print(f"Duracao: {m['duracao']}")
        print(f"Genero: {m['genero']}")
        print(f"Data: {m['data']}")
        print("-" * 20)

while True:
    print("\nSISTEMA DE MUSICAS")
    print("1. Add musica")
    print("2. Ver musicas")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        add_musica()
    elif op == "2":
        ver_musicas()
    elif op == "3":
        break
    else:
        print("Invalido!")
