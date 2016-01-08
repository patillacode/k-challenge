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

import shelve
import sys


class Comment(object):
    """docstring for Comment"""
    def __init__(self, obj_id, text):
        self.id = obj_id
        self.text = text
        self.db_number = self.id % 4

    def get_object_by_id(self, obj_id):
        db = self.open_db()
        obj = db[str(obj_id)]
        db.close()
        return obj

    def save(self):
        db = self.open_db()
        db[str(self.id)] = self
        db.close()

    def open_db(self):
        db_name = "comment{0}".format(self.db_number)
        return shelve.open(db_name)


def populate(items_number):
    print "Populating...",
    for i in range(items_number):
        c = Comment(i, "test_{0}".format(i))
        c.save()
    print "done"


def rebalance():
    print "Balancing...",
    for i in range(4):
        db = shelve.open("comment{0}".format(i))
        for k in db.keys():
            new_table = int(k) % 6
            # when in the wrong table we delete it
            # and add it to the new one
            if new_table != i:
                new_db = shelve.open("comment{0}".format(new_table))
                new_db[k] = db[k]
                db.pop(k)
    print "done"


if __name__ == '__main__':
    try:
        if len(sys.argv) not in (1, 2):
            raise
        elif len(sys.argv) == 1:
            populate(100)
        else:
            items = sys.argv[1]
            assert(items.isdigit)
            populate(int(items))
        rebalance()
    except:
        print "Usage: python challenge_b.py <items_number>"
