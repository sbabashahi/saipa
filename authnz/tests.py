from django.contrib.auth.models import User
from django.test import TestCase

from authnz.transactions import register_user


class AuthnzTestCase(TestCase):
    def test_register_transaction(self):
        username = 'saeed'
        password = 'mypass12'
        user = register_user(username, password)
        self.assertEqual(User.objects.count(), 1, 'Count user model failed')
        self.assertEqual(User.objects.last().username, username, 'Username failed')
        self.assertTrue(User.objects.last().check_password(password), 'Password failed.')
        self.assertIsInstance(user, User, 'Not returned a User')


class RegisterTestCase(TestCase):
    def test_register(self):
        username = 'saeed'
        password = 'mypass12'
        resp = self.client.post('/authnz/register/', data={'username': username, 'password': password},
                                content_type='application/json')
        self.assertEqual(resp.status_code, 201, 'Wrong status code')
        data = resp.json()
        self.assertTrue('data' in data, 'Wrong response structure')
        self.assertTrue('token' in data['data'], 'Wrong response structure')
        self.assertTrue('current_time' in data, 'Wrong response structure')
        self.assertTrue('success' in data, 'Wrong response structure')
        self.assertEqual(data['success'], True, 'Wrong response structure')

    def test_wrong_register(self):
        username = 'saee'
        password = 'mypass12'
        resp = self.client.post('/authnz/register/', data={'username': username, 'password': password},
                                content_type='application/json')
        self.assertEqual(resp.status_code, 400, 'Wrong status code')
        data = resp.json()
        self.assertTrue('current_time' in data, 'Wrong response structure')
        self.assertTrue('success' in data, 'Wrong response structure')
        self.assertEqual(data['success'], False, 'Wrong response structure')
        self.assertIsNotNone(data['message'])
        self.assertIsNotNone(data['message']['username'])

    def test_wrong_register(self):
        username = 'saeed'
        password = 'pass'
        resp = self.client.post('/authnz/register/', data={'username': username, 'password': password},
                                content_type='application/json')
        self.assertEqual(resp.status_code, 400, 'Wrong status code')
        data = resp.json()
        self.assertTrue('current_time' in data, 'Wrong response structure')
        self.assertTrue('success' in data, 'Wrong response structure')
        self.assertEqual(data['success'], False, 'Wrong response structure')
        self.assertIsNotNone(data['message'])
        self.assertIsNotNone(data['message']['password'])

    def test_duplicate_register(self):
        username = 'saeed1'
        password = 'mypass12'
        resp = self.client.post('/authnz/register/', data={'username': username, 'password': password},
                                content_type='application/json')
        self.assertEqual(resp.status_code, 201, 'Wrong status code')

        resp = self.client.post('/authnz/register/', data={'username': username, 'password': password},
                                content_type='application/json')
        self.assertEqual(resp.status_code, 400, 'Wrong status code')
        data = resp.json()
        self.assertTrue('current_time' in data, 'Wrong response structure')
        self.assertTrue('success' in data, 'Wrong response structure')
        self.assertEqual(data['success'], False, 'Wrong response structure')
        self.assertIsNotNone(data['message'])
