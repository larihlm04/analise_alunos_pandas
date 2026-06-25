import pandas as pd

dados = {
    "nome": [
        "Ana", "Carlos", "Julia", "Pedro",
        "Marcos", "Beatriz", "Lucas", "Fernanda",
        "Rafael", "Camila"
    ],
    "nota": [
        8, 6, 10, 5,
        7, 9, 4, 8,
        6, 10
    ]
}

df = pd.DataFrame(dados)#tabela com nomes e notas dos alunos

print(df["nome"].count()) #quantidade de alunos
print(df["nota"].mean()) #media
print(df["nota"].max()) #maior nota
print(df["nota"].min()) #menor nota
print(df[df["nota"] >=6 ]["nome"]) #aprovados
print(df[df["nota"] < 6 ]["nome"]) #reprovados
print (len(df[df["nota"] >=6 ]["nome"]))#quantos aprovados
print (len(df[df["nota"] < 6 ]["nome"]))#quantos reprovados

# filtro -> colunas