from flask import Flask, render_template, make_response
from flask_restful import Resource, Api, request
from infra.repository.linha_repository import LinhaRepository
import json

app = Flask(__name__)
api = Api(app)

# Exemlpo de API REST FULL em memória

linhas = [{"codigo":100,"nome":"CIRCULAR (CONDE DA BOA VISTA / PREFEITURA)","tarifa":"R$ 4,10"},{"codigo":101,"nome":"CIRCULAR (CONDE DA BOA VISTA / RUA DO SOL)","tarifa":"R$ 4,10"},{"codigo":102,"nome":"TI SANTA LUZIA / IBURA","tarifa":"R$ 4,10"},{"codigo":104,"nome":"CIRCULAR (IMIP)","tarifa":"R$ 4,10"},{"codigo":106,"nome":"TI SANTA LUZIA / PARQUE AERONÁUTICA","tarifa":"R$ 4,10"},{"codigo":107,"nome":"CIRCULAR (CABUGÁ / PREFEITURA)","tarifa":"R$ 4,10"},{"codigo":108,"nome":"BARRO / CEASA","tarifa":"R$ 4,10"},{"codigo":115,"nome":"TI AEROPORTO / TI AFOGADOS","tarifa":"R$ 4,10"},{"codigo":116,"nome":"CIRCULAR (PRÍNCIPE)","tarifa":"R$ 4,10"},{"codigo":117,"nome":"CIRCULAR (PREFEITURA / CABUGÁ)","tarifa":"R$ 4,10"},{"codigo":128,"nome":"UR-03 / BARRO (MILAGRES)","tarifa":"R$ 4,10"},{"codigo":138,"nome":"ZUMBI DO PACHECO / TI TANCREDO NEVES","tarifa":"R$ 4,10"},{"codigo":144,"nome":"UR-04 / TI TANCREDO NEVES","tarifa":"R$ 4,10"},{"codigo":149,"nome":"TI CAVALEIRO / ZUMBI DO PACHECO","tarifa":"R$ 4,10"},{"codigo":200,"nome":"JABOATÃO (PARADOR)","tarifa":"R$ 4,10"},{"codigo":202,"nome":"BARRO / MACAXEIRA (VÁRZEA)","tarifa":"R$ 4,10"},{"codigo":203,"nome":"ZUMBI DO PACHECO / BARRO (LOTEAMENTO)","tarifa":"R$ 4,10"},{"codigo":204,"nome":"TI SANTA LUZIA / LOTEAMENTO JIQUIÁ","tarifa":"R$ 4,10"},{"codigo":205,"nome":"UR-05 / BARRO (BR-101)","tarifa":"R$ 4,10"},{"codigo":207,"nome":"BARRO / MACAXEIRA (BR-101)","tarifa":"R$ 4,10"},{"codigo":209,"nome":"COQUEIRAL / BARRO","tarifa":"R$ 4,10"},{"codigo":211,"nome":"VILA TAMANDARÉ","tarifa":"R$ 4,10"},{"codigo":212,"nome":"JARDIM SÃO PAULO","tarifa":"R$ 4,10"},{"codigo":220,"nome":"TI JABOATÃO / TI CAVALEIRO","tarifa":"R$ 4,10"},{"codigo":221,"nome":"VILA CARDEAL E SILVA","tarifa":"R$ 4,10"},{"codigo":222,"nome":"JARDIM UCHÔA","tarifa":"R$ 4,10"},{"codigo":232,"nome":"CAVALEIRO","tarifa":"R$ 4,10"},{"codigo":233,"nome":"CAVALEIRO (BACURAU)","tarifa":"R$ 4,10"},{"codigo":242,"nome":"PACHECO","tarifa":"R$ 4,10"},{"codigo":243,"nome":"VILA DOIS CARNEIROS","tarifa":"R$ 4,10"},{"codigo":244,"nome":"ALTO DO VENTO / TI CAVALEIRO","tarifa":"R$ 4,10"},{"codigo":245,"nome":"DOIS CARNEIROS / TI CAVALEIRO","tarifa":"R$ 4,10"},{"codigo":250,"nome":"SANTO ALEIXO / JABOATÃO (LUZ)","tarifa":"R$ 4,10"},{"codigo":251,"nome":"SANTO ALEIXO / JABOATÃO (RIOS)","tarifa":"R$ 4,10"},{"codigo":252,"nome":"VILA RICA / JABOATÃO","tarifa":"R$ 4,10"},{"codigo":254,"nome":"JABOATÃO (BACURAU)","tarifa":"R$ 4,10"},{"codigo":255,"nome":"QUITANDINHA / TI CAVALEIRO","tarifa":"R$ 4,10"},{"codigo":256,"nome":"TI CAVALEIRO / LOTEAMENTO NOVA ESPERANÇA","tarifa":"R$ 4,10"},{"codigo":261,"nome":"TI JABOATÃO / VILA PIEDADE","tarifa":"R$ 4,10"},{"codigo":262,"nome":"TI JABOATÃO / MALVINAS","tarifa":"R$ 4,10"},{"codigo":272,"nome":"COLÔNIA / JABOATÃO","tarifa":"R$ 4,10"},{"codigo":274,"nome":"LOTE 56 / JABOATÃO","tarifa":"R$ 4,10"},{"codigo":311,"nome":"BONGI (AFOGADOS)","tarifa":"R$ 4,10"},{"codigo":312,"nome":"MUSTARDINHA","tarifa":"R$ 4,10"},{"codigo":313,"nome":"SAN MARTIN (ABDIAS DE CARVALHO)","tarifa":"R$ 4,10"},{"codigo":314,"nome":"MANGUEIRA","tarifa":"R$ 4,10"},{"codigo":315,"nome":"BONGI","tarifa":"R$ 4,10"},{"codigo":321,"nome":"JARDIM SÃO PAULO (ABDIAS DE CARVALHO)","tarifa":"R$ 4,10"},{"codigo":322,"nome":"JARDIM SÃO PAULO (BACURAU)","tarifa":"R$ 4,10"},{"codigo":324,"nome":"JARDIM SÃO PAULO (PIRACICABA)","tarifa":"R$ 4,10"},{"codigo":412,"nome":"SAN MARTIN (LARGO DA PAZ)","tarifa":"R$ 4,10"},{"codigo":424,"nome":"CDU / TORRÕES (VIA SAN MARTIN)","tarifa":"R$ 4,10"}]

cod_linha = []

for linha in linhas:
    cod_linha.append(linha['codigo'])

linha = LinhaRepository()


class Linha(Resource):

    # def get(self, codigo):
    #     if codigo in cod_linha:
    #         pos = cod_linha.index(codigo)
    #         response = linhas[pos]
    #         return response
    #     else:
    #         return {'Status': 'Linha não cadastrada!'}

    def get(self, codigo):
        response = linha.select_codigo(codigo)
        return response

    def delete(self, codigo):
        if codigo in cod_linha:
            pos = cod_linha.index(codigo)
            linhas.pop(pos)
            return {'Status': 'Linha removida com sucesso!'}
        else:
            return {'Status': 'Linha não cadastrada!'}

    def put(self, codigo):
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
        linha.insert(dados['codigo'],dados['nome'],dados['tarifa'],dados['ar_condicionado'],dados['integracao'])
        return {'Status': 'Linha cadastrada com sucesso!'}


    def get(self):
        return linhas


class Form(Resource):

    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('index.html'), 200,
                             headers)


api.add_resource(Form, '/')
api.add_resource(Cadastro_Linha, '/linha')
api.add_resource(Linha, '/linha/<int:codigo>')

if __name__ == '__main__':
    app.run(debug=True)
