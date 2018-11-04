import unittest 
from user import User
 class TestUser(unittest.TestCase):
     """
    Test class that defines test cases for the contact class behaviours
     Args:
        unittest.TestCase: TestCase class that helps in creating test cases
     """
    def setUp(self):
        """
        Set up method to run before each test case.
        """
        self.new_user = User ("Sammy","Mutua") #create user object
         def tearDown(self):
        """
        tearDown method that does the clean-up after each test has run
        """ 
        User.user_list = []
     def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """
        self.assertEqual(self.new_user.username,"Sammy")
        def test_save_user(self):
        """
        test to check if the user object is saved on user list
        """
        self.new_user.save_user() #save user
        self.assertEqual(len(User.user_list),1)
        def test_save_multiple_user(self):
        """
        To check if we can save multiple objects into list
        """
        self.new_user.save_user()
        test_user = User ("Test","34huhuhuhu")
        test_user.save_user()
        self.assertEqual(len(User.user_list),2)
 if __name__ == '__main__':
    unittest.main() 