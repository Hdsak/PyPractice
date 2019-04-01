import unittest
from survey import Anonymys_survey

class Survey_test(unittest.TestCase):
    def setUp(self):
        question="What language did you first learn to speak?"
        self.my_survey=Anonymys_survey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.response)
    def test_store_three_response(self):
        for n in self.responses:
            self.my_survey.store_response(n)
        for n in self.responses:
            self.assertIn(n,self.my_survey.response)
unittest.main()