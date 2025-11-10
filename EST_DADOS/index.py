# Controle de gastos pessoais

# Requisitos:
# Perguntar quantas despesas registrar (nome, valor)

# Após registro: 
# Calcular e exibir total gasto no mês
# Calcular e exibir média dos gastos 
# Mostrar o nome da despesa mais cara e seu valor

# Orientações: 
# Obrigatório uso de variáveis, laços e estruturas condicionais 
# Nomes claros e coerentes
# Organize em etapas definidas (entrada, processamento, saída) 

ListaDespesas = []
totalGasto = 0.0
maisCara = {} #nome, valor
mediaGasto = 0.0

def adicionarDespesa(nome, valor):
    ListaDespesas.append({"nome": nome, "valor": valor})
    totalGasto += valor
    if not maisCara or valor > maisCara["valor"]:
        maisCara = {"nome": nome, "valor": valor}
    mediaGasto = totalGasto / len(ListaDespesas)
    return totalGasto, mediaGasto, maisCara

def main():
    quantidadeDespesas = int(input("Quantas despesas você quer registrar? "))
    for i in range(quantidadeDespesas):
        nome = input("Digite o nome da despesa: ")
        valor = float(input("Digite o valor da despesa: "))
        adicionarDespesa(nome, valor)
    print(f"Total gasto no mês: R$ {totalGasto:.2f}")
    print(f"Média dos gastos: R$ {mediaGasto:.2f}")
    print(f"Despesa mais cara: {maisCara['nome']} - R$ {maisCara['valor']:.2f}")

main()