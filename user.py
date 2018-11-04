class User:
    """
    Class that generates new instances of users.
    """
     user_list = [] #Empty user list
     def __init__(self,username,password):
        """
        __init__ method that defines properties for our objects
         Args:
            username: New user username.
            password: New user password.
        """
         self.username = username
        self.password = password