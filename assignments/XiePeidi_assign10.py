"""
Peidi Xie
May 10th, 2019
Introduction to Programming, Section 03
Assignment 10
"""
'''
Part 1
'''

# open the file of movie_reviews for reading mode and read in the data
# close the file
file_object = open("movie_reviews.txt", "r")
data = file_object.read()
reviews = data.split("\n")
file_object.close()

# ask the user for a word for sentiment test
word = input("Enter a word to test: ")

# count the number of times of appearance of the word
# count the sum of the scores of all movie reviews containing the word
num_reviews = 0
score_reviews = 0
for review in reviews:
    if word.lower() in review.lower():
        num_reviews += 1
        score_reviews += int(review[0])

# display to the user the number of times the word appears, the average sentiment score of the word
# and whether it is positive or not
print("'" + word + "'", "appears", num_reviews, "times")
if num_reviews == 0:
    print("There is no average score for reviews containing the word", "'" + word + "'")
    print("Cannot determine if this word is positive or negative")
else:
    average = score_reviews / num_reviews
    print("The average score for reviews containing the word", "'" + word + "'", "is", average)
    if average >= 2:
        print("This is a positive word")
    else:
        print("This is a negative word")

'''
Part 2
'''

import time

print("Initializing sentiment database")

# keep track of the time of analysis
analysis_start = time.time()

# create a dictionary to store all the words and associated data
words = dict()

# iterate over each review, clean up the string of the review
# store each individual words into the dictionary along with the number of times of appearance
# and the sum of the scores of all movie reviews containing the word
num_word = 0
for review in reviews:
    score = int(review[0])
    for i in review:
        if not i.isalpha():
            i = " "
    review_words = review.split(" ")
    for j in review_words:
        if j.lower() not in words:
            words[j.lower()] = [score, 1]
            num_word += 1
        else:
            words[j.lower()][0] += score
            words[j.lower()][1] += 1

analysis_end = time.time()
time = analysis_end - analysis_start

# display to the user the end of the analysis
print("Sentiment database initialization complete")
print("Total unique words analyzed:", num_word)
print("Analysis took", format(time, ".2f"), "seconds to complete")


# ask the user to enter a phrase, average the average sentiment scores of each words contained in the phrase
# to get the sentiment score for the phrase
# tell the user whether the phrase is positive or not
print()
phrase = input("Enter a phrase to test: ")
phrase_words = phrase.split(" ")
valid_word = 0
sum_average = 0
for k in phrase_words:
    if k.lower() in words:
        average_word = words[k.lower()][0] / words[k.lower()][1]
        print("*", "'" + k + "'", "appears", words[k.lower()][1], "times with an average rating of", average_word)
        valid_word += 1
        sum_average += average_word
    else:
        print("*", "'" + k + "'", "does not have a rating")
if valid_word > 0:
    phrase_average = sum_average / valid_word
    print("Average score for this phrase is:", phrase_average)
    if phrase_average >= 2:
        print("This is a POSITIVE phrase")
    else:
        print("This is a NEGATIVE phrase")
else:
    print("Not enough data to compute sentiment")

'''
Part 3
'''
# function:   sentiment
# input:      a string
# processing: clean up the string, make all letters lowercase and remove punctuations,
#             calculate the sentiment score of the string and return it
# output:     return the sentiment score of the string
def sentiment(string):
    for i in string:
        if i.isalpha():
            i = i.lower()
        else:
            i = " "
    string_words = string.split(" ")
    valid_word = 0
    sum_average = 0
    for j in string_words:
        if j in words:
            average_word = words[j][0] / words[j][1]
            valid_word += 1
            sum_average += average_word
    try:
        score = sum_average / valid_word
    except:
        score = 0
    return score

'''
Part 4
'''


print()
year = input("Enter a year in YY format: ")
month = input("Enter a month (1-2 digits): ")
print()

tweets_file = open("elonmusk_tweets_class.txt", "r")
data2 = tweets_file.read()
tweets = data2.split("\n")
tweets = tweets[:len(tweets)-1]
tweets_file.close()

num_tweet = 0
positive_sentiment = 0
positive_tweet = ""
for tweet in tweets:
    time = tweet[:tweet.index(" ")].split("/")
    if time[0] == month and time[2] == year:
        num_tweet += 1
        tweet = tweet[tweet.index("|")+3:]
        sentiment0 = sentiment(tweet)
        if sentiment0 > positive_sentiment:
            positive_sentiment = sentiment0
            positive_tweet = tweet


print("During this period there were", num_tweet, "tweets")
if num_tweet > 0:
    print("Most positive tweet rated at", positive_sentiment)
    print(positive_tweet)

