class Anonymys_survey():
    def __init__(self,question):
        self.question=question
        self.response=[]
    def show_question(self):
        print(self.question)
    def store_response(self,new_response):
        self.response.append(new_response)
    def show_results(self):
        print("Results of survey :")
        for n in self.response:
            print("\t"+n)
# question="What language did you first learn to speak?"
# survey=Anonymys_survey(question)
# survey.show_question()
# survey.store_response("English")
# survey.show_results()