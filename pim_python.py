import json, re, hashlib, os, sys, string, random
from prova_infraestrutura import prova_infra
from prova_programacao import prova_progr
from prova_ciberseguranca import prova_ciber

def senha_encode(senha):
    senha_hash = hashlib.sha256()
    senha_hash.update(senha.encode())
    return senha_hash.hexdigest()

def validar_email():
    while True:
            email = input("Digite seu e-mail: ")
            padrao_email = r"^\S+@\S+\.\S+$"
            
            for usuario in dados:
                if dados[usuario]["email"] == email:
                    print("Esse e-mail já pertence a outro usuário. Não gostaria de fazer seu log-in?")
                    raise Exception
                
            if re.match(padrao_email, email) == None:
                print("E-mail inválido!")
            else:
                return email
            
def validar_telefone():
    while True:
            telefone = int(input("Digite seu número de telefone (apenas números, com DDD, sem espaçamento): "))
            if len(str(telefone)) != 11:
                print("Número de telefone inválido!")            
            else:
                return telefone
            
def informacoes_pessoais():
    os.system('cls')
    print("Beleza! Vamos seguir com as perguntas.")
    
    # Opções de gênero
    print("\nQual o gênero pelo qual você se identifica?")
    print("1. Mulher")
    print("2. Homem")
    print("3. Não Binário")
    print("4. Prefiro não responder")
    genero_opcao = int(input("Digite o número correspondente: "))
    os.system('cls')
    if genero_opcao == 1:
        genero = "Mulher"
    elif genero_opcao == 2:
        genero = "Homem"
    elif genero_opcao == 3:
        genero = "Não binário"
    elif genero_opcao == 4:
        genero = None
    else:
        raise ValueError
    
    # Opções de cor/etnia
    print("\nQual a sua cor/etnia (de acordo com as classificações do IBGE)?")
    print("1. Branco")
    print("2. Pardo")
    print("3. Preto")
    print("4. Amarelo")
    print("5. Indígena")
    print("6. Prefiro não responder")
    etnia_opcao = int(input("Digite o número correspondente: "))
    os.system('cls')
    if etnia_opcao == 1:
        etnia = "Branco"
    elif etnia_opcao == 2:
        etnia = "Pardo"
    elif etnia_opcao == 3:
        etnia = "Preto"
    elif etnia_opcao == 4:
        etnia = "Amarelo"
    elif etnia_opcao == 5:
        etnia = "Indígena"
    elif etnia_opcao == 6:
        etnia = None
    else:
        raise ValueError

    # Opções de escolaridade
    print("\nQual o seu nível de escolaridade?")
    print("1. Ensino Fundamental incompleto")
    print("2. Ensino Fundamental completo")
    print("3. Ensino Médio incompleto")
    print("4. Ensino Médio completo")
    print("5. Ensino Superior incompleto")
    print("6. Ensino Superior completo")
    escolaridade_opcao = int(input("Digite o número correspondente: "))
    os.system('cls')
    if escolaridade_opcao == 1:
        escolaridade = "Ensino Fundamental incompleto"
    elif escolaridade_opcao == 2:
        escolaridade = "Ensino Fundamental completo"
    elif escolaridade_opcao == 3:
        escolaridade = "Ensino Médio incompleto"
    elif escolaridade_opcao == 4:
        escolaridade = "Ensino Médio completo"
    elif escolaridade_opcao == 5:
        escolaridade = "Ensino Superior incompleto"
    elif escolaridade_opcao == 6:
        escolaridade = "Ensino Superior completo"
    else:
        raise ValueError
    
    # Opções de renda
    
    print("\nQual a sua renda mensal individual?")
    print("1. Nenhuma")
    print("2. Até 2 salários mínimos")
    print("3. De 3 a 5 salários mínimos")
    print("4. De 5 a 8 salários mínimos")
    print("5. Superior a 8 salários mínimos")
    renda_opcao = int(input("Digite o número correspondente: "))
    os.system('cls')
    if renda_opcao == 1:
        renda = "Nenhuma"
    elif renda_opcao == 2:
        renda = "Até 2 salários mínimos"
    elif renda_opcao == 3:
        renda = "De 3 a 5 salários mínimos"
    elif renda_opcao == 4:
        renda = "De 5 a 8 salários mínimos"
    elif renda_opcao == 5:
        renda = "Superior a 8 salários mínimos"
    else:
        raise ValueError
    
    return genero, etnia, escolaridade, renda

