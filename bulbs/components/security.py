import bcrypt

def generate_password(pt_password):
    """Return a hashed byte object using bcrypt's hashpw function."""
    twelve = 12
    salt = bcrypt.gensalt(twelve);
    pt_password = bytes(pt_password, encoding="utf-8")
    hashedpw = bcrypt.hashpw(pt_password, salt)
    return hashedpw
