# Análise de Algoritmos de Ordenação

## Projeto desenvolvido em Python para analisar e comparar o desempenho de quatro algoritmos de ordenação:

- Bubble Sort
- Insertion Sort
- Selection Sort
- Quick Sort

O experimento avalia a quantidade de comparações e trocas/movimentações realizadas por cada algoritmo conforme aumenta a quantidade de elementos processados.

## Objetivo

Simular uma situação de uma central de distribuição de pedidos, na qual códigos numéricos de prioridade precisam ser organizados em ordem crescente.

O objetivo é observar experimentalmente como diferentes algoritmos de ordenação se comportam com conjuntos de:

10 elementos
20 elementos
1.000 elementos

Todos os algoritmos recebem exatamente o mesmo vetor inicial em cada experimento.

## Algoritmos analisados
Bubble Sort

Compara elementos vizinhos e realiza trocas quando estão fora de ordem.

Complexidade típica: O(n²)

Insertion Sort

Constrói o vetor ordenado gradualmente, inserindo cada elemento em sua posição correta.

Complexidade típica: O(n²)

Selection Sort

Procura o menor elemento da parte não ordenada e o coloca na posição correta.

Complexidade típica: O(n²)

Quick Sort

Utiliza um pivô para dividir o vetor em partes menores e ordená-las recursivamente.

Complexidade média: O(n log n)
Pior caso: O(n²)

"Critério de contagem"

O projeto contabiliza:

Comparações

Cada operação utilizada para verificar a relação entre dois valores durante a ordenação.

Trocas

No Bubble Sort e Selection Sort, cada troca de dois elementos é contabilizada como uma operação.

Movimentações

No Insertion Sort, cada deslocamento de elemento e a inserção da chave são contabilizados.

No Quick Sort, cada troca de posição entre elementos é contabilizada como uma movimentação.

## Tamanhos dos experimentos
Tamanho do vetor	Objetivo
10	Observar o comportamento com poucos elementos
20	Comparar o crescimento inicial
1.000	Observar o impacto em conjuntos maiores

Para garantir que a comparação seja justa, é gerado um único vetor original para cada tamanho e, posteriormente, são criadas cópias para cada algoritmo.

vetor_bubble = original.copy()
vetor_insertion = original.copy()
vetor_selection = original.copy()
vetor_quick = original.copy()
