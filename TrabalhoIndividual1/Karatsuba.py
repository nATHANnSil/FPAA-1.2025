def karatsuba(x, y):
    """
    Implementação do algoritmo de Karatsuba para multiplicação eficiente de dois números inteiros.
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise ValueError("Ambos os valores devem ser inteiros.")
    
    # Tratamento de números negativos
    sinal = 1
    if x < 0:
        x = -x
        sinal *= -1
    if y < 0:
        y = -y
        sinal *= -1
    
    # Caso base: números de um dígito são multiplicados diretamente
    if x < 10 or y < 10:
        return sinal * (x * y)
    
    # Determina o tamanho máximo entre os números
    n = max(len(str(x)), len(str(y)))
    n_2 = n // 2
    
    # Divide x e y em partes altas e baixas
    high_x, low_x = divmod(x, 10**n_2)
    high_y, low_y = divmod(y, 10**n_2)
    
    # Recursões
    z0 = karatsuba(low_x, low_y)
    z1 = karatsuba((low_x + high_x), (low_y + high_y))
    z2 = karatsuba(high_x, high_y)
    
    # Combina os resultados e aplica o sinal correto
    return sinal * (z2 * 10**(2 * n_2) + ((z1 - z2 - z0) * 10**n_2) + z0)

if __name__ == "__main__":
    while True:
        try:
            entrada1 = input("Digite o primeiro número (ou 'PARAR' para sair): ")
            if entrada1.upper() == "PARAR":
                break
            entrada2 = input("Digite o segundo número (ou 'PARAR' para sair): ")
            if entrada2.upper() == "PARAR":
                break
            
            num1 = int(entrada1)
            num2 = int(entrada2)
            
            resultado = karatsuba(num1, num2)
            print(f"O resultado de {num1} * {num2} é {resultado}\n")
        except ValueError as e:
            print(f"Erro: {e}. Por favor, insira números inteiros válidos.\n")
