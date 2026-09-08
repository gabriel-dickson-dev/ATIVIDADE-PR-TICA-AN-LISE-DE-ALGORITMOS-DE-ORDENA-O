# Análise dos Resultados

**a) Menor número de comparações para 10 elementos**
O **Insertion Sort** realizou o menor número de comparações, com 27 operações, seguido por Quick Sort (29), Bubble Sort (44) e Selection Sort (45).

**b) Menos trocas ou movimentações**
Houve um empate técnico entre o **Selection Sort** e o **Quick Sort**, ambos com 7 operações de troca/movimentação para 10 elementos.

**c) Comportamento ao aumentar para 20 elementos**
Os algoritmos mantiveram suas características proporcionais. O número de operações aumentou para todos (por exemplo, Bubble subiu de 44 para 189 e Quick de 29 para 58), mantendo o Quick Sort com menor volume de comparações.

**d) Comportamento com 1.000 elementos**
Houve um crescimento drástico nas operações dos algoritmos quadráticos, enquanto o Quick Sort manteve um volume de operações muito inferior, evidenciando o alto custo de $O(n^2)$ em grandes volumes de dados.

**e) Diferença entre algoritmos de complexidade $O(n^2)$**
Apesar de pertencerem à mesma classe teórica $O(n^2)$, eles não executam a mesma quantidade exata de operações. Para 1.000 elementos, o Selection Sort realizou 499.500 comparações, o Bubble Sort 499.122 e o Insertion Sort 240.670, refletindo lógicas internas e eficiências distintas.

**f) Algoritmo com maior crescimento**
O **Bubble Sort** e o **Selection Sort** apresentaram o crescimento mais acentuado e custoso, escalando rapidamente em comparação ao crescimento controlado do Quick Sort.

**g) Diferenciação do Quick Sort**
O Quick Sort destacou-se pela eficiência com vetores maiores (10.385 comparações contra quase 500.000 dos métodos quadráticos), resultado da aplicação de sua complexidade média de $O(n \log n)$ por meio de divisão e conquista.

**h) Coerência com a teoria**
Sim. Os resultados práticos confirmam a teoria: métodos quadráticos escalam de forma exponencialmente pior do que $O(n \log n)$ conforme o tamanho da entrada ($N$) cresce.

**i) Escolha para um sistema de distribuição**
O **Quick Sort** seria a escolha ideal entre os quatro avaliados por sua eficiência em grande escala. Em ambientes de produção reais, alternativas nativas otimizadas ou algoritmos como o Merge Sort também seriam considerados.
