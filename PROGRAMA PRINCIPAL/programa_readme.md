# Análise Empírica de Algoritmos de Ordenação

Este projeto em Python implementa e compara o desempenho empírico de quatro algoritmos clássicos de ordenação. O script mede o número de comparações, trocas/movimentações e o tempo de execução utilizando diferentes tamanhos de entrada.

## Algoritmos Implementados

* **Bubble Sort:** Método quadrático baseado em trocas adjacentes sucessivas com otimização de parada precoce.
* **Insertion Sort:** Método quadrático eficiente para conjuntos pequenos ou parcialmente ordenados.
* **Selection Sort:** Método quadrático baseado na seleção repetida do menor elemento.
* **Quick Sort:** Método eficiente de divisão e conquista baseado em particionamento recursivo.

## Métricas Coletadas

* **Comparações:** Número de vezes que elementos do vetor são avaliados relacionalmente.
* **Trocas / Movimentações:** Quantidade de alterações e deslocamentos de posição realizados no vetor.
* **Tempo de Execução:** Medido em alta precisão utilizando o módulo nativo do Python (`time.perf_counter()`).

```bash
python ordenacao.py

```

## Estrutura do Experimento

O script emprega uma semente fixa (`random.seed(42)`) para garantir a reprodutibilidade dos vetores gerados e executa testes progressivos variando o tamanho da entrada ($N$):

* $N = 10$ elementos
* $N = 100$ elementos
* $N = 1.000$ elementos

Os dados resultantes são impressos diretamente no console em formato tabular, permitindo confrontar a complexidade teórica (notação Big-O) com o comportamento prático de cada algoritmo.
