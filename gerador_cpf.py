import random
import os

def generate_cpf():
    cpf = [random.randrange(10) for _ in range(9)]

    for _ in range(2):
        value = sum([(len(cpf) + 1 - i) * v for i, v in enumerate(cpf)]) % 11
        cpf.append(11 - value if value > 1 else 0)

    return "".join(str(x) for x in cpf)


def generate_cnpj():
    cnpj = [random.randrange(10) for _ in range(8)] + [0, 0, 0, 1]

    for _ in range(2):
        value = sum(v * (i % 8 + 2) for i, v in enumerate(reversed(cnpj)))
        digit = 11 - value % 11
        cnpj.append(digit if digit < 10 else 0)

    return "".join(str(x) for x in cnpj)

opcao = 0

while opcao != 3:

    cpf_gerado = []
    cnpj_gerado = []
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Gerador de CPF e CNPJ.\nSelecione a opção desejada:\n[1] Gerar CPF\n[2] Gerar CNPJ\n[3] Sair")
    opcao = input("Digite sua opção: ")

    if not opcao.isnumeric():
        opcao = 0

    while not int(opcao) in range(1,4):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Entrada inválida - deve ser um número de 1 a 3.\nSelecione a opção desejada:\n[1] Gerar CPF\n[2] Gerar CNPJ\n[3] Sair")
        opcao = input("Digite sua opção: ")
        if not opcao.isnumeric():
            opcao = 0

    opcao = int(opcao)

    if opcao == 1:
        cpf_gerado = generate_cpf()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você escolheu a opção de gerar CPF.\nO CPF gerado é {cpf_gerado}")
        enter = input("Digite qualquer tecla para continuar...")

    elif opcao == 2:
        cnpj_gerado = generate_cnpj()
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Você escolheu a opção de gerar CNPJ.\nO CNPJ gerado é {cnpj_gerado}")
        enter = input("Digite qualquer tecla para continuar...")

    else:
        exit()
    


