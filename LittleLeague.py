game = []
strikes = 0
hits = 0
hits_in_a_row = 0
runs = 0
outs = 0
f = open('S.txt', 'r')
input = f.read()

for i in range(1, len(input)):
    if input[i] == '(':
        if input[i + 6] == ')':
            play = {"pitch": input[i+1:i+3], "swing": input[i+5]}
        elif input[i + 5] == ')':
            play = {"pitch": input[i+1:i+2], "swing": input[i+4]}
        else:
            print("Should never reach here")
        game.append(play)

for i in range(0, len(game)):
    play = game[i]
    if play["pitch"] == "FB" and play["swing"] == "F":
        runs += (hits + 1)
        hits = 0
    elif play["pitch"] == "C" and play["swing"] == "S":
        strikes = 0
        hits+=1
        hits_in_a_row+=1
        if hits_in_a_row == 4:
            hits -= 1
            runs += 1
    elif play["pitch"] == "FB" and play["swing"] == "S":
        strikes+=1
        if strikes == 3:
            outs += 1
            if outs == 3:
                break
    elif play["pitch"] == "C" and play["swing"] == "F":
        strikes+=1
        if strikes == 3:
            outs += 1
            if outs == 3:
                break
    else:
        print("Something's wrong")

print(runs)