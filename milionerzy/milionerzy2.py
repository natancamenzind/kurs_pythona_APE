import json
import random
# 1. load db
file = open('milionerzy_db', 'r')
data_base = file.read()
milionerzy_db = json.loads(data_base)

# 2. get question from db
def get_questio_from_db(db):
	return random.choice(list(db.items()))

# 3. prepare answers
def prepare_answers(question):
	question_dict = question[1]
	all_answers = [question_dict.get('good'),
		question_dict.get('bad')[0],
		question_dict.get('bad')[1],
		question_dict.get('bad')[2]]
	random.shuffle(all_answers)

	return dict(zip(('A', 'B', 'C', 'D'), all_answers))

# 4. print question and answers
def print_question_and_answers(question_dict, answers_dict):
	print(question_dict.get('question'))
	for k, v in answers_dict.items():
		print(f"{k}: {v}")

# 5. ask for answer
def ask_and_judge(answers_dict, question_dict):
	answer = input()
	# 6. compare user answer with right one
	given_answer = answers_dict.get(answer)
	if given_answer == question_dict.get('good'):
		print('Brawo')
	else:
		print('Źle')


question = get_questio_from_db(milionerzy_db)
answers = prepare_answers(question)
print_question_and_answers(question[1], answers)
ask_and_judge(answers, question[1])
