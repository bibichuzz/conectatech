import os

def prova_progr():
    nota = 0

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n1) Qual é o tipo de dado retornado pela expressão: type(3.14)?\n")
    print(f"a) int")
    print(f"b) str")
    print(f"c) float")
    print(f"d) bool")
    resposta1 = input("Digite a alternativa: ").lower()
    if resposta1 == "c":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n2) Qual é a função de uma estrutura 'if' em Python?\n")
    print(f"a) Executar um bloco de código várias vezes")
    print(f"b) Definir variáveis globais")
    print(f"c) Verificar uma condição e executar um bloco de código se ela for verdadeira")
    print(f"d) Criar uma nova função")
    resposta2 = input("Digite a alternativa: ").lower()
    if resposta2 == "c":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n3) O que o código abaixo imprime?\n\nfor i in range(3):\n    print(i)\n")
    print(f"a) 1 2 3")
    print(f"b) 0 1 2")
    print(f"c) 0 1 2 3")
    print(f"d) 1 2")
    resposta3 = input("Digite a alternativa: ").lower()
    if resposta3 == "b":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n4) Qual a principal diferença entre listas e tuplas em Python?\n")
    print(f"a) Listas não podem conter strings, tuplas podem")
    print(f"b) Tuplas são mutáveis, listas não")
    print(f"c) Listas são mutáveis, tuplas não")
    print(f"d) Ambas são mutáveis")
    resposta4 = input("Digite a alternativa: ").lower()
    if resposta4 == "c":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n5) Qual é a saída do código: print(10 > 5 and 3 < 1)?\n")
    print(f"a) True")
    print(f"b) False")
    print(f"c) 10 > 5")
    print(f"d) 3 < 1")
    resposta5 = input("Digite a alternativa: ").lower()
    if resposta5 == "b":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n6) Qual é a forma correta de definir uma função em Python?\n")
    print(f"a) function minhaFuncao():")
    print(f"b) def minhaFuncao:")
    print(f"c) def minhaFuncao():")
    print(f"d) define minhaFuncao():")
    resposta6 = input("Digite a alternativa: ").lower()
    if resposta6 == "c":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n7) Em Python, o que o método append() faz em uma lista?\n")
    print(f"a) Remove o último item")
    print(f"b) Adiciona um item ao final")
    print(f"c) Ordena os itens")
    print(f"d) Apaga todos os itens")
    resposta7 = input("Digite a alternativa: ").lower()
    if resposta7 == "b":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n8) Qual estrutura é usada para repetir um bloco de código até que uma condição se torne falsa?\n")
    print(f"a) for")
    print(f"b) if")
    print(f"c) def")
    print(f"d) while")
    resposta8 = input("Digite a alternativa: ").lower()
    if resposta8 == "d":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n9) Qual é a sintaxe correta para acessar o valor associado à chave 'nome' em um dicionário chamado aluno?\n")
    print(f"a) aluno.nome")
    print(f"b) aluno{'nome'}")
    print(f"c) aluno['nome']")
    print(f"d) aluno(nome)")
    resposta9 = input("Digite a alternativa: ").lower()
    if resposta9 == "c":
        nota += 1

    os.system('cls')
    print(f"----- PROGRAMAÇÃO E PENSAMENTO LÓGICO -----")
    print(f"\n10) Qual dos seguintes é um operador lógico em Python?\n")
    print(f"a) plus")
    print(f"b) &&")
    print(f"c) and")
    print(f"d) ==")
    resposta10 = input("Digite a alternativa: ").lower()
    if resposta10 == "c":
        nota += 1

    os.system('cls')
    return nota
