from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy


class IndexViewTestCase(TestCase):

    def setUp(self):
        self.dados = {
            'nome': 'Gustavo Fontenele',
            'email': 'gustavo@hotmail.com',
            'assunto': 'Meu Assunto',
            'mensagem': 'Minha mensagem',
        }

    def test_form_valid(self):
        request = self.client.post(reverse_lazy('index'), data=self.dados)
        self.assertEqual(request.status_code, 302)

    def test_form_invalid(self):
        dados = {
            'nome': 'Gustavo Fontenele',
            'assunto': 'Meu Assunto',
        }
        request = self.client.post(reverse_lazy('index'), data=dados)
        self.assertEqual(request.status_code, 200)
gf1711
