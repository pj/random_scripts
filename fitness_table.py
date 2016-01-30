#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2016 pauljohnson <pauljohnson@Paul-Johnsons-MacBook-Pro.local>
#
# Distributed under terms of the MIT license.

"""
Generate a series of workouts for stronglifts 5x5
"""

from datetime import timedelta, date
from collections import defaultdict

sessions = [
    (0, ["Squat", "Bench Press", "Barbell Row"]),
    (2, ["Squat", "Overhead Press", "Deadlift"]),
    (4, ["Squat", "Bench Press", "Barbell Row"]),
    (7, ["Squat", "Overhead Press", "Deadlift"]),
    (9, ["Squat", "Bench Press", "Barbell Row"]),
    (11, ["Squat", "Overhead Press", "Deadlift"])
]

weights = {
    "Squat": 62.5,
    "Bench Press": 42.5,
    "Barbell Row": 32.5,
    "Overhead Press": 30.0,
    "Deadlift": 65.0
}

reps = defaultdict(lambda: "5x5", Deadlift="1x5")

INCREMENT = 2.5
FORTNIGHTS = 4

start_date = date(2016, 2, 1)


def get_suffix(day):
    if 4 <= day <= 20 or 24 <= day <= 30:
        return "th"
    else:
        return ["st", "nd", "rd"][day % 10 - 1]

for fortnight in xrange(0, FORTNIGHTS):
    for offset, exercises in sessions:
        exercise_date = start_date + timedelta(weeks=fortnight*2, days=offset)

        suffix = get_suffix(exercise_date.day)

        formatted_date = exercise_date.strftime(
                             '"%A %-d{}, %B %Y"').format(suffix)

        if offset == 0 or offset == 7:
            weights = {k: v + INCREMENT for (k, v) in weights.iteritems()}

        for d, exercise in zip([formatted_date, "", ""], exercises):
            print ",".join([d, exercise,
                            str(weights[exercise]), reps[exercise]])

        print ",,,"
