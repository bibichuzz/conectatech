import os

def prova_infra():
    nota = 0

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n1) O que é um processo em um sistema operacional?\n")
    print(f"a) Um tipo de memória de acesso rápido")
    print(f"b) Um algoritmo de ordenação")
    print(f"c) Um programa em execução")
    print(f"d) Um componente físico do processador")
    resposta1 = input("Digite a alternativa: ").lower()
    if resposta1 == "c":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n2) Para que servem os semáforos em sistemas operacionais?\n")
    print(f"a) Controlar o acesso concorrente a recursos compartilhados")
    print(f"b) Enviar sinais elétricos à memória")
    print(f"c) Organizar a ordem de arquivos no disco")
    print(f"d) Sincronizar relógios do sistema")
    resposta2 = input("Digite a alternativa: ").lower()
    if resposta2 == "a":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n3) O que é uma thread?\n")
    print(f"a) Um tipo de arquivo executável")
    print(f"b) Uma subunidade de execução dentro de um processo")
    print(f"c) Um endereço IP dinâmico")
    print(f"d) Um tipo de instrução lógica")
    resposta3 = input("Digite a alternativa: ").lower()
    if resposta3 == "b":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n4) Qual a função dos registradores em um processador?\n")
    print(f"a) Controlar a interface gráfica")
    print(f"b) Gerenciar os dispositivos de entrada")
    print(f"c) Armazenar temporariamente dados e instruções em execução")
    print(f"d) Armazenar programas permanentemente")
    resposta4 = input("Digite a alternativa: ").lower()
    if resposta4 == "c":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n5) O que representa o ponteiro de pilha (stack pointer)?\n")
    print(f"a) Endereço da última célula de memória usada pela RAM")
    print(f"b) Posição atual de execução da CPU")
    print(f"c) Endereço do topo da pilha na memória")
    print(f"d) Local onde o sistema armazena arquivos temporários")
    resposta5 = input("Digite a alternativa: ").lower()
    if resposta5 == "c":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n6) Em relação à memória RAM, qual das opções é correta?\n")
    print(f"a) É usada apenas durante o boot do sistema")
    print(f"b) É uma memória volátil usada para armazenar dados temporários")
    print(f"c) É mais lenta que o HD e usada para backup")
    print(f"d) Armazena o sistema operacional permanentemente")
    resposta6 = input("Digite a alternativa: ").lower()
    if resposta6 == "b":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n7) O que são portas lógicas?\n")
    print(f"a) Conexões de rede usadas para acessar a internet")
    print(f"b) Ferramentas de segurança de software")
    print(f"c) Componentes que realizam operações booleanas no hardware")
    print(f"d) Tipos de memória virtual")
    resposta7 = input("Digite a alternativa: ").lower()
    if resposta7 == "c":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n8) O que é escalonamento de processos?\n")
    print(f"a) Uma técnica para limpar a memória RAM")
    print(f"b) Um tipo de firewall interno")
    print(f"c) O mecanismo para decidir qual processo será executado pela CPU")
    print(f"d) Um método de compactação de arquivos")
    resposta8 = input("Digite a alternativa: ").lower()
    if resposta8 == "c":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n9) O que caracteriza o estado 'pronto' de um processo?\n")
    print(f"a) Está aguardando uma operação de E/S")
    print(f"b) Está sendo executado pela CPU")
    print(f"c) Está carregado e aguardando ser escalonado")
    print(f"d) Está em espera indefinida")
    resposta9 = input("Digite a alternativa: ").lower()
    if resposta9 == "c":
        nota += 1

    os.system('cls')
    print(f"----- INFRAESTRUTURA COMPUTACIONAL -----")
    print(f"\n10) Qual o objetivo do uso de multitarefa em um sistema operacional?\n")
    print(f"a) Reduzir o uso de memória RAM")
    print(f"b) Permitir que múltiplos programas sejam executados ao mesmo tempo")
    print(f"c) Aumentar a velocidade do processador")
    print(f"d) Proteger o sistema contra vírus")
    resposta10 = input("Digite a alternativa: ").lower()
    if resposta10 == "b":
        nota += 1

    os.system('cls')
    return nota