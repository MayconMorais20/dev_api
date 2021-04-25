from flask import Flask, request
from flask_restful import Resource, Api
from habilidades import Habilidades, HabilidadesModificar
import json

app = Flask(__name__)
api = Api(app)

desenvolvedores = [
    {
     'id': 0,
     'nome':'Rafael',
     'habilidades': ['Python','Flask']
    },
    {
     'id': 1,
     'nome':'Galleani',
     'habilidades': ['Python','Django']
    },
    {
      'id': 2,
      'nome':'Joao paulo',
      'habilidades': ['C++','Java']
    }
]

# devolve um desenvolverdor pelo id, é permitido também deletar e alterar os dados pelo id
class Desenvolvedor(Resource):
    def get(self,id):
        try:    
            reponse = desenvolvedores[id]
            return reponse
        except IndexError:
            status = 'erro'
            mensagem = f'desenvolvedor de id: {id}, não existe.'
        except:
            status = 'erro'
            mensagem = 'erro desconhecido, procure o ADM da API'
        
        #não executa se não houver erros!       
        return {'status': status, 'mensagem' : mensagem }
    
    def put(self,id):
        try:
            dados = json.loads(request.data)
            desenvolvedores[id] = dados
            return dados
        except IndexError:
            status = 'erro'
            mensagem = f'desenvolvedor de id: {id}, não existe.'
        except:
            status = 'erro'
            mensagem = 'erro desconhecido, procure o ADM da API'
        
        #não executa se não houver erros!          
        return {'status': status, 'mensagem' : mensagem }
            
    def delete(self,id):
        try:
            desenvolvedores.pop(id)
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

#lista todos os desenvolvedores e permite a inserção de um novo desenvolvedor
class ListaDesenvolvedores(Resource):
    def get(self):
        return desenvolvedores
    
    def post(self):
        dados = json.loads(request.data)
        id = len(desenvolvedores)
        dados.update({'id': id })
        desenvolvedores.append(dados)
        
        return dados

api.add_resource(ListaDesenvolvedores, '/dev/')
api.add_resource(Desenvolvedor, '/dev/<int:id>/')
api.add_resource(Habilidades, '/habilidades/')
api.add_resource(HabilidadesModificar, '/habilidades/<int:id>/')

if __name__ == "__main__":
    app.run(debug =True)