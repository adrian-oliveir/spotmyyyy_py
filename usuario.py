usuarios = []

def cadastrar_usuario():
    usuario_id = input("ID usuario: ")
    nome = input("Nome: ")
    email = input("Email: ")
    senha = input("Senha: ")
    
    print("Tipo de conta:")
    print("1 - Ouvinte")
    print("2 - Artista") 
    print("3 - Produtor")
    tipo_op = input("Escolha (1/2/3): ")
    
    if tipo_op == "1":
        tipo = "Ouvinte"
    elif tipo_op == "2":
        tipo = "Artista"
    elif tipo_op == "3":
        tipo = "Produtor"
    else:
        tipo = "Ouvinte"
    
    foto = input("Foto perfil: ")
    
    print("Generos musicais:")
    print("1 - Rock")
    print("2 - Pop")
    print("3 - Eletronica")
    print("4 - Hip Hop")
    print("5 - Sertanejo")
    generos_op = input("Escolha (ex: 1,3,5): ")
    
    generos_map = {"1": "Rock", "2": "Pop", "3": "Eletronica", "4": "Hip Hop", "5": "Sertanejo"}
    generos = ", ".join([generos_map.get(g.strip(), "") for g in generos_op.split(",") if g.strip() in generos_map])
    
    usuarios.append({
        'id': usuario_id,
        'nome': nome,
        'email': email,
        'senha': senha,
        'tipo': tipo,
        'foto': foto,
        'generos': generos,
        'criacao': 'hoje',
        'login': 'agora'
    })
    print("Usuario cadastrado!")

def listar_usuarios():
    for u in usuarios:
        print(f"ID: {u['id']}")
        print(f"Nome: {u['nome']}")
        print(f"Email: {u['email']}")
        print(f"Tipo: {u['tipo']}")
        print(f"Generos: {u['generos']}")
        print(f"Criado: {u['criacao']}")
        print(f"Ultimo login: {u['login']}")
        print("-" * 20)

while True:
    print("\nMUSICFLOW - SISTEMA USUARIOS")
    print("1. Cadastrar usuario")
    print("2. Listar usuarios")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        cadastrar_usuario()
    elif op == "2":
        listar_usuarios()
    elif op == "3":
        break
    else:
        print("Invalido!")
