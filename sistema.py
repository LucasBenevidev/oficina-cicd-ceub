# Regra de Negócio: Função de Soma de Valores
def somar_valores(a, b):
    return a + b

# Validação do Sistema (Teste Automatizado)
def test_somar_valores():
    # Espera-se que 2 + 3 seja estritamente igual a 5
    assert somar_valores(2, 3) == 6
    print("Sucesso: A validação matemática do sistema passou em conformidade!")

if __name__ == "__main__":
    test_somar_valores()
