import bcrypt

def generate_password(pt_password):
    '''Returns a hashed bytes object using bcrypt's hashpw function'''
    twelve = 12
    salt = bcrypt.gensalt(twelve);
    
    pt_password = bytes(pt_password, encoding="utf-8")
    hashed_password = bcrypt.hashpw(pt_password, salt)
    
    return hashed_password
