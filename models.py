from basicConfig import db


# class BasicDetails(db.Model):
#     __abstract__ = True
#     id = db.Column(db.Integer,primary_key=True)
#     created_on = db.Column(db.DateTime, default=db.func.now())
#     updated_on = db.Column(db.DateTime, default=db.func.now(), onupdate=db.func.now())
#     created_by=db.Column(db.String(50))
#     updated_by=db.Column(db.String(50))


# table 1
class Users(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    user_id=db.Column(db.String(50),unique=True)
    user_name=db.Column(db.String(50),unique=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    password=db.Column(db.String(80))
    # designation=db.Column(db.String(50)) 
    # department=db.Column(db.String(50)) 
    email_id=db.Column(db.String(50)) 
    contact_no=db.Column(db.String(50))
    # location=db.Column(db.String(500))
    # imageURL=db.Column(db.String(2083))
    # mediaURL= db.Column(db.String(2083))
    # reportingTo=db.Column(db.String(50))
    # isActive=db.Column(db.Boolean,default=True,nullable=False)
    
    # skills=db.relationship('SkillSet',backref="Users")
    # roles_id=db.relationship('UserPrevilage',backref="Users")

# table 3
# class UserRole(BasicDetails): #parent
#     role=db.Column(db.String(50),unique=True)
#     role_ids=(db.Column(db.String(50)))
   
#     roles=db.relationship('UserPrevilage',backref="UserRole")

# # table 2
# class UserPrevilage(BasicDetails): #child
#     user_ids = db.Column(db.String(50),db.ForeignKey(Users.user_id))
#     role_id=db.Column(db.String(50),db.ForeignKey(UserRole.role_ids))
#     __table_args__ = (db.UniqueConstraint('user_ids', 'role_id'),)
    

# #table 4
# class SkillSet(BasicDetails):
#     skill=db.Column(db.String(50))
#     user_ids=db.Column(db.String(50),db.ForeignKey(Users.user_id))
#     __table_args__ = (db.UniqueConstraint('user_ids', 'skill'),)    

# db.drop_all()
db.create_all()