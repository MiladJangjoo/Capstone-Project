from app import db
from werkzeug.security import generate_password_hash, check_password_hash

class PassModel(db.Model):

    __tablename__ = 'passengers' 

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique=True, nullable = False)
    phone_number = db.Column(db.String, nullable = False)
    password_hash = db.Column(db.String, nullable = False)
    email = db.Column(db.String, unique=True, nullable = False)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    requests = db.relationship('ReqModel', backref ='author', lazy='dynamic', cascade='all, delete')


    def __repr__(self):
        return f'<Passenger: {self.username}>'
    

    def hash_password(self,password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash,password)
    
    def from_dict(self,dict):
        password= dict.pop('password')
        self.hash_password(password)
        for k,v in dict.items():
            setattr(self, k, v)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()