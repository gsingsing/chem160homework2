from random import choices
ntrials = 15000
player1wins = 0
rolldice = [1,2,3,4,5,6]
for i in range(ntrials):
    player2=[]
    player2=choices(rolldice, k=2)
    if player2[0] ==player2[1]:
        continue
    player1=[]
    player1=choices(rolldice, k=3)
    player1.sort(reverse=True)
    if player1[0]+player1[1]>player2[0]+player2[1]:
        player1wins=player1wins+1
ratio=player1wins/ntrials
print(ratio)
# ratio is about 0.52, which is fairly close to 50% which is a fair game.
# however player1 would still have a 2% higher chance of winning.