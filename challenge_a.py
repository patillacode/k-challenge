#!/usr/bin/env python

# Challenge A:

# Build a tool which receives a corpus of text, analyses it and reports the top
# 10 most frequent bigrams, trigrams, four-grams (i.e. most frequently
# occurring two, three and four word consecutive combinations).

# **Extra**: Use a string similarity function to aggregate the 'similar'
# bigrams together: Ex: 'the-house' and 'tea-house' will be counted as the
# same bigram.

# File path to be analyzed
INPUT = "input.txt"

# For very big texts maybe it is better to go line by line
# for commodity I split the whole text at once
# text = open(INPUT).split()
text = "My example input text, text, for easy testing, easy testing, .".split()


# Where to store the grams
# key = gram size (2, 3, 4)
# value = the actual grams - a list of lists
grams = {}
frecuent = {}
# Since we are doing bi, tri and four-grams
for gram_size in range(2, 5):
    # gram_size = n + 1
    grams[gram_size] = []
    for i in range(len(text) - gram_size):
        grams[gram_size].append(text[i:i + gram_size])

# Get the most common element within a list for each word list we have
# and store it in our frecuent dictionary
for gram_size in range(2, 5):
    frecuent[gram_size] = max(grams[gram_size], key=grams[gram_size].count)

# print results
print "\nGrams:"
for k, v in grams.iteritems():
    print "#" * 30
    print "Size", k, ":"
    for g in v:
        print g

print "\nMost frecuent:"
for k, v in frecuent.iteritems():
    print "#" * 30
    print k, ": ", " ".join(v)

# Dev Notes:
# punctuation is not treated
# case sensitive
# for same frecuency items only one (at random) will show
# beware of number of items when splitting may cause in errors
# example: "1, 1, 2, 2, 3, 4, 4, 4, "
# "4," would be the most frecuent, but by taking bigrids you don't
# take the last one, same applies for other n-grids
