# Basic Algorithms

## Decode String

Dada uma string codificada, retorne a string decodificada.

A regra de codificação é: `k[string_codificada]`, onde a `string_codificada` dentro dos colchetes serão repetidas o
número
de `k` vezes. O valor de `k` será sempre um número positivo.

Você deve assumir que as strings de entrada são sempre válidas, sem espaço e os colchetes estão bem formatados.

### Exemplo

```python
solution("3[a]2[bc]")  # "aaabcbc"
solution("3[a2[c]]")  # "accaccacc"
solution("2[abc]3[cd]ef")  # "abcabccdcdcdef"
```