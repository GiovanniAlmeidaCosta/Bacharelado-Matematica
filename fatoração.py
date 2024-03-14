"""
Bacharelado Matemática Universidade Positivo 2024
Giovanni de Almeida Costa
Teoria dos Números
"""

#
#    Retorna um vetor com os fatores primos do número dado.
#
def fatoracao_primos(numero):
    fatores = [] # Guarda os fatores
    divisor = 2  # primeiro número primo

    while numero > 1:
        while numero % divisor == 0:
            fatores.append(divisor)
            numero //= divisor
        divisor += 1

        # Só testar números não primos
        while not eh_primo(divisor):
            divisor += 1

    return fatores

#
# Verifica se um número é primo
#
def eh_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True