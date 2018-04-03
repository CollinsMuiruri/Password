import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    '''
    defines the cases for the contact class behaviour
    '''

    def setUp(self):
        '''
        run before each TestCase
        '''
        self.new_credentials = Credentials("Dnyt","hd","0710682029","dnyt@moringa.com")

    def test_init(self):
        '''
        test if object is initialized
        '''

        self.assertEqual(self.new_credentials.first_name,"Dnyt")
        self.assertEqual(self.new_credentials.last_name,"hd")
        self.assertEqual(self.new_credentials.number,"0710682029")
        self.assertEqual(self.new_credentials.email,"dnyt@moringa.com")

    def test_save_credentials(self):
        '''
        save credentials
        '''
        self.new_credentials.save_credentials()

        self.assertEqual(len(Credentials.contact_list),1)

    def test_credentials_display(self):
        '''
        Show saved Credentials
        '''
        self.assertEqual(Credentials.display_credentials(),Credentials.contact_list)



if __name__ == '__main__':
    unittest.main()
