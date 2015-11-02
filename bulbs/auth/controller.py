from bulbs.resources import connection


class UserSession(object):
    def __init__(self, username=None, id=None, group_id=None):#, authorized=False):
        self.username = username
        self.id = id
        self.group_id = group_id
        
    def is_mod(self):
        pass
        
    def is_admin(self):
        pass
        
    def is_banned(self):
        pass
        
    #def is_authorized(self):
    #    return self.authorized
        
    #def set_authorization(self, username):
    #    if not self.is_authorized:
    #        self.username = username
    #        self.authorized = True
            
            # return true if authorization was a sucess, false otherwise
    #        return True
        
    #    return False            
            
def authorize(username, password):
    cursor = connection.con.cursor()
    cursor.execute(
        "SELECT convert_from(decrypt(password, %s, 'aes'), 'utf-8') \
         FROM bulbs_user WHERE username = %s", 
            ("close but no guitar", username)
    )

    if not password == cursor.fetchone()[0]:
        # failure to authenticate
        return dict(
            success=False,
            session=None
        )

    cursor.execute("SELECT id FROM bulbs_User WHERE username = %s", (username, ))
    user_id = cursor.fetchone()[0]
    cursor.execute("SELECT group_id FROM bulbs_User WHERE username = %s", (username, ))
    group_id = cursor.fetchone()[0]
    
    return dict(
        success=True,
        session=UserSession(username, user_id, group_id)
    )

