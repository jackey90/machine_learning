__author__ = 'jackey90'

from recommendations import critics
from recommendations import sim_distance
from recommendations import sim_pearson
from recommendations import topMatches
from recommendations import getRecommendations
from recommendations import transformData

#print critics['Lisa Rose']
#print sim_distance(critics, "Lisa Rose", "Gene Seymour")
#print sim_distance(critics, "Mick LaSalle", "Jack Matthews")
#print topMatches(critics,"Lisa Rose", 6, sim_pearson)

#print getRecommendations(critics,'Toby')

movies=transformData(critics)
print topMatches(movies,'Just My Luck')