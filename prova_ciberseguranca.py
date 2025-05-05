import os

def prova_ciber():
    nota = 0

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n1) O que é ransomware?\n")
    print(f"a) Um antivírus gratuito")
    print(f"b) Um software de backup automático")
    print(f"c) Um tipo de ataque que sequestra dados e exige pagamento para liberá-los")
    print(f"d) Um protocolo de segurança de rede")
    resposta1 = input("Digite a alternativa: ").lower()
    if resposta1 == "c":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n2) Qual das opções a seguir é uma boa prática de segurança digital?\n")
    print(f"a) Usar a mesma senha em todos os sites")
    print(f"b) Compartilhar senhas com colegas de confiança")
    print(f"c) Atualizar senhas regularmente e usar autenticação de dois fatores")
    print(f"d) Anotar senhas em um post-it e colar no monitor")
    resposta2 = input("Digite a alternativa: ").lower()
    if resposta2 == "c":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n3) O que é a LGPD?\n")
    print(f"a) Um antivírus brasileiro")
    print(f"b) Uma lei que trata da proteção de dados pessoais no Brasil")
    print(f"c) Um tipo de ataque digital via rede")
    print(f"d) Um software de firewall")
    resposta3 = input("Digite a alternativa: ").lower()
    if resposta3 == "b":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n4) O que caracteriza um vírus de computador?\n")
    print(f"a) Um arquivo grande demais para a RAM")
    print(f"b) Um programa malicioso que se replica e infecta outros arquivos")
    print(f"c) Um sistema operacional alternativo")
    print(f"d) Uma falha de hardware")
    resposta4 = input("Digite a alternativa: ").lower()
    if resposta4 == "b":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n5) Qual é o papel da ANPD?\n")
    print(f"a) Desenvolver sistemas operacionais seguros")
    print(f"b) Monitorar redes Wi-Fi públicas")
    print(f"c) Fiscalizar e regulamentar o cumprimento da LGPD no Brasil")
    print(f"d) Criar programas antivírus para o governo")
    resposta5 = input("Digite a alternativa: ").lower()
    if resposta5 == "c":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n6) Qual senha abaixo é considerada forte?\n")
    print(f"a) 123456")
    print(f"b) senha123")
    print(f"c) Maria2024")
    print(f"d) Xz!9@q#L7m")
    resposta6 = input("Digite a alternativa: ").lower()
    if resposta6 == "d":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n7) O que é criptografia?\n")
    print(f"a) Um tipo de malware usado para invadir servidores")
    print(f"b) Um recurso para apagar arquivos automaticamente")
    print(f"c) Um processo de codificação de dados para protegê-los contra acesso não autorizado")
    print(f"d) Um antivírus de código aberto")
    resposta7 = input("Digite a alternativa: ").lower()
    if resposta7 == "c":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n8) Por que é importante fazer backups?\n")
    print(f"a) Para liberar espaço no disco rígido")
    print(f"b) Para evitar que o computador trave")
    print(f"c) Para restaurar dados em caso de perda ou ataque cibernético")
    print(f"d) Para manter os arquivos organizados por ordem alfabética")
    resposta8 = input("Digite a alternativa: ").lower()
    if resposta8 == "c":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n9) O que é um ataque de phishing?\n")
    print(f"a) Uma tentativa de acessar arquivos locais via terminal")
    print(f"b) Um tipo de ataque físico ao servidor")
    print(f"c) Uma técnica de engenharia social para enganar usuários e obter informações confidenciais")
    print(f"d) Um processo de criptografia reversa")
    resposta9 = input("Digite a alternativa: ").lower()
    if resposta9 == "c":
        nota += 1

    os.system('cls')
    print(f"----- CIBERSEGURANÇA -----")
    print(f"\n10) Qual das opções abaixo ajuda a proteger dispositivos conectados à internet?\n")
    print(f"a) Desativar o Wi-Fi")
    print(f"b) Instalar software pirata")
    print(f"c) Manter o sistema operacional e os programas atualizados")
    print(f"d) Utilizar apenas redes públicas")
    resposta10 = input("Digite a alternativa: ").lower()
    if resposta10 == "c":
        nota += 1

    os.system('cls')
    return nota
