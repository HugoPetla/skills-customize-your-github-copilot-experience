# 🎮 Assignment: Games in Python

## 🎯 Objective

Nesta tarefa, você implementará um jogo clássico de adivinhação (Hangman) em Python.
Você praticará o uso de strings, loops, condicionais, seleção aleatória, manipulação de dados, controle de fluxo e interação com o usuário.

## 📝 Tasks

### 🛠️ Implementar o Jogo Hangman

#### Description
Crie um jogo de Hangman completo onde os jogadores adivinham letras para revelar uma palavra oculta antes de esgotarem as tentativas.

#### Requirements
Completed program should:

- Selecionar aleatoriamente uma palavra de uma lista predefinida
- Exibir o progresso atual no formato `_ _ _`
- Exibir o progresso atual no formato `_ _ _` (letras adivinhadas e espaços em branco)
- Rastrear o número de tentativas incorretas restantes
- Validar entrada do usuário (verificar se é uma letra válida e se já foi adivinada)
- Encerrar o jogo quando a palavra for adivinhada ou as tentativas se esgotarem
- Exibir mensagens de vitória ou derrota com o resultado final

**Exemplos:**
```
Palavra: _ _ _ _ _ _
Tentativas restantes: 6
Adivinhe uma letra: a
Palavra: a _ _ _ _ _
```

### 🛠️ Melhorias Opcionais

#### Description
Expanda seu jogo com recursos adicionais para maior desafio.

#### Requirements
Completed program should (choose at least 2):

- Implementar dificuldade (fácil, médio, difícil com diferentes números de tentativas)
- Adicionar uma categoria ou tema para cada palavra
- Mostrar letras já adivinhadas (corretas e incorretas)
- Manter um placar de vitórias/derrotas
- Permitir múltiplas rodadas sem reiniciar o programa
