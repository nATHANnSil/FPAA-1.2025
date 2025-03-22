def maxmin_select(arr, left, right):
    """
    Algoritmo recursivo para encontrar o maior e menor elemento em um array.
    """
    # Caso base 1: Array com um único elemento
    if left == right:
        return arr[left], arr[left]  # Retorna o mesmo elemento como min e max
    
    # Caso base 2: Array com dois elementos
    if right == left + 1:
        if arr[left] < arr[right]:
            return arr[left], arr[right]  # Retorna (min, max) ordenados
        else:
            return arr[right], arr[left]  # Retorna (min, max) ordenados
    
    # Divisão do array em duas metades
    mid = (left + right) // 2  # Calcula o ponto médio
    min1, max1 = maxmin_select(arr, left, mid)  # Recursão na primeira metade
    min2, max2 = maxmin_select(arr, mid + 1, right)  # Recursão na segunda metade
    
    # Combinação dos resultados das metades
    return min(min1, min2), max(max1, max2)  # Retorna o min e max globais

if __name__ == "__main__":
    # Interface de usuário para entrada de dados
    while True:
        try:
            numeros = []
            print("Digite os números, um por vez. Quando terminar, digite 'PRONTO'.")
            while True:
                entrada = input("Número: ")
                if entrada.upper() == "PRONTO":
                    break  # Finaliza a entrada de dados
                numeros.append(int(entrada))  # Converte entrada para inteiro
            
            if not numeros:
                print("Nenhum número inserido. Tente novamente.")
                continue  # Reinicia o loop se o array estiver vazio
            
            # Executa o algoritmo e exibe os resultados
            minimo, maximo = maxmin_select(numeros, 0, len(numeros) - 1)
            print(f"Menor elemento: {minimo}, Maior elemento: {maximo}")
            
            # Opção para sair do programa
            parar = input("Digite 'PARE' para sair ou pressione Enter para continuar: ")
            if parar.upper() == "PARE":
                break
        except ValueError:
            print("Entrada inválida. Certifique-se de inserir apenas números inteiros.")
