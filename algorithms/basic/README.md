# Basic Algorithms

## Decode String

Dada uma string codificada, retorne a string decodificada.

A regra de codificação é: k[string_codificada], onde a string_codificada dentro dos colchetes serão repetidas o número
de k vezes. O valor de k será sempre um número positivo.

Você deve assumir que as strings de entrada são sempre válidas, sem espaço e os colchetes estão bem formatados.

### Exemplos

```python
solution("3[a]2[bc]")  # "aaabcbc"
solution("3[a2[c]]")  # "accaccacc"
solution("2[abc]3[cd]ef")  # "abcabccdcdcdef"
```

## Invert Binary Tree

Neste desafio você deverá construir uma função que recebe uma árvore binária e inverta seus itens filhos, ou seja, o nó
filho da direita do item atual deve ser invertido com o nó filho da esquerda.

Os nós podem ter valores ou até mesmo serem nulos (indicando que não possuem filhos).

### Exemplos

Sua função receberá uma árvore binária da seguinte forma:

..........1 ......../...  
.......2.....3 ....../....../.  
....4...5.6..7 ..../.\  
..8...9

E deverá retornar a árvore binária da seguinte forma:
..........1 ......../...  
.......3.....2 ....../....../.  
....5...4.7..6 ..../.\  
..9...8

## Minimum Depth of Binary Tree

Dada uma árvore binária, encontre a menor profundidade da mesma.

A profundidade mínima é o número de nós que formam o menor caminho entre a raiz e o nó sem nenhum filho da árvore.

Nota: Um nó considerado sem nenhum filho é aquele em que o left e o right são nulos, ou seja, não tem nenhum filho.

Exemplo:

Dada a árvore binária [3, 9, 20, None, None, 15, 7]

        3  
       / \  
      9   20  
     /     \  
    15      7  

O resultado é 2 pois o menor caminho passa pelos números 3 e 9.

## Palindrome Check

Neste desafio você deverá construir uma função que recebe uma string e identifique se a mesma é uma palindrome, ou seja,
se a string é igual a ela mesma invertida.

Exemplo:

Dado que temos a string algomania uma vez invertida temos ainamogla que são diferentes.

Logo, não é uma palindrome.

Ja se recebemos a string abccba uma vez invertida temos abccba que são iguais e a função deve retornar True nesta
situação.

## Three Sum

O Three sum é uma variação do problema Two Sum, caso você ainda não tenha feito ele sugiro que vá primeiro nele e depois
volte aqui.

A idéia deste problema é identificar todos os três números que quando somados resultem em um valor especificado.

Exemplo:

Se o array é [12, 3, 1, 2, -6, 5, -8, 6] e o target é 0. Neste caso, seu programa deve retornar:

[[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]

A soma de todos os valores das listas acima será igual a zero.

## Top k Most Frequent Element

Dado um array que nunca é vazio, retorne os K elementos mais frequentes do mesmo.

Exemplo:

Entrada: [1, 1, 1, 3, 3, 5, 6, 7, 8, 9, 10] -> K = 2

Saída: [1, 3]

Explicação: Os 2 números mais frequentes são 1 e 3.

## Two Sum

O Two Sum é bastante comum durante entrevistas. Seu objetivo é identificar um par de números que somados batam com o
valor da variável target.

Ele pode ser escrito em um algoritmo que roda no tempo O(n).

Exemplo:

Se o array é [4, 1, 2, -2, 11, 15, 1, -1, -6, -4] e o target é 9. Neste caso, seu programa deve retornar:

[-2, 11]

O motivo é bastante simples:

-2 + 11 = 9

## Valid Parentheses

Dada uma string com apenas os seguintes caracteres '(', ')', '{', '}', '[', ']' determine se uma determinada string é
válida.

Uma string é considerada válida se:

Caracteres de abertura devem ser fechadas pelo mesmo tipo. Abertura devem ser fechados com uma chave correspondente. Uma
string vazia é considerada válida.

Exemplo:

Dada uma string com apenas os seguintes caracteres '(', ')', '{', '}', '[', ']' determine se uma determinada string é
válida.

Uma string é considerada válida se:

Caracteres de abertura devem ser fechadas pelo mesmo tipo. Abertura devem ser fechados com uma chave correspondente. Uma
string vazia é considerada válida.