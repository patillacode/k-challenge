# Coding challenge

This is an optional coding exercise to learn about your approach to technical
requirements and actual coding. The idea is to solve **only one** of the code
challenges below.

Directions:

- Restrict the time to maximum 2 hours (assume easier options if/when needed)
- If you're unsure about any requirements, please assume the easier option
- Feel free to use any language, library and frameworks you think are
appropriate (although please keep it simple so we can run the test.
Simple is beautiful)


## Challenge A: Build a simple n-grams tool

Build a tool which receives a corpus of text, analyses it and reports the top
10 most frequent bigrams, trigrams, four-grams (i.e. most frequently occurring
two, three and four word consecutive combinations).

**Extra**: Use a string similarity function to aggregate the 'similar' bigrams
together: Ex: 'the-house' and 'tea-house' will be counted as the same bigram.


## Challenge B: Simple Sharding system

- There is a DB [1] with Comments.
- The object *Comment (id = number, text = string)* will provide *save()* and
*get_object_by_id(id=[number])* methods, which saves and retrieves the object
from a DB [1](see notes below).
-  Every object will be saved in one of 4 tables (tables have the same
structure and named like comment0, comment1, comment2, comment3) depending on
the object id using the Modulus function, i.e. *ID % 4 = 0, 1, 2, or 3.*

Ex: If id=317, the object will be kept in DB number 1.

-  Populate the tables with random comments (In such way that the tables are
reasonable populated with approximately same number of records).
-  Add two new tables: comment4 and comment5 and create code to rebalance
(move) the objects
according to new function: ID % 6 (as some of them will be in the "wrong"
table).

**Extra**: Change the modulus function for a consistent hashing function.


## Challenge C: Create a simple Round Robin Database tool (RRD)

-  A RRD is some sort of circular structure (list) with a fixed number of
slots to keep data.
-  It is filled in order, and once you reach the end of the list, the first
element gets overwritten. This ensures the size of the database does not grow
over the time while keeping the most recent data available.
-  This RRD will store a timestamp (epoch) and a value (float).
-  The goal is to build a two interfaces: (1) to save and (2) to query the
data.

#### Save command/interface:
- The value will be saved in two round robin structures in a DB [1]
- The first RRD will keep the values for the last hour i.e. each slot will
represent a minute within 60 minutes.
- The second keeps values per hour, for 24 hours. To determine the value per
hour to save, please choose the minimum from the list of values per minute:

i.e. valueOnHour1 = min(valueOnMinute0, valueOnMinute1, valueOnMinute2,...,
valueOnMinute59)

rrd save {epoch_timestamp} {float_to_save} (if command line or the equivalent
fields on a graphical interface):
*Ex. rrd 1345018938 33.1*

#### Query command
- retrieves the data from the RRD
- Displays the data kept on the RRD files as well as calculating average,
maximum and minimum values.
*Ex. rrd query minutes. *
Ex. output:
1345018980, 132.1
1345019040, 322.1
1345019160, NULL*
...
1345022580, 53.3
minutes: min: 53.3, avg: 403.3, max: 512.11

*rrd query hours.*
Ex. output:
1345021200, 132.1
1345024800, 122.1
...
1345028400, 453.3

hour: min: 53.3, avg: 403.3, max: 512.11

- Assume 'NULL' for slots with no information.

**Extra**:
Implement buffering so the save command could be called many times per minute
and the values get aggregated into one before saving it into the database:

ValueOnMinute1 = sum( valueOnMinute1Second34, ..., valueOnMinute1Second57)

## Notes

* The Extra section is only if you have time and/or personal interest.
* [1] DB: You can choose any persistent system or library
(please keep it simple). Some ideas: SQLite or any simple file-persistence
framework.
* When finished, please email the code along with instructions to run it.
* Don't disclose w/o authorisation
* Important: Please note this code challenge is completely optional.