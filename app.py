import sqlite3
from flask import Flask, request, jsonify
from models.meal import Meal
from database import db


app = Flask(__name__)
app.config['SECRET_KEY'] = "your_secret_key"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db.init_app(app)

db = sqlite3.connect('sistema_cadastro.db')
cursor = db.cursor()

# Criação de dieta
@app.route('/meal', methods=["POST"])
def create_meal():
   data_json = request.json
   nome = data_json.get("nome")
   descricao = data_json.get("descricao")
   horario = data_json.get("horario")
   data = data_json.get("data")
   dieta = data_json.get("dieta")

   if nome and descricao:
      meal = Meal(nome=nome, descricao=descricao, horario=horario, data=data, dieta=dieta)
      db.session.add(meal)
      db.session.commit()
      return jsonify({"message" : "Refeição cadastrada com sucesso !"}), 200   
   
   return jsonify({"messagem" : "Dados inválidos. "}), 400

# Altera dieta ja criada 
@app.route('/meal/<int:id_meal>', methods=["PUT"])
def update_meal(id_meal): 
   data_json = request.json
   meal = Meal.query.get(id_meal)

   # Alteração do nome
   if meal and data_json.get("nome"):
         meal.nome = data_json.get("nome")
         db.session.commit()
         return jsonify({"messagem": f"Refeição {id_meal} atualizado com sucesso. "})
   
   # Alteração da descrição
   if meal and data_json.get("descricao"):
         meal.descricao = data_json.get("descricao")
         db.session.commit()
         return jsonify({"messagem": f"Refeição {id_meal} atualizado com sucesso. "})

   # Alteração do horario
   if meal and data_json.get("horario"):
         meal.horario = data_json.get("horario")
         db.session.commit()
         return jsonify({"messagem": f"Refeição {id_meal} atualizado com sucesso. "})
   
   # Alteração da data
   if meal and data_json.get("data"):
      meal.data = data_json.get("data")
      db.session.commit()
      return jsonify({"messagem": f"Refeição {id_meal} atualizado com sucesso. "})
   
   # Alteração da dieta 
   if meal and data_json.get("dieta"):
      meal.dieta = data_json.get("dieta")
      db.session.commit()
      return jsonify({"messagem": f"Refeição {id_meal} atualizado com sucesso. "})
   
   return jsonify({"messagem" : "Dieta não encontrado. "}), 404   

# Delete dieta já cadastrada
@app.route('/meal/<int:id_meal>', methods=['DELETE'])
def delete_meal(id_meal): 
     meal = Meal.query.get(id_meal)

     if meal:
          db.session.delete(meal)
          db.session.commit()
          return jsonify({"message": f"Refeição {id_meal} deletado com sucesso !"})
    
     return jsonify({"messagem" : "Usuario não encontrado. "}), 404

# Busca uma refeição especifica no sistema 
@app.route('/meal/<int:id_meal>', methods=['GET'])
def read_meal(id_meal): 
     meal = Meal.query.get(id_meal)

     if meal:
          return ({"nome": meal.nome})
    
     return jsonify({"messagem" : "Refeição não encontrado. "}), 404

# Busca todas as refeições cadastrada no sistema
@app.route('/buscar_todos_refeicoes', methods=['GET'])
def buscar_todas_meal(): 
   
   return jsonify(db)
    

if __name__ == "__main__":
    app.run(debug=True)


