# Parte 2
O segundo entregável consiste em um problema comum em engenharia de dados: a transformação de dados disponíveis em <a href="https://drive.google.com/file/d/1IDCjpDZh5St97jw4K_bAewJ8hf-rax9C/view?usp=sharing">arquivo Json</a> para o formato de dataframe, algo comum no dia a dia da empresa. Após transformar esse Json em dataframe é possível perceber que a coluna "item_list" está como dicionário. Seu gestor pediu dois pontos de atenção nessa tarefa:

- Expandir a coluna num mesmo dataframe;
- Normalizar os itens dessa coluna de dicionário e dividí-los em dois dataframes separados, seguindo o modelo relacional.

# Gerar codigo para extração dos Jsons

```
#parte_dois.py
```