avaliacoes = []

def add_avaliacao():
    avaliacao_id = input("ID avaliacao: ")
    usuario_id = input("ID usuario: ")
    musica_id = input("ID musica: ")
    
    print("Nota (1-5):")
    print("1 - ★")
    print("2 - ★★") 
    print("3 - ★★★")
    print("4 - ★★★★")
    print("5 - ★★★★★")
    nota_op = input("Escolha (1-5): ")
    
    nota_map = {"1": "★", "2": "★★", "3": "★★★", "4": "★★★★", "5": "★★★★★"}
    nota = nota_map.get(nota_op, "★★★")
    
    comentario = input("Comentario: ")
    
    avaliacoes.append({
        'id': avaliacao_id,
        'usuario_id': usuario_id,
        'musica_id': musica_id,
        'nota': nota,
        'comentario': comentario,
        'data': 'hoje'
    })
    print("Avaliacao adicionada!")

def ver_avaliacoes():
    for a in avaliacoes:
        print(f"ID: {a['id']}")
        print(f"Usuario: {a['usuario_id']}")
        print(f"Musica: {a['musica_id']}")
        print(f"Nota: {a['nota']}")
        print(f"Comentario: {a['comentario']}")
        print(f"Data: {a['data']}")
        print("-" * 20)

while True:
    print("\nAVALIACOES DE MUSICAS")
    print("1. Add avaliacao")
    print("2. Ver avaliacoes")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        add_avaliacao()
    elif op == "2":
        ver_avaliacoes()
    elif op == "3":
        break
    else:
        print("Invalido!")
