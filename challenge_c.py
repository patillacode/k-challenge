#!/usr/bin/env python

# Challenge C: Create a simple Round Robin Database tool (RRD)

# -  A RRD is some sort of circular structure (list) with a fixed number of
# slots to keep data.
# -  It is filled in order, and once you reach the end of the list, the first
# element gets overwritten. This ensures the size of the database does not grow
# over the time while keeping the most recent data available.
# -  This RRD will store a timestamp (epoch) and a value (float).
# -  The goal is to build a two interfaces: (1) to save and (2) to query the
# data.

# Save command/interface:
# - The value will be saved in two round robin structures in a DB [1]
# - The first RRD will keep the values for the last hour i.e. each slot will
# represent a minute within 60 minutes.
# - The second keeps values per hour, for 24 hours. To determine the value per
# hour to save, please choose the minimum from the list of values per minute:

# i.e. valueOnHour1 = min(valueOnMinute0, valueOnMinute1, valueOnMinute2,...,
# valueOnMinute59)

# rrd save {epoch_timestamp} {float_to_save} (if command line or the equivalent
# fields on a graphical interface):
# *Ex. rrd 1345018938 33.1*

# Query command
# - retrieves the data from the RRD
# - Displays the data kept on the RRD files as well as calculating average,
# maximum and minimum values.
# *Ex. rrd query minutes. *
# Ex. output:
# 1345018980, 132.1
# 1345019040, 322.1
# 1345019160, NULL*
# ...
# 1345022580, 53.3
# minutes: min: 53.3, avg: 403.3, max: 512.11

# *rrd query hours.*
# Ex. output:
# 1345021200, 132.1
# 1345024800, 122.1
# ...
# 1345028400, 453.3

# hour: min: 53.3, avg: 403.3, max: 512.11

# - Assume 'NULL' for slots with no information.

# **Extra**:
# Implement buffering so the save command could be called many times per minute
# and the values get aggregated into one before saving it into the database:

# ValueOnMinute1 = sum( valueOnMinute1Second34, ..., valueOnMinute1Second57)