caminho = os.path.join(os.path.dirname(__file__), "database.json")

try:
    # Abre arquivo e lê os dados que tem nele
    with open(caminho, "r", encoding='utf-8') as arquivo_leitura:
        dados = json.load(arquivo_leitura)
    os.system('cls')
    print("Dados carregados!")
except:
    # Se arquivo estiver vazio
    dados = {}
    os.system('cls')
    print("Não há dados cadastrados.")

try:
    # Opções da plataforma
    print("---------- CONECTA TECH ----------")
    print("Olá, bem vindo(a) à plataforma Conecta Tech! O que você deseja?")
    print("1. Cadastrar novo usuário")
    print("2. Fazer log-in")
    print("3. Sair")
    resposta = int(input("Digite a opção desejada: "))

    # CADASTRO DE USUÁRIO
    if resposta == 1:
        os.system('cls')
        # Pede informações do novo usuário
        print("\n---------- CADASTRO DE USUÁRIO ----------")
        print("Boa! Vamos cadastrar um novo usuário...")

        while True:
            id = f"{''.join(random.choices(string.ascii_letters.upper(),k=3))}{''.join(random.choices("0123456789",k=4))}"
            if id not in dados.keys():
                break

        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        # Checa se usuário é menor de idade
        if idade < 18:
            print("Você é muito novo para se cadastrar sozinho! Contate seu responsável.")
            raise Exception
        
        # Validação de e-mail
        email = validar_email()

        # Validação de telefone
        telefone = validar_telefone()

        # Criptografando a senha do usuário
        senha_input = input("Digite sua nova senha: ")
        senha = senha_encode(senha_input)

        # Pedido de informações socieconômicas com consentimento
        print("\nPerfeito! Agora precisamos de algumas informações socioeconômicas suas, para que possamos melhorar a experiência da plataforma.")

        consentimento = input("Você consente em compartilhar seus dados socioeconômicos com a plataforma Conecta Tech, para fins de análise e melhoria de serviço? (S / N) ")

        # Se houver consentimento
        if consentimento.lower() == "s" or consentimento.lower() == "sim":
            genero, etnia, escolaridade, renda = informacoes_pessoais()

        # Se não houver consentimento
        elif consentimento.lower() == "n":
            print("Sem problemas! Seguiremos com o seu cadastro sem essas informações.")
            genero = None
            etnia = None
            escolaridade = None
            renda = None

        else:
            raise ValueError
        
        # Cria um novo usuário, adicionando-o ao dicionário JSON
        user = {
            "nome": nome,
            "idade": idade,
            "email": email,
            "telefone": str(telefone),
            "senha": senha,
            "genero": genero,
            "etnia": etnia,
            "escolaridade": escolaridade,
            "renda": renda,
            "nota_infraestrutura": None,
            "nota_programacao": None,
            "nota_ciberseguranca": None
        }
        dados[id] = user
        with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
            json.dump(dados, arquivo_escrita, ensure_ascii=False)

        print("Usuário cadastrado com sucesso!")

    elif resposta == 2:
        # LOGANDO O USUÁRIO NA PLATAFORMA
        os.system('cls')
        print("\n---------- LOG-IN ----------")
        print("Boa! Vamos fazer seu log-in...")
        email_usuario = input("Digite o e-mail cadastrado: ")
        senha_usuario = input("Digite a sua senha: ")

        # Codificando senha inserida
        senha_usuario_hash = senha_encode(senha_usuario)

        # Comparando os dados com a database JSON
        for usuario in dados:
            # Se e-mail e senha estiverem corretos
            if dados[usuario]["email"] == email_usuario and dados[usuario]["senha"] == senha_usuario_hash:
                os.system('cls')
                print(f"----- {dados[usuario]["nome"]}, BEM VINDO(A)! -----")
                break

            # Se e-mail estiver correto, e senha estiver errada
            elif dados[usuario]["email"] == email_usuario and dados[usuario]["senha"] != senha_usuario_hash:
                print("Senha incorreta. Tente novamente!")
                raise Exception
                
            # Se o e-mail não for encontrado
            elif usuario == list(dados)[-1]:
                print("Não foi possível identificar seu usuário. Não se esqueça de fazer seu cadastro!")
                raise Exception
            
        # Quando usuário estiver logado:
        while True: 
            print("\nO que você gostaria de fazer?")
            print("1. Visualizar minhas informações")
            print("2. Atualizar minhas informações")
            print("3. Excluir meu usuário")
            print("4. Disciplinas")
            print("5. Sair")
            resposta_login = int(input("Digite a opção desejada: "))
            if resposta_login == 1:
                os.system('cls')
                print(f"----- USUÁRIO: {dados[usuario]["nome"]} -----")
                print(f"Email: {dados[usuario]["email"]}")
                print(f"Telefone: {dados[usuario]["telefone"]}")
                print(f"\n----- INFORMAÇÕES PESSOAIS -----")
                print(f"Gênero: {dados[usuario]["genero"]}")
                print(f"Etnia: {dados[usuario]["etnia"]}")
                print(f"Escolaridade: {dados[usuario]["escolaridade"]}")
                print(f"Renda: {dados[usuario]["renda"]}")
                print(f"----------------------------------------")
                continue

            elif resposta_login == 2:
                # Atualizar informações
                os.system('cls')
                print(f"----- ATUALIZANDO INFORMAÇÕES -----")
                print("\nQual informação você gostaria de atualizar?")
                print("1. E-mail")
                print("2. Telefone")
                print("3. Informações pessoais")
                print("4. Senha")
                print("5. Voltar")
                resposta_update = int(input("Digite a opção desejada: "))

                if resposta_update == 1:
                    # Novo e-mail
                    email_novo = validar_email()
                    dados[usuario]["email"] = email_novo
                    with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                        json.dump(dados, arquivo_escrita, ensure_ascii=False)
                    print("E-mail atualizado!")
                    continue

                elif resposta_update == 2:
                    # Novo telefone
                    telefone_novo = validar_telefone()
                    dados[usuario]["telefone"] = telefone_novo
                    with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                        json.dump(dados, arquivo_escrita, ensure_ascii=False)
                    print("Telefone atualizado!")
                    continue

                elif resposta_update == 3:
                    # Novas informações pessoais
                    genero_novo, etnia_nova, escolaridade_nova, renda_nova = informacoes_pessoais()
                    dados[usuario]["genero"] = genero_novo
                    dados[usuario]["etnia"] = etnia_nova
                    dados[usuario]["escolaridade"] = escolaridade_nova
                    dados[usuario]["renda"] = renda_nova
                    with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                        json.dump(dados, arquivo_escrita, ensure_ascii=False)
                    print("Informações pessoais atualizadas!")
                    continue

                elif resposta_update == 4:
                    # Nova senha
                    senha_atual = input("Confirme sua senha: ")
                    senha_atual_encode = senha_encode(senha_atual)
                    if senha_atual_encode != dados[usuario]["senha"]:
                        print("Senha inválida! Tente novamente.")
                        continue

                    senha_nova = input("Digite sua nova senha: ")
                    dados[usuario]["senha"] = senha_encode(senha_nova)
                    with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                        json.dump(dados, arquivo_escrita, ensure_ascii=False)
                    print("Senha atualizada!")
                    continue

                elif resposta_update == 5:
                    continue

                else:
                    raise ValueError

            elif resposta_login == 3:
                os.system('cls')
                print(f"----- EXCLUIR USUÁRIO -----")
                excluir_confirmar = input("Você tem certeza que deseja deletar seu usuário? Você perderá todo o seu progresso nas disciplinas! (S / N) ")
                if excluir_confirmar.lower() == "s" or excluir_confirmar.lower() == "sim":
                    del dados[usuario]
                    with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                        json.dump(dados, arquivo_escrita, ensure_ascii=False)
                    print("Usuário excluído, até mais!")
                    break
                else:
                    continue

            elif resposta_login == 4:
                os.system('cls')
                print(f"----- DISCIPLINAS -----")
                print("\nO que você gostaria de fazer?")
                print("1. Visualizar minhas notas")
                print("2. Fazer provas")
                print("3. Voltar")
                resposta_disciplinas = int(input("Digite a opção desejada: "))
                if resposta_disciplinas == 1:
                    os.system('cls')
                    print(f"----- DISCIPLINAS - NOTAS -----")
                    print(f"Infraestrutura computacional: {dados[usuario]["nota_infraestrutura"]}")
                    print(f"Programação e pensamento lógico: {dados[usuario]["nota_programacao"]}")
                    print(f"Cibersegurança: {dados[usuario]["nota_ciberseguranca"]}")
                    continue

                elif resposta_disciplinas == 2:
                    # Escolher qual prova fazer
                    print("\nQual prova você gostaria de acessar?")
                    print("1. Infraestrutura computacional")
                    print("2. Programação e pensamento lógico")
                    print("3. Cibersegurança")
                    print("4. Voltar")
                    resposta_provas = int(input("Digite a opção desejada: "))

                    if resposta_provas == 1:
                        # Se já houver uma nota registrada para a prova
                        if dados[usuario]["nota_infraestrutura"] != None:
                            os.system('cls')
                            print("Você já fez essa prova! Verifique sua nota em 'Visualizar minhas notas'")
                            continue
                        nota_infra = prova_infra()
                        dados[usuario]["nota_infraestrutura"] = nota_infra
                        with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                            json.dump(dados, arquivo_escrita, ensure_ascii=False)
                        os.system('cls')
                        print("Prova finalizada! Aguarde os resultados.")
                        continue

                    elif resposta_provas == 2:
                        if dados[usuario]["nota_programacao"] != None:
                            os.system('cls')
                            print("Você já fez essa prova! Verifique sua nota em 'Visualizar minhas notas'")
                            continue
                        nota_programa = prova_progr()
                        dados[usuario]["nota_programacao"] = nota_programa
                        with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                            json.dump(dados, arquivo_escrita, ensure_ascii=False)
                        os.system('cls')
                        print("Prova finalizada! Aguarde os resultados.")
                        continue

                    elif resposta_provas == 3:
                        if dados[usuario]["nota_ciberseguranca"] != None:
                            os.system('cls')
                            print("Você já fez essa prova! Verifique sua nota em 'Visualizar minhas notas'")
                            continue
                        nota_ciber = prova_ciber()
                        dados[usuario]["nota_ciberseguranca"] = nota_ciber
                        with open(caminho, "w", encoding='utf-8') as arquivo_escrita:
                            json.dump(dados, arquivo_escrita, ensure_ascii=False)
                        os.system('cls')
                        print("Prova finalizada! Aguarde os resultados.")
                        continue

                elif resposta_disciplinas == 3:
                    continue

            elif resposta_login == 5:
                print("\nSem problemas! Parando a execução...")
                break
            else:
                print("ERRO: Digite uma resposta válida!")

    else:
        print("\nSem problemas! Parando a execução...")
        sys.exit()

except ValueError:
    # Se idade não for um número inteiro
    print("Erro: digite uma resposta válida.")
except:
    # Se algo der errado durante o cadastro ou log-in
    print("Erro de processamento, tente novamente mais tarde.")