class AnonymousSurvey:
    '''Collect answers of the survey'''
    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        '''Show the survey question'''
        print(self.question)

    def store_response(self, new_response):
        '''Store a new response'''
        self.responses.append(new_response)

    def show_results(self):
        '''Show the survey results'''
        print("Survey reesult: ")
        for response in self.responses:
            print(f"- {response}")

first_answer = AnonymousSurvey("What is your name?")

first_answer.show_question()
first_answer.store_response("George")
first_answer.store_response("John")
first_answer.store_response("Mary")
first_answer.show_results()