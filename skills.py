# Part 1: Discussion
# What are the three main design advantages that object orientation can provide?

# Object orientation provides encapsulation, abstraction, and polymorphism. 

# Encapsulation keeps methods, properties, and other details together as a single object. 
# Encapsulation allows for data and functions to be grouped, which lends to more organized code.
# Abstraction hides the internal details of the function or object.
# Polymophism allows for treating objects of subclasses as objects of a base class. 
# It gives the ability to change components of subclasses. 

# Explain each concept.

# 1. What is a class?

# A class is a user-defined type. Classes are used to create objects, which provide a set 
# of variables, attributes, methods, or other properties for item(s).
# A parent class is a class that is used to create (or derive) another class, while the child 
# or subclasses are those that are derived. 

# # 2. What is an instance attribute?

# While class attributes are owned by the parent class, instance attributes are those 
# defined on the instance itself, and are set directly on the object.

# # 3. What is a method?

# Methods are functions declared on a class. They have at least one parameter. 

# # 4. What is an instance in object orientation?
# An instance is the creation of a new object. 

# # 5. How is a class attribute different than an instance attribute? Give an example of when you might use each.

# While class attributes are owned by the parent class, instance attributes are those 
# # defined on the instance itself, and are set directly on the object. A class attribute is a piece of 
# # data on the class itself and when you ask for it on an instance, it finds it on the class.
# Say you create a class to represent rectangles. A class attribute might be used to specify width and height.
# An instance attribute would be used when you instantiate a rectangle object and assign values to the height and width. 

# Parts 2 through 5:
# Create your classes and class methods

class Student(object):
	"""Stores student info"""

	def __init__(self, first_name, last_name, address, score):
		self.first_name = first_name
		self.last_name = last_name
		self.address = address
		self.score = score 

####################

class Question(object):
	"""Stores question and answers"""

	def __init__(self, question, answer):
		self.question = "question: %s", % question
		self.answer = "answer: %s", % answer

	def ask_and_evaluate(self, question):
		user_input = raw_input(question)
		if user_input == correct_answer:
			return True
		else:
			return False

#####################

class Exam(object):
	"""Exam info"""

	def __init__(self, name, questions, answers):
		self.name = name 
		self.questions = []
		self.answers = answers

	def add_question(self, question, correct_answer):
		"""Takes in a question and answer and adds to the questions list"""
		return "question: %s, correct_answer: %s" % (question, correct_answer)
		#self.questions.append("question: %s, correct_answer: %s" % (question, correct_answer))

	def administrator(questions):
		score = 0
		for question in self.questions:
			ask_and_evaluate(question)
			if ask_and_evaluate == True:
				score += 1
			return score

###### Part 4 #######

def take_test(Exam, Student):
	Exam.administrator()
	self.score = score

def example(Exam, Student):
	Exam.add_question()
	# need to create new instance of the Student class 
	new_student = Student()
	Exam.administrator()

###### Part 5 ###### 

class Quiz(Exam):
	"""A subclass for quiz that takes some attributes from Exam"""
	
	# Not sure how to do this
	def administrator(self):
		

