from survey import AnonymousSurvey

# Define a question, and make a Survey.
question = "What language did you first learn to speak"
my_survey = AnonymousSurvey(question)

# Show the question, and store responses to the question
my_survey.show_question()
print("Enter 'q' at any time to quit. \n")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

# Show the survey results
my_survey.show_results()