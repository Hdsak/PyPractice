import unittest
from survey import Anonymys_survey

class Survey_test(unittest.TestCase):
    def test_store_single_response(self):
        question="What language did you first learn to speak?"
        my_survey=Anonymys_survey(question)
        my_survey.store_response("english")
        self.assertIn("english",my_survey.response)
    def test_store_three_response(self):
        question="What language did you first learn to speak?"
        my_survey=Anonymys_survey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        for n in responses:
            my_survey.store_response(n)
        for n in responses:
            self.assertIn(n,my_survey.response)
unittest.main()