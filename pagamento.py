pagamentos = []

def cadastrar():
    usuario = input("ID usuario: ")
    
    print("Assinaturas disponíveis:")
    print("1 - Basic R$ 10,00")
    print("2 - Standard R$ 30,00") 
    print("3 - Premium R$ 50,00")
    
    opcao_assinatura = input("Escolha a assinatura (1/2/3): ")
    
    if opcao_assinatura == "1":
        assinatura = "Basic"
        valor = "10,00"
    elif opcao_assinatura == "2":
        assinatura = "Standard" 
        valor = "30,00"
    elif opcao_assinatura == "3":
        assinatura = "Premium"
        valor = "50,00"
    else:
        print("Opção inválida! Usando Basic.")
        assinatura = "Basic"
        valor = "10,00"
    
    metodo = input("Metodo pagamento: ")
    cpf = input("CPF: ")
    
    pagamentos.append({
        'usuario': usuario,
        'assinatura': assinatura,
        'metodo': metodo,
        'valor': valor,
        'cpf': cpf
    })
    print("Cadastrado!")

def listar():
    for p in pagamentos:
        print(f"Usuario: {p['usuario']}")
        print(f"Assinatura: {p['assinatura']}")
        print(f"Metodo: {p['metodo']}")
        print(f"Valor: R$ {p['valor']}")
        cpf_limpo = p['cpf'].replace('.', '').replace('-', '')
        print(f"CPF: {cpf_limpo}")
        print("-" * 20)

while True:
    print("\n1. Cadastrar pagamento")
    print("2. Listar pagamentos") 
    print("3. Sair")
    opcao = input("Opcao: ")
    
    if opcao == "1":
        cadastrar()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        break
    else:
        print("Opcao invalida!")
