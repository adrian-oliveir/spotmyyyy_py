assinaturas = []

def add_assinatura():
    assinatura_id = input("ID assinatura: ")
    usuario_id = input("ID usuario: ")
    
    print("Plano:")
    print("1 - Basico R$ 10,00")
    print("2 - avançado R$ 30,00")
    print("3 - Premium R$ 50,00")
    plano_op = input("Escolha (1-3): ")
    
    if plano_op == "1":
        plano = "Basico"
        preco = "10,00"
    elif plano_op == "2":
        plano = "avançado"
        preco = "30,00"
    elif plano_op == "3":
        plano = "Premium"
        preco = "50,00"
    else:
        plano = "Basico"
        preco = "10,00"
    
    print("Status:")
    print("1 - Ativa")
    print("2 - Inativa")
    status_op = input("Escolha (1-2): ")
    
    status = "Ativa" if status_op == "1" else "Inativa"
    
    data_inicio = input("Data inicio: ")
    data_fim = input("Data fim: ")
    
    assinaturas.append({
        'id': assinatura_id,
        'usuario_id': usuario_id,
        'plano': plano,
        'preco': preco,
        'status': status,
        'inicio': data_inicio,
        'fim': data_fim
    })
    print("Assinatura adicionada!")

def ver_assinaturas():
    for a in assinaturas:
        print(f"ID: {a['id']}")
        print(f"Usuario: {a['usuario_id']}")
        print(f"Plano: {a['plano']}")
        print(f"Preco: R$ {a['preco']}")
        print(f"Status: {a['status']}")
        print(f"Inicio: {a['inicio']}")
        print(f"Fim: {a['fim']}")
        print("-" * 20)

while True:
    print("\nSISTEMA DE ASSINATURAS")
    print("1. Add assinatura")
    print("2. Ver assinaturas")
    print("3. Sair")
    
    op = input("Opcao: ")
    
    if op == "1":
        add_assinatura()
    elif op == "2":
        ver_assinaturas()
    elif op == "3":
        break
    else:
        print("Invalido!")
