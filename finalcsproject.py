import random

fh=open('gamedata.txt','a')

# ---------------- TEAM DATA ---------------- #
teams = {
    "INDIA": ['Rohit Sharma(C)','Shubman Gill','Virat Kohli','Shreyas Iyer','KL Rahul(WK)',                          
              'Hardik Pandya','Ravindra Jadeja','Kuldeep Yadav','Jasprit Bumrah',
              'Mohammed Shami','Mohammed Siraj'],

    "AUSTRALIA": ['David Warner','Travis Head','Steve Smith','Marnus Labuschagne',
                  'Glenn Maxwell','Mitchell Marsh','Alex Carey(WK)','Pat Cummins(C)',
                  'Mitchell Starc','Josh Hazlewood','Adam Zampa'],

    "ENGLAND": ['Jonny Bairstow','Jos Buttler(C & WK)','Joe Root','Ben Stokes',
                'Harry Brook','Moeen Ali','Sam Curran','Chris Woakes',
                'Mark Wood','Adil Rashid','Reece Topley'],

    "PAKISTAN": ['Babar Azam(C)','Imam-ul-Haq','Mohammad Rizwan(WK)','Fakhar Zaman',
                     'Iftikhar Ahmed','Shadab Khan','Mohammad Nawaz','Shaheen Afridi',
                     'Haris Rauf','Naseem Shah','Hasan Ali'],

    "SOUTHAFRICA": ['Quinton de Kock(WK)','Temba Bavuma(C)','Rassie van der Dussen',
                        'Aiden Markram','Heinrich Klaasen','David Miller','Marco Jansen',
                        'Kagiso Rabada','Anrich Nortje','Keshav Maharaj','Lungi Ngidi'],

    "NEWZEALAND": ['Devon Conway','Finn Allen','Kane Williamson','Daryl Mitchell',
                       'Glenn Phillips','Tom Latham(WK)','Mitchell Santner','Tim Southee(C)',
                       'Trent Boult','Lockie Ferguson','Ish Sodhi']
}

overs=int(input('Enter no. of overs you want to play:'))                                # no of overs to play the game

print('\n---------------- TEAM SELECTION ----------------')
print("\nAvailable Teams:", list(teams.keys()))
team1=input("\nEnter your team: ").upper()                                              #input the new team if you want 
team2=input("\nEnter opponent team: ").upper()
print('\nTeam 1 playing 11 is',teams[team1])
print('\nTeam 2 playing 11 is',teams[team2])
changesteam1=input('\nIf you want to change playing 11 of team1 then type YES otherwise NO:').upper()
if changesteam1=='YES':
    nochanges=int(input('\nEnter no. of changes in playing 11:'))
    for i in range(0,nochanges):
        position=int(input('\nEnter posion at which you want to change:'))
        name=input('\nEnter player name you wanted')
        teams[team1][position-1]=name
changesteam2=input('\nIf you want to change playing 11 of team2 then type YES otherwise NO:').upper()
if changesteam2=='YES':
    nochanges1=int(input('\nEnter no. of changes in playing 11:'))
    for j in range(0,nochanges1):
        position1=int(input('\nEnter posion at which you want to change:'))
        name1=input('\nEnter player name you wanted')
        teams[team2][position1-1]=name1
print('\nTeam 1 current playing 11 is',teams[team1])
print('\nTeam 2 current playing 11 is',teams[team2])

print("\n", team1, "VS", team2)

# ---------------- TOSS ---------------- #
toss_winner = random.choice([team1, team2])                         #for toss random function is used 
print("\nToss won by:", toss_winner)

if toss_winner == team1:
    choice = input("\n team 1 has to Choose BAT or BOWL: ").upper()
    if choice == "BAT":
        bat_team = teams[team1]
        bowl_team = teams[team2]
        batteam = team1
        bowlteam = team2
    if choice == "BOWL":
        bawl_team = teams[team1]
        bat_team = teams[team2]
        batteam = team2
        bowlteam = team1
