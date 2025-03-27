# Intermediary Algorithms

## Word Search

Dado uma matriz 2D e uma palavra, identifique se esta determinada palavra está dentro da matriz.

A palavra pode ser construída a partir de letras que estão sequenciais em valores adjacentes, onde valores adjacentes
são aqueles que estão horizontalmente ou verticalmente por perto.

**Nota:** a mesma letra não pode ser usada duas vezes para construir uma palavra.

### Exemplo

```python
board = [
    ['A', 'B', 'C', 'E'],
    ['S', 'F', 'C', 'S'],
    ['A', 'D', 'E', 'E']
]  
```

Dada a palavra `ABCCED`, retorne `True`.  
Dada a palavra `SEE`, retorne `True`.  
Dada a palavra `ABCB`, retorne `False`.  