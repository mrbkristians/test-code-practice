from survey import AnonymousSurvey

# Define a guestion, and make a survey
question = "What is your native language?"
my_survey = AnonymousSurvey(question)

# Show  the question, and store responses
my_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
print("\nThank you to everyone who participated in the survey!")
my_survey.show_results()