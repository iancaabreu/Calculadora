# Função para calcular a multa moratória
def calcular_multa_moratoria(valor_parcela, dias_atraso, taxa_multa):
    # Verifica se há atraso
    if dias_atraso > 0:
        # Calcula a multa moratória
        multa_moratoria = (valor_parcela * taxa_multa * dias_atraso)
        # Verifica se a multa moratória excede o limite máximo de 10% sobre o valor da nota
        if multa_moratoria > (valor_parcela * 0.1):
            # Define o limite máximo de multa aplicável
            multa_moratoria = valor_parcela * 0.1
        # Retorna a multa moratória
        return round(multa_moratoria, 2)
    else:
        # Retorna zero se não há atraso
        return 0

# Entrada de dados
valor_parcela = float(input("Digite o valor da parcela: "))
dias_atraso = int(input("Digite o número de dias em atraso: "))
taxa_multa = float(input("Digite a taxa de multa moratória: "))

multa_moratoria = calcular_multa_moratoria(valor_parcela, dias_atraso, taxa_multa)
print(f"A multa moratória é de R$ {multa_moratoria}")

