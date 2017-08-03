# Questions and Answers - The following is code that assigns global variables to question strings
# and answer lists.  These variables will be returned by a function that takes a user chosen
# difficulty level as input, and returns the appropriate question and answer.

# Easy mode

easy_question = '''\nThe capital of Germany is __1__. In 1936, Berlin hosted the Summer __2__.
After World War II, the city was split between east and __3__. In 1989, the city was reunified 
with the destruction of the Berlin __4__.\n'''

easy_answers = ['Berlin','Olympics','west','wall']

# Medium mode

medium_question = '''\nThe capital of France is __1__. Two well known tourist attractions in
this city are the __2__ tower and the __3__ art museum, which houses the famous Mona __4__
painting.\n'''

medium_answers = ['Paris','Eiffel','Louvre','Lisa']

# Hard mode

hard_question = '''\nThe capital of Belgium is __1__. This city is the administrative centre of
the __2__ Union and the North Atlantic __3__ Organization. The primary languages 
spoken in this city are French and __4__.\n'''

hard_answers = ['Brussels','European','Treaty','Dutch']


# The blank_spaces list contains string objects that will be passed into the game_play function
# when a user guesses the correct answer.  Each string object will be searched for within the 
# appropriate question string and replaced with the appropriate answer string.

blank_spaces = ['__1__','__2__','__3__','__4__']


# The acceptable_answers function ensures that a user is choosing a correct difficulty level.  It
# takes the user input from the game_level_choice function and returns True or False based on this
# check.
def acceptable_answers(user_difficulty_level_choice):
     acceptable_answers_list = ['easy','medium','hard']
     if str.lower(user_difficulty_level_choice) in acceptable_answers_list:
          return True
     else:
          return False


# The game_level_choice function takes a difficulty level choice as user input, and returns
# 2 global variables that are assigned the appropriate question and answers based on that
# choice.

def game_level_choice(level_choice):
     while acceptable_answers(level_choice) == False:
          print
          print 'Not a valid mode...'
          level_choice = raw_input('Choose easy, medium, or hard: ')
          print
     if str.lower(level_choice) == 'easy':
          print "\nYou've chosen easy mode!\n"
          print easy_question
          return (easy_question, easy_answers)
     if str.lower(level_choice) == 'medium':
          print "\nYou've chosen medium mode!\n"
          print medium_question
          return (medium_question, medium_answers)
     if str.lower(level_choice) == 'hard':
          print "\nYou've chosen hard mode!  So brave!\n"
          print hard_question
          return (hard_question, hard_answers)


# The play_game function initiates the game by first printing the rules for the user.  It
# then calls the game_level_choice function and assigns variables to its output which are
# the question and answers for the selected difficulty level.  It then prints the question
# string and prompts the user to guess which answers go in the blank spaces.  The user gets
# 4 tries for each blank.  If they type an answer that matches the appropriate string in
# the answers list, the blank is replaced with the correct answer, and the updated question
# string printed for the user.  The user is then asked to guess what goes in the next blank.
# This continues until the user guesses all of the blanks correctly.  

def play_game(question_string, answer_list):
     answer_index = 0
     while answer_index < len(answer_list):
          guess_count = 1
          guess = raw_input('What word should replace ' + blank_spaces[answer_index] + '? ')
          while str.lower(guess) != str.lower(answer_list[answer_index]):
               if guess_count == 4:
                    print '\nYou have exceeded the number of guesses!\n'
                    quit()
               else:
                    print '\nThat is not the correct answer, try again.  Guesses remaining: ', 4 - guess_count
                    guess_count += 1
                    print question_string
                    guess = raw_input('What word should replace ' + blank_spaces[answer_index] + '? ')
          if str.lower(guess) == str.lower(answer_list[answer_index]):
               print 'You got it right!'
               question_string = question_string.replace(blank_spaces[answer_index],answer_list[answer_index])
               print question_string
          answer_index += 1
     print 'You won!'

# Calls the play_game function which allows the user to play the game!
print '''\n\nThis is a fill in the blank quiz.\n\nYou will be asked to read a paragraph and 
guess which words should replace the blank spaces.\n\nPlease start by choosing a difficulty 
level.\n'''

question_string, answer_list = game_level_choice(raw_input('Choose easy, medium, or hard: '))

play_game(question_string, answer_list)



