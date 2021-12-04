from django.test import Client
import unittest
import json
import os.path

from validator.utils.validator import ValidatorUtirls

class TestValidatorAPI(unittest.TestCase):

    def setUp(self):
         self.client = Client()

    def test_call_end_point_return_404(self):
        url = "/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    def test_call_end_point_return_200_if_cpf_exist_in_archive(self):
        url = "/000.000.000-00/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        
    def test_call_end_point_return_422_if_cpf_length_is_not_14(self):
        url = "/000.000.000-0/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 422)
    
    def test_call_end_point_return_block_if_cpf_exist_in_archive(self):
        url = "/000.000.000-00/"
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertDictEqual(data, {"status": "BLOCK"})
    
    def test_call_end_point_return_free_if_cpf_not_exist_in_archive(self):
        url = "/000.000.000-77/"
        response = self.client.get(url)
        data = json.loads(response.content)
        self.assertDictEqual(data, {"status": "FREE"})
    
class TestUtilsValidator(unittest.TestCase):
    
    def test_method_verify_status_cpf_return_true(self):
        cpf = "000.000.000-00"
        data = ValidatorUtirls.verify_status_cpf(cpf)
        self.assertTrue(data)
        
    def test_method_verify_status_cpf_return_false(self):
        cpf = "000.000.000-99"
        data = ValidatorUtirls.verify_status_cpf(cpf)
        self.assertFalse(data)

    def test_method_format_cpf_return_length_11(self):
        cpf = "00000000099"
        data = ValidatorUtirls.format_cpf(cpf)
        self.assertEqual(len(data), 14)
    
    def test_method_remove_special_characters_return_only_numbers(self):
        cpf = "000.000.000-99"
        data = ValidatorUtirls.remove_special_characters(cpf)
        self.assertTrue(data.isdigit())
    
    def test_exist_archive(self):
        self.assertTrue(os.path.isfile("blacklist.txt"))
    
    #def test_method_verify_status_cpf_exception(self):
    #    self.assertRaises(Exception, ValidatorUtirls.verify_status_cpf, [None])