else:
    choice1 = input("\n team 2 has to Choose BAT or BOWL: ").upper()
    if choice1 == "BAT":
        bat_team = teams[team2]
        bowl_team = teams[team1]
        batteam = team2
        bowlteam = team1
    if choice1 == "BOWL":
        bowl_team = teams[team2]
        bat_team = teams[team1]
        batteam = team1
        bowlteam = team2
    

# ---------------- MATCH DATA ---------------- #
bowls = ["bouncer","yorker","slower","slot"                                       #these are important data for the game 
         ,"swing","googly","leg spin","off spin"]

shots = ["cover drive","straight drive","square cut",
         "pull","hook","inside out","defence","leave","cut"]

# ==========================================================
#                       FIRST INNINGS
# ==========================================================

runs = 0
wickets = 0
next_batsman = 2

striker = bat_team[0]
non_striker = bat_team[1]

print("\n--- FIRST INNINGS START (",overs," OVERS) ---")
print("\nOpeners:", striker, "&", non_striker)

for over in range(1,overs+1):                                           #loop for the no of overs in the game 
    print("\nOver:", over)
    for ball in range(1, 7):
        if wickets == 11:
            print("Team all out!")
            break                                                      #its is used for moving to next inning as all 11 players are out 

        delivery = random.choice(bowls)                                # random function is used for different balls , it make a element of real game 
        print("\nBall", ball, "| Delivery:", delivery)
        print("\nStriker:", striker)

        if delivery == "bouncer":                                        # these are condition so that for a certain ball , there is a different shot
            print("\nAvailable shots:", shots)                      
            short=input("\nPlay short: ").upper()
            if short in ["STRAIGHT DRIVE","COVER DRIVE","INSIDE OUT"]:
                print("\nBouncer! Catch out") 
                wickets += 1
                print("Score:", runs, "/", wickets)
                if next_batsman < len(bat_team):
                    striker = bat_team[next_batsman]
                    next_batsman += 1                                   # it is for counting no of wickets 
            if short in ["DEFENCE","LEAVE","CUT"]:
                print("\nA dot boll")
                print("Score:", runs, "/", wickets)
            if short in ["SQUARE CUT","PULL"]:
                print("\nIts a 4")
                runs=runs+4
                print("Score:", runs, "/", wickets)
            if short in ["HOOK"]:
                print("\nA massive 6")
                runs=runs+6
                print("Score:", runs, "/", wickets)
                
        if delivery == "yorker":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","SQUARE CUT","PULL","HOOK","INSIDE OUT","LEAVE"]:
                print("\nYorker! Clean bold") 
                wickets += 1
                print("Score:", runs, "/", wickets)
                if next_batsman < len(bat_team):
                    striker = bat_team[next_batsman]
                    next_batsman += 1
            if short in ["DEFENCE"]:
                print("\nA dot ball")
                print("Score:", runs, "/", wickets)

        if delivery == "slower":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["PULL","HOOK","DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs, "/", wickets)
            if short in ["COVER DRIVE","STRAIGHT DRIVE","SQUARE CUT","INSIDE OUT"]:
                print("\nIts a 4")
                runs=runs+4
                print("Score:", runs, "/", wickets)

        if delivery == "slot":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs, "/", wickets)
            if short in ["COVER DRIVE","STRAIGHT DRIVE","SQUARE CUT","PULL","INSIDE OUT"]:
                print("\nIts an 4")
                runs=runs+4
                print("Score:", runs, "/", wickets)
            if short in ["HOOK"]:
                print("\nA massive 6")
                runs=runs+6
                print("Score:", runs, "/", wickets)

        if delivery == "swing":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","LEAVE"]:
                print("\nWhat a swing,Its an edge! Catch out") 
                wickets += 1
                print("Score:", runs, "/", wickets)
                if next_batsman < len(bat_team):
                    striker = bat_team[next_batsman]
                    next_batsman += 1
            if short in ["INSIDE OUT"]:
                print("\nIts an 4")
                runs=runs+4
                print("Score:", runs, "/", wickets)
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE"]:
                print("\nA dot ball")
                print("Score:", runs, "/", wickets)

        if delivery == "googly":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","INSIDE OUT"]:
                print("\nWhat a googly,Its an edge! Catch out") 
                wickets += 1
                print("Score:", runs, "/", wickets)
                if next_batsman < len(bat_team):
                    striker = bat_team[next_batsman]
                    next_batsman += 1
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs, "/", wickets)

        if delivery == "leg spin":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","LEAVE"]:
                print("\nWhat a spin,Its an edge! Catch out") 
                wickets += 1
                print("Score:", runs, "/", wickets)
                if next_batsman < len(bat_team):
                    striker = bat_team[next_batsman]
                    next_batsman += 1
            if short in ["INSIDE OUT"]:
                print("\nIts a 4")
                runs=runs+4
                print("Score:", runs, "/", wickets)
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE"]:
                print("\nA dot ball")
                print("Score:", runs, "/", wickets)

        if delivery == "off spin":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["STRAIGHT DRIVE"]:
                print("\nWhat a spin,Its an edge! Catch out") 
                wickets += 1
                print("Score:", runs, "/", wickets)
                if next_batsman < len(bat_team):
                    striker = bat_team[next_batsman]
                    next_batsman += 1
            if short in ["COVER DRIVE","INSIDE OUT"]:
                print("\nIts an 4")
                runs=runs+4
                print("Score:", runs, "/", wickets)
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs, "/", wickets)

    # Strike change after over
    striker, non_striker = non_striker, striker

