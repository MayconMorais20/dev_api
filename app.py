from flask import Flask, request, jsonify
import json
app = Flask(__name__)

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

# devolve um desenvolverdor pelo id, é permitido também deletar e alterar os dados
@app.route('/dev/<int:id>/', methods = ['GET','PUT','DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:    
            desenvolvedor = desenvolvedores[id]
            return desenvolvedor
        except IndexError:
            mensagem = f'desenvolvedor de ID = {id}, não existe.'
            return {'status':'erro', 'mensagem': mensagem}
        
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        
        return jsonify(dados)
    
    elif request.method == 'DELETE':
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
            
        return {'status': status, 'mensagem' : mensagem }


#lista todos os desenvolvedores e permite a inserção de um novo desenvolvedor
@app.route('/dev', methods = ['POST', 'GET'])
def lista_desenvolvedores():
    if request.method == 'POST':
        data = json.loads(request.data)
        id = len(desenvolvedores)
        data.update({'id': id })
        print(data)
        desenvolvedores.append(data)
        return jsonify(data)
    
    elif request.method == 'GET':
        return jsonify(desenvolvedores) 
        

if __name__ == "__main__":
    app.run(debug = True)