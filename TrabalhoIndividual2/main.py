def maxmin_select(arr, left, right):
    """
    Algoritmo recursivo para encontrar o maior e menor elemento em um array
    utilizando a abordagem de divisão e conquista.
    """
    # Caso base: Apenas um elemento no array
    if left == right:
        return arr[left], arr[left]
    
    # Caso base: Dois elementos, comparando diretamente
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]
        else:
            return arr[right], arr[left]
    
    # Divisão do problema em duas partes
    mid = (left + right) // 2
    min1, max1 = maxmin_select(arr, left, mid)
    min2, max2 = maxmin_select(arr, mid + 1, right)
    
    # Combinação dos resultados
    return min(min1, min2), max(max1, max2)

if __name__ == "__main__":
    while True:
        try:
            numeros = []
            print("Digite os números, um por vez. Quando terminar, digite 'PRONTO'.")
            while True:
                entrada = input("Número: ")
                if entrada.upper() == "PRONTO":
                    break
                numeros.append(int(entrada))
            
            if not numeros:
                print("Nenhum número inserido. Tente novamente.")
                continue
            
            minimo, maximo = maxmin_select(numeros, 0, len(numeros) - 1)
            print(f"Menor elemento: {minimo}, Maior elemento: {maximo}")
            
            parar = input("Digite 'PARE' para sair ou pressione Enter para continuar: ")
            if parar.upper() == "PARE":
                break
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir apenas números inteiros.")
