playlists = []

def criar_playlist():
    playlist_id = input("ID playlist: ")
    usuario_id = input("ID usuario: ")
    nome = input("Nome playlist: ")
    descricao = input("Descricao: ")
    
    print("Status:")
    print("1 - Publica")
    print("2 - Privada")
    status_op = input("Escolha (1/2): ")
    
    if status_op == "1":
        status = "Publica"
    else:
        status = "Privada"
    
    playlists.append({
        'id': playlist_id,
        'usuario_id': usuario_id,
        'nome': nome,
        'descricao': descricao,
        'criacao': 'hoje',
        'status': status
    })
    print("Playlist criada!")

def listar_playlists():
    for p in playlists:
        print(f"ID: {p['id']}")
        print(f"Usuario: {p['usuario_id']}")
        print(f"Nome: {p['nome']}")
        print(f"Descricao: {p['descricao']}")
        print(f"Criacao: {p['criacao']}")
        print(f"Status: {p['status']}")
        print("-" * 20)

while True:
    print("\nSISTEMA PLAYLISTS")
    print("1. Criar playlist")
    print("2. Listar playlists")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        criar_playlist()
    elif op == "2":
        listar_playlists()
    elif op == "3":
        break
    else:
        print("Invalido!")
