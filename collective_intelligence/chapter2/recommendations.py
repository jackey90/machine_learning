# A dictionary of movie critics and their ratings of a small
# set of movies
critics = {
    "Lisa Rose": {
        "Lady in the Water": 2.5,
        "Snakes on a Plane": 3.5,
        "Just My Luck": 3,
        "Superman Returns": 3.5,
        "You, Me and Dupree": 2.5,
        "The Night Listener": 3
    },
    "Gene Seymour": {
        "Lady in the Water": 3,
        "Snakes on a Plane": 3.5,
        "Just My Luck": 1.5,
        "Superman Returns": 5,
        "The Night Listener": 3,
        "You, Me and Dupree": 3.5
    },
    "Michael Phillips": {
        "Lady in the Water": 2.5,
        "Snakes on a Plane": 3,
        "Superman Returns": 3.5,
        "The Night Listener": 4
    },
    "Claudia Puig": {
        "Snakes on a Plane": 3.5,
        "Just My Luck": 3,
        "The Night Listener": 4.5,
        "Superman Returns": 4,
        "You, Me and Dupree": 2.5
    },
    "Mick LaSalle": {
        "Lady in the Water": 3,
        "Snakes on a Plane": 4,
        "Just My Luck": 2,
        "Superman Returns": 3,
        "The Night Listener": 3,
        "You, Me and Dupree": 2
    },
    "Jack Matthews": {
        "Lady in the Water": 3,
        "Snakes on a Plane": 4,
        "The Night Listener": 3,
        "Superman Returns": 5,
        "You, Me and Dupree": 3.5
    },
    "Toby": {
        "Snakes on a Plane": 4.5,
        "You, Me and Dupree": 1,
        "Superman Returns": 4
    }
}

import math

def sim_distance(data, person1, person2):
    si = {}
    for item in data[person1]:
        if item in data[person2]:
            si[item] = 1
    if len(si) == 0: return 0
    sum_of_squares = sum(
        [pow(data[person1][item] - data[person2][item], 2) for item in data[person1] if item in data[person2]])
    return 1 / (1 + sum_of_squares)


def sim_pearson(data, p1, p2):
    si = {}
    for item in data[p1]:
        # find the same item
        if item in data[p2]: si[item] = 1
    n = len(si)
    if n == 0: return 0

    sum1 = sum([data[p1][it] for it in si])
    sum2 = sum([data[p2][it] for it in si])

    sum1Sq = sum([pow(data[p1][it], 2) for it in si])
    sum2Sq = sum([pow(data[p2][it], 2) for it in si])

    pSum = sum([data[p1][it] * data[p2][it] for it in si])

    num = pSum - (sum1 * sum2 / n)

    den = math.sqrt((sum1Sq - pow(sum1, 2) / n) * (sum2Sq - pow(sum2, 2) / n))

    if den == 0: return 0

    r = num / den
    return r


def topMatches(data,person,n=5,similarity=sim_pearson):
    scores=[(similarity(data,person,other),other) for other in data if other != person]

    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommendations(data,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in data:
        #skip self
        if other == person: continue
        sim = similarity(data,person,other)
        if sim <= 0 : continue

        for item in data[other]:
            # item not in my list
            if item not in data[person] or data[person][item] == 0:
                totals.setdefault(item,0)
                totals[item] += data[other][item]*sim
                simSums.setdefault(item,0)
                simSums[item] += sim

    rankings=[(total/simSums[item],item) for item,total in totals.items()]
    rankings.sort()
    rankings.reverse()
    return rankings

def transformData(data):
    result={}
    for person in data:
        for item in data[person]:
            result.setdefault(item,{})

            result[item][person]=data[person][item]
    return result

