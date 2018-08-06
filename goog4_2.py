# Distract the Guards
# ===================

# The time for the mass escape has come, and you need to distract the guards so that the bunny prisoners can make it out! 
# Unfortunately for you, they're watching the bunnies closely. Fortunately, this means they haven't realized yet that the space 
# station is about to explode due to the destruction of the LAMBCHOP doomsday device. Also fortunately, all that time you spent working 
# as first a minion and then a henchman means that you know the guards are fond of bananas. And gambling. And thumb wrestling.

# The guards, being bored, readily accept your suggestion to play the Banana Games.

# You will set up simultaneous thumb wrestling matches. In each match, two guards will pair off to thumb wrestle. 
# The guard with fewer bananas will bet all their bananas, and the other guard will match the bet. The winner will receive all of 
# the bet bananas. You don't pair off guards with the same number of bananas (you will see why, shortly). You know enough guard 
# psychology to know that the one who has more bananas always gets over-confident and loses. Once a match begins, the pair of 
# guards will continue to thumb wrestle and exchange bananas, until both of them have the same number of bananas. Once that happens, 
# both of them will lose interest and go back to guarding the prisoners, and you don't want THAT to happen!

# For example, if the two guards that were paired started with 3 and 5 bananas, after the first round of thumb wrestling 
# they will have 6 and 2 (the one with 3 bananas wins and gets 3 bananas from the loser). After the second round, they will have 
# 4 and 4 (the one with 6 bananas loses 2 bananas). At that point they stop and get back to guarding.

# How is all this useful to distract the guards? Notice that if the guards had started with 1 and 
# 4 bananas, then they keep thumb wrestling! 1, 4 -> 2, 3 -> 4, 1 -> 3, 2 -> 1, 4 and so on.

# Now your plan is clear. You must pair up the guards in such a way that the maximum number of guards go into
# an infinite thumb wrestling loop!

# Write a function answer(banana_list) which, given a list of positive integers depicting the amount of 
# bananas the each guard starts with, returns the fewest possible number of guards that will be left to 
# watch the prisoners. Element i of the list will be the number of bananas that guard i (counting from 0) starts with.

# The number of guards will be at least 1 and not more than 100, and the number of bananas each guard 
# starts with will be a positive integer no more than 1073741823 (i.e. 2^30 -1). Some of them stockpile a LOT of bananas.

# Test cases
# ==========

# Inputs:
#    (int list) banana_list = [1, 1]
# Output:
#    (int) 2

# Inputs:
#    (int list) banana_list = [1, 7, 3, 21, 13, 19]
# Output:
#    (int) 0
class Graph:
    def __init__(self, banana_list):
        self.length = len(banana_list)
        self.graph = list([0]*self.length for i in xrange(self.length))
        for i in xrange(self.length):
            for j in xrange(self.length):
                if i < j: 
                    self.graph[i][j] = dead_lock(banana_list[i], banana_list[j])
                    self.graph[j][i] = self.graph[i][j] 


def gcd(a, b):
    while(b):
        a, b = b, a % b
    return a

def dead_lock(a, b):
    if a == b:
        return 0
    denom = gcd(a,b)
    if (a + b) % 2 == 1:
        return 1
    a, b = a/denom, b/denom
    a, b = max(a, b), min(a, b)    
    return dead_lock(a - b,2 * b)

def power(a):
    plus = a + 1
    while (plus != 1):
        if (plus % 2 != 0):
            return False
        plus = plus / 2
    return True

def isSpecial(m, n):
    X = m / n
    powerof = X.bit_length() - 1 if power(X - 1) and X != 1 else X.bit_length()
    if m == (n * ((2**powerof) -1)) + 2**powerof:
        return True
    return False

def between(a, b):
    m = max(a,b)
    n = min(a,b)
    mod = m % n
    if mod == 0 and power(m / n):
        return False
    elif power(n) and isSpecial(m, n):
        return False
    return True

def make_graph(banana_list):
    graph = [[0]*len(banana_list) for i in xrange(len(banana_list))]
    for i in xrange(len(banana_list)):
        for j in xrange(i, len(banana_list)):
            if banana_list[j] != banana_list[i] and between(banana_list[i], banana_list[j]):
                graph[i][j] = 1
                graph[j][i] = graph[i][j]
    return graph


def answer(banana_list):
    graph = make_graph(banana_list)
    counts = {x:len(graph[x]) for x in graph}
    unoccupied = len(banana_list)
    paired = []
    #while len(paired) < len(banana_list):
    #    fewest = min(counts, key=counts.get)
    #    if len(graph[fewest]) == 0:
    #        paired.append(fewest)
    #print(min(counts, key=counts.get))
banana_list = [1,7]
#answer(banana_list)