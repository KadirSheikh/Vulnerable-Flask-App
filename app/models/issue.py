from app import db 
class Issue(db.Model): 
    id = db.Column(db.Integer, primary_key=True) 
    issue = db.Column(db.String(255), nullable=False) 
    rca = db.Column(db.String(255), nullable=False) 
    improvement = db.Column(db.String(255), nullable=False) 
    def __repr__(self): 
        return f"<Issue {self.issue}>" 