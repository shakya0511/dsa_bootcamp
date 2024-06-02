# we have competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
# we have results = [0,0,1]
# deduce UniqueTeams = ["HTML", "C#", "Python"]
# for each win team will get 3 points and 0 points if looses
### pseudo code
# for each index in competition if "0" means index[0] str will be +3  
    # if "1" means index[1] will be +3 





def Solution1(competitions, results):

    teams = []
    for matches in competitions:
        for team in matches:
            teams.append(team)
    UniqueTeams = set(teams)
    UniqueTeams = {element: 0 for element in UniqueTeams}
    
    # for score,match in zip(results,competitions):
    # for match in range(len(competitions)-1):
    idx = 0
    while idx < (len(results)):
        if results[idx] == 0:
            winner = competitions[idx][1]
            UniqueTeams[winner] += 3

        if results[idx] == 1:
            winner = competitions[idx][0]
            UniqueTeams[winner] += 3
        idx +=1
        
            

    final_winner = max(UniqueTeams, key=UniqueTeams.get)


    return str(final_winner)

competitions = [
    ["HTML", "C#"],
    ["C#", "Python"],
    ["Python", "HTML"]
]

result = [0,0,1]


Solution1(competitions,result)