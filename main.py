# Função para calcular a multa moratória
def calcular_multa_moratoria(valor_da_nota, dias_atraso, taxa_multa):
    # Verifica se há atraso
    if dias_atraso > 0:
        # Calcula a multa moratória
        multa_moratoria = (valor_da_nota * taxa_multa * dias_atraso) / 365
        # Retorna a multa moratória
        return round(multa_moratoria, 2)
    else:
        # Retorna zero se não há atraso
        return 0

# Entrada de dados
valor_da_nota = float(input("Digite o valor da nota: "))
dias_atraso = int(input("Digite o número de dias em atraso: "))
taxa_multa = float(input("Digite a taxa de multa moratória: "))

multa_moratoria = calcular_multa_moratoria(valor_da_nota, dias_atraso, taxa_multa)
print(f"A multa moratória é de R$ {multa_moratoria}")