from django.test import TestCase
#from .Models import User

class Login(TestCase):
    def setUp(self):
                self.user = User.objects.create(
            email='test@gmail.com', password='testpassword'
        )
    def test_login_success(self):
        response = self.client.post(reverse('login'), {
               'email' : 'test@gmail.com',
               'password': 'testpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['user'].is_authenticated)

    def test_login_failure(self):
        response = self.client.post(reverse('login'), {
              'email' : 'test@gmail.com',
              'password' : 'wrongpassword'
        })
        self.assertEqual(response.status_code, 200)
        self.assertFalse(response.context['user'].is_authenticated)
    
    def test_invalid_email(self):
          response = self.client.post(reverse('login'), {
                'email' : 'wrong@gmail.com',
                'password' : 'testpassword'
          })
          self.assertEqual(response.status_code, 200)
          self.assertFalse(response.content['user'].is_authenticated)

    def test_email_format(self):
          response = self.client.post(reverse('login'), {
                'email' : 'test',
                'password' : 'testpassword'
          })
    def test_login_redirect(self):
          response = self.client.post(reverse('login'),{
                'email' : 'test@gmail.com',
                'password' : 'testpassword'
          })
          self.assertRedirects(response, reverse('home'))