print("\nEnd of 1st Innings:", runs, "/", wickets)                        #it is score card for 1st inning !!!!

# ==========================================================
#                       SECOND INNINGS
# ==========================================================

target = runs + 1
runs2 = 0
wickets2 = 0
next_batsman2 = 2

striker = bowl_team[0]
non_striker = bowl_team[1]
print("\n--- SECOND INNINGS START (",overs,"OVERS) ---")                          #start of new inning
print("Target:", target)                                                          #target for team so it can give real match vibe


for over in range(1,overs+1):   
    print("\nOver:", over)
    for ball in range(1, 7):
        if wickets2 == 11 or runs2 >= target:
            break

        delivery = random.choice(bowls)
        print("\nBall", ball, "| Delivery:", delivery)
        print("Striker:", striker)

        if delivery == "bouncer":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["STRAIGHT DRIVE","COVER DRIVE","INSIDE OUT"]:
                print("\nBouncer! Catch out") 
                wickets2 += 1
                print("Score:", runs2, "/", wickets2)
                if next_batsman < len(bat_team):
                    striker = bowl_team[next_batsman2]
                    next_batsman2 += 1
            if short in ["DEFENCE","LEAVE","CUT"]:
                print("\nA dot boll")
                print("Score:", runs2, "/", wickets2)
            if short in ["SQUARE CUT","PULL"]:
                print("\nIts a 4")
                runs2=runs2+4
                print("Score:", runs2, "/", wickets2)
            if short in ["HOOK"]:
                print("\nA massive 6")
                runs2=runs2+6
                print("Score:", runs2, "/", wickets2)
                
        if delivery == "yorker":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","SQUARE CUT","PULL","HOOK","INSIDE OUT","LEAVE"]:
                print("\nYorker! Clean bold") 
                wickets2 += 1
                print("Score:", runs2, "/", wickets2)
                if next_batsman < len(bat_team):
                    striker = bowl_team[next_batsman2]
                    next_batsman2 += 1
            if short in ["DEFENCE"]:
                print("\nA dot ball")
                print("Score:", runs2, "/", wickets2)

        if delivery == "slower":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["PULL","HOOK","DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs2, "/", wickets2)
            if short in ["COVER DRIVE","STRAIGHT DRIVE","SQUARE CUT","INSIDE OUT"]:
                print("\nIts a 4")
                runs2=runs2+4
                print("Score:", runs2, "/", wickets2)

        if delivery == "slot":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs2, "/", wickets2)
            if short in ["COVER DRIVE","STRAIGHT DRIVE","SQUARE CUT","PULL","INSIDE OUT"]:
                print("\nIts an 4")
                runs2=runs2+4
                print("Score:", runs2, "/", wickets2)
            if short in ["HOOK"]:
                print("\nA massive 6")
                runs2=runs2+6
                print("Score:", runs2, "/", wickets2)

        if delivery == "swing":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","LEAVE"]:
                print("\nWhat a swing,Its an edge! Catch out") 
                wickets2 += 1
                print("Score:", runs2, "/", wickets2)
                if next_batsman < len(bat_team):
                    striker = bowl_team[next_batsman2]
                    next_batsman2 += 1
            if short in ["INSIDE OUT"]:
                print("\nIts an 4")
                runs2=runs2+4
                print("Score:", runs2, "/", wickets2)
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE"]:
                print("\nA dot ball")
                print("Score:", runs2, "/", wickets2)

        if delivery == "googly":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","INSIDE OUT"]:
                print("\nWhat a googly,Its an edge! Catch out") 
                wickets2 += 1
                print("Score:", runs2, "/", wickets2)
                if next_batsman < len(bat_team):
                    striker = bowl_team[next_batsman2]
                    next_batsman2 += 1
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs2, "/", wickets2)

        if delivery == "leg spin":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["COVER DRIVE","STRAIGHT DRIVE","LEAVE"]:
                print("\nWhat a spin,Its an edge! Catch out") 
                wickets2 += 1
                print("Score:", runs2, "/", wickets2)
                if next_batsman < len(bat_team):
                    striker = bowl_team[next_batsman2]
                    next_batsman2 += 1
            if short in ["INSIDE OUT"]:
                print("\nIts a 4")
                runs2=runs2+4
                print("Score:", runs2, "/", wickets2)
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE"]:
                print("\nA dot ball")
                print("Score:", runs2, "/", wickets2)

        if delivery == "off spin":
            print("\nAvailable shots:", shots)
            short=input("\nPlay short: ").upper()
            if short in ["STRAIGHT DRIVE"]:
                print("\nWhat a spin,Its an edge! Catch out") 
                wickets2 += 1
                print("Score:", runs2, "/", wickets2)
                if next_batsman < len(bat_team):
                    striker = bowl_team[next_batsman2]
                    next_batsman2 += 1
            if short in ["COVER DRIVE","INSIDE OUT"]:
                print("\nIts an 4")
                runs2=runs2+4
                print("Score:", runs2, "/", wickets2)
            if short in ["SQUARE CUT","PULL","HOOK","DEFENCE","LEAVE"]:
                print("\nA dot ball")
                print("Score:", runs2, "/", wickets2)

    # Strike change after over
    striker, non_striker = non_striker, striker

# ---------------- RESULT ---------------- #
print("\n--- MATCH RESULT ---")
if runs2 >= target:                                          #condition for winning and loosing the match
    print("Chasing team WON the match! which is",bowlteam)
    fh.write('Game between:')
    fh.write(team1)
    fh.write('Vs')
    fh.write(team2)
    fh.write('and game is won by chasing team which is')
    fh.write(bowlteam)
    fh.write('\n')
else:
    print("Defending team WON the match! which is",batteam)
    fh.write('Game between:')
    fh.write(team1)
    fh.write('Vs')
    fh.write(team2)
    fh.write('and game is won by chasing team which is')
    fh.write(batteam)
    fh.write('\n')

fh.close()

fh1=open('gamedata.txt','r')

y=input('Enter yes if you want to see previous records of game otherwise no').upper()
if y == 'YES':
    record=fh1.readlines()
    for p in record:
        print(p)

fh1.close()
    

