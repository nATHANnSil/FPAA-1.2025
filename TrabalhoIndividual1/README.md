# Algoritmo de Karatsuba em Python

## Descrição do Projeto
Implementação do algoritmo de Karatsuba para multiplicação eficiente de números inteiros grandes. O algoritmo reduz a complexidade da multiplicação tradicional de \(O(n^2)\) para \(O(n^{\log_2 3}) \O(n^{1.585})\), utilizando divisão e conquista recursiva.

### Lógica do Algoritmo (Passo a Passo):
1. **Validação de Entradas**:  
   - Verifica se os valores são inteiros (`int`).
2. **Tratamento de Sinais**:  
   - Converte números negativos para positivos e armazena o sinal do resultado.
3. **Caso Base**:  
   - Se um dos números tem 1 dígito (`x < 10` ou `y < 10`), retorna a multiplicação direta com o sinal ajustado.
4. **Divisão dos Números**:  
   - Divide `x` e `y` em partes alta (`high`) e baixa (`low`), usando `divmod`.
5. **Recursão**:  
   - Calcula três produtos recursivamente:  
     - `z0 = karatsuba(low_x, low_y)`  
     - `z1 = karatsuba((low_x + high_x), (low_y + high_y))`  
     - `z2 = karatsuba(high_x, high_y)`.
6. **Combinação**:  
   - Aplica a fórmula:  
     z2 * 10^{2n/2} + (z1 - z2 - z0) * 10^{n/2} + z0
     
7. **Ajuste Final**:  
   - Multiplica o resultado pelo sinal armazenado.

## Como Executar o Projeto
### Pré-requisitos:
- Python 3.x instalado.

### Passos:
1. Clone o repositório:
   ```bash
   git clone https://github.com/nATHANnSil/FPAA-1.2025.git
   
E navegue até a pasta TrabalhoIndividual1 com:

   ``` 
   cd FPAA-1.2025/TrabalhoIndividual1
   ```
2. Execução do código
    ```
    python Karatsuba.py

3. Siga as instruções do Terminal

- Digite dois numeros inteiros. 
    - Ex.: 10 e 350
- Para sair, digite **PARAR**

# Relatório Técnico

### Análise da Complexidade Ciclomática

### Grafo de Fluxo de Controle

Disponível em: https://drive.google.com/file/d/1hSKEn00RUmWY8G1ESnAUAKshnhfz3aCr/view?usp=sharing

- Nós (N): 11 (validação, erro, tratamento de sinais, recursão, etc...).
- Arestas (E): 12 (Se ! inteiro e Se = inteiro).
- Componentes Conexos (P): 1
- Cálculo da Complexidade Ciclomática:

    ```
    M = E - N + 2.P -> M = 12 - 11 + 2.1 -> M = 3

### Análise da Complexidade Assintótica

- Complexidade Temporal: 

    ``` 
    T(n)=3T(2/n)+O(n)⟹O(nlog2³)≈O(n1.585)

- Melhor Caso:
O(1) (quando um dos números tem 1 dígito).

- Pior Caso: 
O(n¹⁵⁸⁵)(números grandes com divisões equilibradas).

- Complexidade Espacial:
O(n)(devido a pilha de recursão)


## LICENÇA
### Este projeto está licenciado sob a Licença MIT.


