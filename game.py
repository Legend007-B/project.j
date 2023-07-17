import random

def get_choices ():
    your_choice = input("Enter a choice(rock, paper, scissors)")
    compuuter_choice = ['rock', 'paper', 'scissors']
    my_choice = random.choice(compuuter_choice)
    choices = {"player": your_choice, "james": my_choice}
    return choices

def check_win (player, james):
   print (f"you chose {player}, I chose {james}")
   if player == james:
       return "It's a tie!"
   elif player == 'rock':
       if james == 'scissors':
        return "rock smashes scissors! you win!"
       else:
        return "paper covers rock! you lose."
   elif player == "paper" :
      if james == "rock":
         return "paper covers rock! you win."
      else:
         return "scissors cuts paper! you lose."
   elif player == "scissors":
      if james == "paper":
         return "scissors cuts paper! you win."
      else:
         return "rock smashes scissors! you lose."
      
choices = get_choices ()      
result = check_win(choices["player"], choices ["james"])   
print(result) 
   
   