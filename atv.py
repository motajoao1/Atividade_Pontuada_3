import os
os.system ("cls || clear")

def autenticar_funcionario():
    matricula = input("Digite sua matrícula: ")
    senha = input("Digite sua senha: ")
    print("Acesso concedido!\n")
    return matricula

def calcular_inss(salario_base):
    if salario_base <= 1320.00:
        inss = salario_base * 0.075
    elif salario_base <= 2571.29:
        inss = salario_base * 0.09
    elif salario_base <= 3856.94:
        inss = salario_base * 0.12
    elif salario_base <= 7507.49:
        inss = salario_base * 0.14
    else:
        inss = 1051.05
    return min(inss, 1051.05)

def calcular_irrf(salario_base, dependentes):
    deducao_dependente = dependentes * 189.59
    base_ir = salario_base - deducao_dependente

    if base_ir <= 2112.00:
        irrf = 0
    elif base_ir <= 2826.65:
        irrf = base_ir * 0.075
    elif base_ir <= 3544.00:
        irrf = base_ir * 0.15
    elif base_ir <= 4256.00:
        irrf = base_ir * 0.225
    else:
        irrf = base_ir * 0.275
    return irrf

def calcular_vale_transporte(salario_base, opta_vt):
    return salario_base * 0.06 if opta_vt.lower() == 's' else 0

def calcular_vale_refeicao(valor_vr):
    return valor_vr * 0.20

def calcular_plano_saude(dependentes):
    return dependentes * 150.00

def calcular_salario_liquido():
    autenticar_funcionario()

    salario_base = float(input("Informe seu salário base (R$): "))
    dependentes = int(input("Informe a quantidade de dependentes: "))
    opta_vt = input("Deseja receber vale transporte? (s/n): ")
    valor_vr = float(input("Informe o valor do vale refeição fornecido pela empresa (R$): "))

    inss = calcular_inss(salario_base)
    irrf = calcular_irrf(salario_base, dependentes)
    vt = calcular_vale_transporte(salario_base, opta_vt)
    vr = calcular_vale_refeicao(valor_vr)
    saude = calcular_plano_saude(dependentes)

    descontos = inss + irrf + vt + vr + saude
    salario_liquido = salario_base - descontos

    print("\n--- Folha de Pagamento ---")
    print(f"Salário Base: R$ {salario_base:.2f}")
    print(f"INSS: R$ {inss:.2f}")
    print(f"IRRF: R$ {irrf:.2f}")
    print(f"Vale Transporte: R$ {vt:.2f}")
    print(f"Vale Refeição: R$ {vr:.2f}")
    print(f"Plano de Saúde: R$ {saude:.2f}")
    print(f"Salário Líquido: R$ {salario_liquido:.2f}")

# Executar o sistema
calcular_salario_liquido()
