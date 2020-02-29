#! /usr/bin/env python3
'''
This module is designed for python 3.6 or newer
'''
import random

mood_map = [
    ('happy', 0.25),
    ('angry', 0.25),
    ('anxious', 0.25),
    ('sad', 0.25),
]

class MoodRing:
    def __init__(self, map=mood_map):
        self.moods_opts, self.mood_probs = zip(*map)
        self.change()

    def __str__(self):
        return self.mood

    def __repr__(self):
        return self.mood

    def change(self):
        self.mood = random.choices(population=self.moods_opts,
                                   weights=self.mood_probs, 
                                   k=1)[0]



if __name__ == '__main__':
    print(MoodRing())
    #this_map = [('crank', 5), ('cryyng', 8)]
    #print(MoodRing(this_map))
