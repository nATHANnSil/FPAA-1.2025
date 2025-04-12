import networkx as nx
import matplotlib.pyplot as plt
import random
from datetime import datetime

class Graph:
    def __init__(self, vertices, directed=False):
        """
        Inicializa o grafo com uma matriz de adjacência e gera arestas aleatórias.
        
        Argumentos:
            vertices (int): Número de vértices do grafo.
            directed (bool): True para grafo direcionado, False para não direcionado.
        """
        self.V = vertices
        self.directed = directed
        self.graph = [[0] * vertices for _ in range(vertices)]
        self._generate_random_graph()

    def _generate_random_graph(self):
        """Gera um grafo aleatório único com conexões válidas."""
        random.seed(datetime.now().timestamp())  # Semente única
        
        # Número de arestas: entre V-1 (mínimo para caminho) e o máximo possível
        min_edges = self.V - 1  # Mínimo para tentar garantir caminho Hamiltoniano
        max_possible_edges = self.V * (self.V - 1) if self.directed else self.V * (self.V - 1) // 2
        edge_count = random.randint(min_edges, max_possible_edges)
        
        # Lista de todas as arestas possíveis (sem loops)
        possible_edges = []
        for u in range(self.V):
            for v in range(self.V):
                if u != v and (self.directed or u < v):
                    possible_edges.append((u, v))
        
        # Embaralha e seleciona 'edge_count' arestas
        random.shuffle(possible_edges)
        selected_edges = possible_edges[:edge_count]
        
        # Adiciona arestas ao grafo
        for u, v in selected_edges:
            self.graph[u][v] = 1
            if not self.directed:
                self.graph[v][u] = 1

    def is_valid(self, v, path, pos):
        """Verifica se o vértice 'v' pode ser adicionado ao caminho na posição 'pos'."""
        if self.graph[path[pos - 1]][v] == 0:
            return False  # Sem aresta
        if v in path:
            return False  # Vértice repetido
        return True

    def hamiltonian_util(self, path, pos):
        """Função recursiva de backtracking para encontrar o caminho Hamiltoniano."""
        if pos == self.V:
            return True  # Todos os vértices foram visitados
        
        for v in range(self.V):
            if self.is_valid(v, path, pos):
                path[pos] = v
                if self.hamiltonian_util(path, pos + 1):
                    return True
                path[pos] = -1  # Backtracking
        
        return False

    def find_hamiltonian_path(self):
        """Encontra um caminho Hamiltoniano no grafo, se existir."""
        for start in range(self.V):  # Tenta iniciar de todos os vértices
            path = [-1] * self.V
            path[0] = start
            if self.hamiltonian_util(path, 1):
                return path
        return None

    def visualize_graph(self, path=None):
        """Visualiza o grafo e destaca o caminho Hamiltoniano."""
        G = nx.DiGraph() if self.directed else nx.Graph()
        
        # Adiciona arestas
        for u in range(self.V):
            for v in range(self.V):
                if self.graph[u][v] == 1:
                    G.add_edge(u, v)
        
        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue',
                edge_color='gray', node_size=700, font_size=14, arrows=self.directed)
        
        # Destaca o caminho
        if path:
            edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
            nx.draw_networkx_edges(G, pos, edgelist=edges,
                                   edge_color='red', width=2, arrows=self.directed)
        
        plt.title(f"Grafo {'Direcionado' if self.directed else 'Não Direcionado'}")
        plt.show()

if __name__ == "__main__":
    # Solicita apenas o tipo de grafo ao usuário
    directed = input("Grafo direcionado? (s/n): ").lower() == 's'
    
    # Gera automaticamente entre 5 e 8 vértices
    V = random.randint(5, 8)
    
    # Cria e processa o grafo
    g = Graph(V, directed)
    path = g.find_hamiltonian_path()
    
    # Exibe resultados
    if path:
        print(f"Caminho Hamiltoniano encontrado ({'direcionado' if directed else 'não direcionado'}):")
        print(" → ".join(map(str, path)))
        g.visualize_graph(path)
    else:
        print(f"Nenhum Caminho Hamiltoniano encontrado ({'direcionado' if directed else 'não direcionado'}).")
        g.visualize_graph()
