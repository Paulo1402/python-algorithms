# Intermediary Algorithms

## Simplify Path

Simplifique o path absoluto para um arquivo (no estilo Unix). Em outras palavras, converta o mesmo para o modo canonico.

Neste modo, o `.` se refere ao diretório atual. `..` se refere ao diretório acima.

**Nota:** O path neste formato deve sempre começar com `/` e sempre devera ter um `/` único entre os diretórios.

### Exemplo

```
Entrada: "/home/"
Saída: "/home"
```

```
Entrada: "/home/../"
Saída: "/"
```

```
Entrada: "/home/../home/./"
Saída: "/home"
```

```
Entrada: "/home/../home/./"
Saída: "/home"
```
