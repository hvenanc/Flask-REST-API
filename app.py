from flask import Flask,render_template,make_response
from flask_restful import Resource, Api,request
import json

app = Flask(__name__)
api = Api(app)

#Exemlpo de API REST FULL em memória

linhas = [
    {
        "codigo" : 202,
        "nome" : 'T.I Barro/T.I Macaxeira(VARZEA)',
        "tarifa" : 4.10,
        "ar-condicionado" : False
    },

    {
        "codigo" : 2060,
        "nome" : 'T.I Tancredo Neves/T.I Macaxeira',
        "tarifa" : 4.10,
        "ar-condicionado" : True
    },
]

cod_linha = []

for linha in linhas:
    cod_linha.append(linha['codigo'])

class Linha(Resource):

    def get(self,codigo):
        if codigo in cod_linha:
            pos = cod_linha.index(codigo)
            response = linhas[pos]
            return response
        else:
            return {'Status': 'Linha não cadastrada!'}

    def delete(self,codigo):
        if codigo in cod_linha:
            pos = cod_linha.index(codigo)
            linhas.pop(pos)
            return {'Status': 'Linha removida com sucesso!'}
        else:
            return {'Status': 'Linha não cadastrada!'}

    def put(self,codigo):
        if codigo in cod_linha:
            pos = cod_linha.index(codigo)
            dados = json.loads(request.data)
            linhas[pos] = dados
            linhas[pos]['codigo'] = codigo
            return {'Status': 'Linha alterada com sucesso'}
        else:
            return {'Status': 'Linha não cadastrada!'}

class Cadastro_Linha(Resource):


   def post(self):
        dados = json.loads(request.data)
        cod_linha.append(dados['codigo'])
        linhas.append(dados)
        return {'Status': 'Linha cadastrada com sucesso!'}

   def get(self):
       return linhas

class Form(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200,
                             headers)

api.add_resource(Form,'/')
api.add_resource(Cadastro_Linha,'/linha')
api.add_resource(Linha,'/linha/<int:codigo>')

if __name__ == '__main__':
    app.run(debug=True)
