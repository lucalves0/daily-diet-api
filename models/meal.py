from database import db 

class Meal(db.Model):
    # id (int), username (text), description (text), data (text), horario (text), data (text), dieta_ativa(Boolean)
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    descricao = db.Column(db.String(200), nullable=False)
    horario = db.Column(db.String(200), nullable=False)
    data = db.Column(db.String(200), nullable=False)
    dieta = db.Column(db.String(200), nullable=False)