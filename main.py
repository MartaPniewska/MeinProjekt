# geografie-spiel.py

capitals = {"USA":"Washington D.C.", "France":"Paris", "India":"New Delhi", "Holland":"Amsterdam", "Spain":"Madrid", "Italy":"Rom", "Norway":"Oslo"}

scores = 0
capitals_list = list((capitals.items()))
for land, stadt in capitals_list:
    eingabe = input("Was ist die Hauptstadt von " + land + " ist? Deine Antwort:  ")
    if eingabe == stadt:
        scores += 1
        print("Richtig! Deine Punktezahl: ", scores)
    else:
        print("Falsch! Richtig ist ", stadt)
total_score= round(scores/len(capitals_list)*100,1)
print("Dein Score ist: ", total_score, "%")
