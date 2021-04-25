from flask_restful import Resource
from flask import request
import json

lista_habilidades = {
        'nome': 
                [
                    'Python',
                    'Java',
                    'PHP',
                    'Spring',
                    'MySQL',
                ]
}

class Habilidades(Resource):
    def get(self):
        return lista_habilidades
    
    def post(self):
        dados = json.loads(request.data)
        lista_habilidades["nome"].append(dados["nome"])
        return dados
    
class HabilidadesModificar(Resource):
    def put(self,id):
        try:
            dados = json.loads(request.data)
            lista_habilidades["nome"][id] = dados["nome"]
            return dados
        except IndexError:
            status = 'erro'
            mensagem = f'desenvolvedor de id: {id}, não existe.'
        except:
            status = 'erro'
            mensagem = 'erro desconhecido, procure o ADM da API'
            
    def delete(self, id):
        try:
            lista_habilidades["nome"].pop(id)
            status = 'sucesso'
            mensagem = 'registro excluido'
        except IndexError:
            status = 'erro'
            mensagem = f'desenvolvedor de ID = {id}, não existe.'
        except:
            status = 'erro'
            mensagem = 'erro desconhecido, procure o ADM da API'
        
        #não executa se não houver erros!          
        return {'status': status, 'mensagem' : mensagem }