# Program written by Antonin CALLARD, ENS Lyon, France

# A list of very good Sans jokes and puns from Undertale and https://steamcommunity.com/sharedfiles/filedetails/?id=537274165
list_jokes = [
    "I know I can be difficult at times.\n Hope you don't have a bone to pick with me!",
    "I have got a ton of work done today.\n A skele-ton!",
    "There was once a very hard-working skeleton.\n He always worked himself down to the bone!",
    "It's easy to tell when a skeleton is lying.\n You can see right through them!",
    "Why are skeletons so calm?\n -> Because nothing gets under their skin!",
    "Why can't skeletons play church music?\n -> Because they have no organs.",
    "What do skeletons hate the most about wind?\n -> Nothing, it goes right through them.",
    "Why don't skeletons fight each other?\n -> They don't have the guts!",
    "When does a skeleton laugh?\n -> When someone tickles his funny bone!",
    "Papyrus doesn't like my hotdogs...\n Probably because he doesn't have the stomach for it!",
    "Why are graveyards so noisy?\n -> Because of all the coffin!",
    "Papyrus stood by the fire for too long.\n Now he's BONE-dry!",
    "What do skeletons say before they begin dining?\n -> Bone-Appetit!",
    "Have you seen my brother?\n -> I have a BONE to pick with him.",
    "What did the skeleton say while riding his Harley Davidson motorcycle?\n -> I'm bone to be wild!",
    "Why did the skeleton want a friend?\n -> Because they were feeling bonely... ;(",
    "Why do skeletons makes bad miners?\n -> Because they only go *6 foot under ground*!"
]

## Auxiliary functions

"""
    __filter_args(args): separate arguments into options (i.e. -[...]) and real arguments.
"""
def __filter_args(args):
    opt,filtered = [],[]
    for arg in args:
        if arg[0] == "-":
            opt.append(arg)
        else:
            filtered.append(arg)
    return opt,filtered

"""
    __filter_joke(regex): return the list of jokes matching a given regex.
"""
import re
def __filter_joke(regex):
    res = []
    for joke in list_jokes:
        pass
        # if re.match(regex, joke):
        #   res.append(joke)
    return res

import random
"""
    random_joke(): return a random joke from the list of jokes "list_jokes".
"""
def random_joke():
    pass


## Interface

import sys
help = {
    "random" : "print a random joke",
    "random <regex>" : "print a random joke matching <regex>",
    "random -n<i> <regex>" : "print i random jokes matching <regex>"
}

def main():
    cmd, *args = sys.argv[1:]
    # Get the list of options (i.e. -[...]) into options
    # and the list of real arguments into args
    options, args = __filter_args(args)
    # Parse input command
    if cmd == "random":
        print(random_joke())
    else:
        print("Help: usage of integers.py")
        for command in help:
            print("  {} : {}".format(command, help[command]))
    # Exit program
    exit()

if __name__ == "__main__":
    main()
