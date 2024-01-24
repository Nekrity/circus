# Made by Artūrs Izkalnis
# Specifikācija
# - 1pt Spelētāji sāk no lauciņa nr. 1, vispār 100 lauciņu. Ir divi spēlētāji. Vinē tas kurš pirmais sasniedz pēdējo lauciņu
# - 1pt Maksimāli - 25 raundi, ja beidzas raundi - neizšķirts
# - 1pt Viens pēc otra met kauliņu (ar nejauša ciparu ģenerātora palidzību) un iet uz priekšu
# - 1pt Ja trāpa uz lauciņu ar kāpnem:
# -- zilas kāpnes ved uz leju, 18 -> 7, 67 -> 46 , 80 -> 69, 74 -> 63
# -- sarkanas kāpnes ved uz augšu, 15 -> 24, 39 -> 48, 33 -> 52, 87 -> 96 
# - 1pt Katrā raundā tik drukāta informācija kur atrodas spēlētājs, dators un vai ir uzkāpts uz kāpnem

# Koda vertēšanas kritēriji
# - 1pt Kodā izmanto mainīgus, ciklus (for vai while), zarošanu (if)
# - 1pt Kods strādā bez kļūdam
# - 1pt Mainīgo un funkciju nosaukumi atspoguļo izmantošanas būtību, bez saisinājumiem, rakstīti snake_case stilā
# - 1pt Kodam ir jēdzīgi komentāri, pirms "if, for" koda konstrukcijam
# - 1pt Izmaiņas saglabātas versiju vadības sistēmā Git

# Dokumentācija
# Mainīgie - https://www.w3schools.com/python/python_variables.asp
# Operācijas ar mainīgiem - https://www.w3schools.com/python/python_operators.asp
# Mainīgo drukāšana - https://www.w3schools.com/python/python_variables_output.asp
# Nosacījumi, zarošana, if ... else - https://www.w3schools.com/python/python_conditions.asp
# For cikls - https://www.w3schools.com/python/python_for_loops.asp
# Nejauša skaitļa generēšana - https://www.w3schools.com/python/ref_random_randint.asp
# Github Fork (repozitorija kopija) - https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
# Klonēt repozitoriju - hhttps://code.visualstudio.com/docs/sourcecontrol/intro-to-git
import random
red_ladder_start=[15,39,33,87]
red_ladder_end=[24,48,52,96]
blue_ladder_start=[18,67,80,74]
blue_ladder_end=[7,46,69,63]

def ladders(player_name, player_position, ladder_color): #works if you stepped on any ladder
    global new_player_position
    if (ladder_color=="red"): #checks if it's red ladder
        print("Well done ",player_name,"! You stepped on red ladder.",sep="")
        player_on_ladder=red_ladder_start.index(player_position)
        new_player_position=red_ladder_end[player_on_ladder]
        print(player_name,"you're on position", new_player_position)
    else: #in any other case it's blue ladder
        print("How unfortunate ",player_name,"! You stepped on blue ladder.",sep="")
        player_on_ladder=blue_ladder_start.index(player_position)
        new_player_position=blue_ladder_end[player_on_ladder]
        print(player_name,"you're on position", new_player_position)

def circus(): #the game itself
   rounds=1
   player1_position=1
   player1_name="player1"
   player2_position=1
   player2_name="player2"
   print("Welcome to the circus!","Your goal is to reach the last field (100) in 25 rounds!")
   while True: #works forever until break
        input(player1_name +" roll the dice")
        player1_position += random.randint(1,6)
        if (player1_position>=100): #check if player1 won
            print(player1_name,"you're on position 100")
            print("Congratulations",player1_name,"! You won!")
            break
        print(player1_name,"you're on position", player1_position)
        if (player1_position in red_ladder_start): #check if player1 stepped on red ladder
            ladders(player1_name,player1_position,"red")
            player1_position=new_player_position
        if (player1_position in blue_ladder_start): #check if player1 stepped on blue ladder
            ladders(player1_name,player1_position,"blue")
            player1_position=new_player_position
        input(player2_name +" roll the dice")
        player2_position += random.randint(1,6)
        if (player2_position>=100): #check if player2 won
            print(player2_name,"you're on position 100")
            print("Congratulations",player2_name,"! You won!")
            break
        print(player2_name,"you're on position", player2_position)
        if (player2_position in red_ladder_start): #check if player2 stepped on red ladder
            ladders(player2_name,player2_position,"red")
            player2_position=new_player_position
        if (player2_position in blue_ladder_start): #check if player2 stepped on blue ladder
            ladders(player2_name,player2_position,"blue")
            player2_position=new_player_position
        rounds += 1
        if (rounds>25): #if current round is after 25 - stop the game
            print("Rounds ended!")
            print("How unfortunate! Nobody won!")
            break

circus()
