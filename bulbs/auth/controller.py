from bulbs.resources import connection


class Session(object):
    def __init__(self, username=None, id=None, group_id=None):
        self._username = username
        self._id = id
        self._group_id = group_id
        self._authorized = False
        
    def is_authorized(self):
        return self._authorized
        
    def set_authorization(self, username):
        if self._username is None:
            self._username = username
            return "User sucessfully authorized"
            
        return "User already authorized"
        
    @property
    def username(self):
        return self._username
        
    @username.setter
    def username(self, value):
        self._username = value
            
    @property
    def group_id(self):
        return self._group_id
        
    @group_id.setter
    def group_id(self, value):
        self._group_id = value
            
            
def authorize(username, password):
    cursor = connection.con.cursor()
    cursor.execute(
        "SELECT convert_from(decrypt(password, %s, 'aes'), 'utf-8') \
         FROM bulbs_user WHERE username = %s", 
            ("close but no guitar", username)
    )

    if not password == cursor.fetchone()[0]:
        # failure to authenticate, mostly likely invalid user or pass
        return dict(
            success=False,
            session=Session()
        )

    cursor.execute("SELECT id FROM bulbs_User WHERE username = %s", (username, ))
    user_id = cursor.fetchone()[0]
    cursor.execute("SELECT group_id FROM bulbs_User WHERE username = %s", (username, ))
    group_id = cursor.fetchone()[0]
    
    return dict(
        success=True,
        session=Session(username, user_id, group_id)
    )
    
    #return {
    #    "success": True, 
    #    "session": Session(username, user_id, group_id)
    #}


