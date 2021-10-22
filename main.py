from fastapi import FastAPI
from flask import Flask, render_template, request, redirect, session, flash, url_for

app = Flask(__name__)

class cidade:
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

cidade1 = cidade('Fortaleza',"Rua X, n 40")
cidade2 = cidade('Recife',"Rua X, n 40")
cidade3 = cidade('Salvador',"Rua X, n 40")
cidade4 = cidade('São Paulo',"Rua X, n 40")
cidade5 = cidade('Rio de Janeiro',"Rua X, n 40")
cidade6 = cidade('Porto Alegre',"Rua X, n 40")
cidade7 = cidade('Manaus',"Rua X, n 40")

cidades = [cidade1,cidade2, cidade3,cidade4 , cidade5,cidade6 ]

@app.get("/")
async def root():
    return render_template('index.html', titulo='Página Principal')

@app.get("/estrutura")
async def estr():
    return render_template('estrutura.html', titulo='Estrutura')

@app.get("/contato")
async def cont():
    return render_template('contato.html', titulo='Contato', cidades=cidades )


app.run(debug=True)