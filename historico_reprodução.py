historico = []

def add_historico():
    historico_id = input("ID historico: ")
    usuario_id = input("ID usuario: ")
    musica_id = input("ID musica: ")
    dispositivo = input("Dispositivo: ")
    
    historico.append({
        'id': historico_id,
        'usuario_id': usuario_id,
        'musica_id': musica_id,
        'data': 'agora',
        'dispositivo': dispositivo
    })
    print("Historico adicionado!")

def ver_historico():
    for h in historico:
        print(f"ID: {h['id']}")
        print(f"Usuario: {h['usuario_id']}")
        print(f"Musica: {h['musica_id']}")
        print(f"Data: {h['data']}")
        print(f"Dispositivo: {h['dispositivo']}")
        print("-" * 20)

while True:
    print("\nHISTORICO DE MUSICAS")
    print("1. Add historico")
    print("2. Ver historico")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        add_historico()
    elif op == "2":
        ver_historico()
    elif op == "3":
        break
    else:
        print("Invalido!")
