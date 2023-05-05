"""
Tavi Logan
Spring 2023 Contest Analysis & Improvement Plan
April 17 2023

In all 3 contests taken, a significant portion of the time I'd allotted myself was
wasted on a single problem - I approached these contests attempting to challenge myself
as much as possible attempting problem types I was unfamiliar with, rather than complete 
as many questions as possible in the time available.
As such, a lot of the easy points were left to waste so I could focus my little time on 
problems I found interesting. If I were to participate in an actual programming competition
I would likely take a different approach, but I'm here for practice, not points, so whatever.


Weaknesses
    The most popular lecture problem type this semester seemed to be graph traversal, 
    so I attempted a couple problems with a graph traversal solution, and found it to
    be much harder than anticipated simply due to being unfamiliar with implementing them.
    Although I was able to theorize solutions for these problems, I wasn't able to successfully
    put my solution into code.

Improvement Problems:

Lineup -> Bronze
    I was actually able to get this problem pretty quick with a greedy approach, but attempting to get a graph-based solution
    was actually pretty tough. I ended up iterating through the options in alphabetical order, but skipping over any that
    had two neighbors. If a particular option had a necessary neighbor, I would add that neighbor, and then recurse through 
    adding its other necessary neighbors that were not already in the solution.

Planting -> Silver
    Surprisingly, the silver problem I tried was far easier than the bronze problem. The problem in finding how many
    distinct types of grass were necessary when it was not allowed for the same type of grass to be adjacent or separated by
    only one node. This one was simple - for any node, there had to be a number of grass types equal to itself and its
    neighbors, since each neighbor could not be the same. The solution, then, was the most constrained node, which was simply
    the one with the most neighbors

Moocast -> Silver
    I came up with a solution that appears to work, but times out of test cases. The goal of the problem was
    to find the maximum number of cows reachable from a single walkie talkie broadcast. To accomplish this, I first had to 
    build the graph. I sorted the cows by their x coordinate, then iterated through them, checking the distance of each 
    until the x distance of the cow being tested was greater than the strength of the walkie talkie. Then I just had
    to recursively search through each potential starting node to find the number of cows each could reach, and take the maximum.
    I also had some difficulty stemming from the fact that the distance was not specified as being Euclidean or Manhattan, and
    it took some test submissions simply to figure that out, which would not have been possible in a real contest, but would
    be known in any real use case, so whatev.
    There are certainly ways that I could've more efficiently accomplished this. I could further break the graph into "regions"
    of communicativity as I tested, to more efficiently process on subsequent tests. While scanning left -> right I could
    build a directed graph by also checking the distance against the strength of the other walkie talk, which would mean I
    wouldn't have to scan right -> left afterwards.
    """


