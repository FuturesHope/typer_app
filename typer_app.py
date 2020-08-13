#
# Create an app to help user type faster.
# Give him a word to type it five times
# collect data on typing timing on each cycle
# tell the user how many mistakes were made during the exercise
# show a chart with the typing speed evolution
import time as t
import matplotlib.pyplot as plt
import random
import sys

# create a list for 3 words from user input
user_wordlist = []

# Introduce the user to the app
print('Greetings User of "Typer Train App", which should help you practice typing words faster in a scientific way. ')
# Let user know that the app asks user for three words and add to the list
print('You will be asked for one word that contains 5 chars minimum, one of words will be picked fo you automatically')


# validate that the word contains only and min 5 letters  - use str.isalpha()
# this while block should populate the list with 3 valid words
while(len(user_wordlist)<1):
    usr_input = input('Please provide your word: ')
    if usr_input.isalpha():
        if len(usr_input)<5:
            print('Please provide a word of 5 letter minimum ')
            continue
        print('The word "{}" is validated and saved'.format(usr_input))
        user_wordlist.append(usr_input)
    else:
        print('Please provide a word consisting only of letters ')
        continue
# let the user know what word was chosen for training
# random_index = random.randint(0,len(user_wordlist)-1)
chosen_word = user_wordlist[0]
# print('Your chosen word for training is: {}'.format(chosen_word))

# create a container for user typed words
user_typed_words = []
time_stamps = []
timing_data = []


# ask the user if he is ready to start and press enter
input('Pres enter when you ready to start typing the chosen word 5 times, the timer will start')
for x in range(5):
    time_stamps.append(t.time())
    user_typed_words.append(input('type it now..  '))
    time_stamps.append(t.time())

print('\n')
print('User typed words are: {}'.format(user_typed_words))
print('\n')
# show the number of mistakes
mistakes_counter = 0
for word in user_typed_words:
    if word.lower() != chosen_word.lower():
        mistakes_counter+=1
print('Mistakes are made in {} words.'.format(mistakes_counter))
# wait 3 sec for user reading the final results from the screen
t.sleep(3)
# print('The typing timing_data is: {}'.format(timing_data))
# append the timings of typing to the list of timing_data
for x in range(1,len(time_stamps),2):
    timing_data.append(time_stamps[x] - time_stamps[x-1])
# use pyplot to show the progress of typing
# create labels for x axis, show the plot
x_axis = [1,2,3,4,5]
plt.bar(x_axis, timing_data)
plt.ylabel('Timing in sec')
plt.xlabel('Attempts')
plt.title('Your word typing timing results')
plt.show()

print('You might need to press CTRL + "C" or "Z" to finally exit the training game')
