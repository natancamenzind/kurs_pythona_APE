import json
import random
# 1. load db
def load_db():
	file = open('milionerzy_db', 'r')
	return json.loads(file.read())
# 2. load question, show answers
def get_question(db, answered_questions):
	question =  random.choice(list(db.items()))
	return question

def create_shuffled_answers(question):
	"""
	qustion: dict; question with all answers
	return: dict; keys A-D, values answers
	"""
	answers = [
		question.get('good'),
		question.get('bad')[0],
		question.get('bad')[1],
		question.get('bad')[2],
	]
	random.shuffle(answers)
	return {
		'A': answers[0], 
		'B': answers[1], 
		'C': answers[2], 
		'D': answers[3], 
	}

def print_question_and_answers(question, answer):
	print(question.get('question'))
	print("A: {}\nB: {}\nC: {}\nD: {}"
		.format(answer.get('A'),
				answer.get('B'),
				answer.get('C'),
				answer.get('D'),)
		)

db = load_db()
print('\n\n\n\tMILIARD W ROZUMIE\n\n\n\n')
bad = 0
good = 0
answered_questions = []
while len(answered_questions) != len(db):
	question = get_question(db, answered_questions)
	answered_questions.append(question[0])
	question = question[1]
	shuffled = create_shuffled_answers(question)
	print_question_and_answers(question, shuffled)


	answer = input('Twoja odpowiedź to:\n').upper()
	if shuffled.get(answer) == question.get('good'):
		print('Brawo!')
		good += 1
	else:
		print('Do dupy!')
		bad += 1

print("Dobrze: {}".format(good))
print("Źle: {}".format(bad))
