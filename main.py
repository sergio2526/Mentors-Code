from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)
#pymysql: Paquete para la interacción con bd.
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root@localhost/flaskmysql'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Hereda modelo que viene desde la instancia db
class Mentoria(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(70), unique=True)
    description = db.Column(db.String(100))

    def __init__(self, title, description):
        self.title = title
        self.description = description

#crea tablas apartir de las clase mentoria
db.create_all()

class MentoriaSchema(ma.Schema):
    class Meta:
        fields = ('id','title','description')

#cuando se crea una mentoria
mentoria_schema = MentoriaSchema()
mentorias_schema = MentoriaSchema(many=True)


#Enviar mentoria
@app.route('/mentoria', methods=['POST'])
def create_mentoria():
    
    title = request.json['title']
    description = request.json['description']

    new_mentoria = Mentoria(title, description)
    db.session.add(new_mentoria)
    db.session.commit()
    
    return mentoria_schema.jsonify(new_mentoria)


#mostrar todas las mentorias
@app.route('/mentoria', methods=['GET'])
def get_mentorias():
    all_mentorias = Mentoria.query.all()
    result = mentorias_schema.dump(all_mentorias)
    return jsonify(result)


#consultar mentoria
@app.route('/mentoria/<id>', methods=['GET'])
def get_mentoria(id):
    mentoria = Mentoria.query.get(id)
    return mentoria_schema.jsonify(mentoria)


#update mentoria
@app.route('/mentoria/<id>', methods=['PUT'])
def update_mentoria(id):
    mentoria = Mentoria.query.get(id)

    title = request.json['title']
    description = request.json['description']

    mentoria.title = title
    mentoria.description = description

    db.session.commit()
    return mentoria_schema.jsonify(mentoria)


#Delete mentoria
@app.route('/mentoria/<id>', methods=['DELETE'])
def delete_mentoria(id):
    mentoria = Mentoria.query.get(id)
    db.session.delete(mentoria)
    db.session.commit()

    return mentoria_schema.jsonify(mentoria)


if __name__ == '__main__':
    app.run(debug=True)