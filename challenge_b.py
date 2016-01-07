#!/usr/bin/env python

# Challenge B:

# - There is a DB [1] with Comments.
# - The object *Comment (id = number, text = string)* will provide *save()* and
# *get_object_by_id(id=[number])* methods, which saves and retrieves the object
# from a DB [1](see notes below).
# -  Every object will be saved in one of 4 tables (tables have the same
# structure and named like comment0, comment1, comment2, comment3) depending on
# the object id using the Modulus function, i.e. *ID % 4 = 0, 1, 2, or 3.*

# Ex: If id=317, the object will be kept in DB number 1.

# -  Populate the tables with random comments (In such way that the tables are
# reasonable populated with approximately same number of records).
# -  Add two new tables: comment4 and comment5 and create code to rebalance
# (move) the objects
# according to new function: ID % 6 (as some of them will be in the "wrong"
# table).

# **Extra**: Change the modulus function for a consistent hashing function.


class Comment(object):
    """docstring for Comment"""
    def __init__(self, text):
        self.db = self.get_db()

    def get_db(self):
        pass

    def save(self):
        super(Comment, self)
