import random


def choose_options():

  options = ('piedra', 'papel', 'tijera')
  user_option = input('piedra, papel o tijera => ')
  computer_option = random.choice(options)
  user_option = user_option.lower()

  
  
  if not user_option in options:
    print('esa opcion no es valida')
    #continue
    return None, None
  
  print('User option =>', user_option)
  print('Computer option =>', computer_option)
  return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):

  if user_option == computer_option:
    print("Empate!")
  
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print('piedra gana a tijera')
      print('user gano!')
      user_wins += 1
    else:
      print('papel gana a piedra')
      print('computer gano!')
      computer_wins += 1
      
  elif user_option == 'papel':
    if computer_option == 'piedra':
      print('papel gana a piedra')
      print('user gano!')
      user_wins += 1
    else:
      print('tijera gana a papel')
      print('computer gano!')
      computer_wins += 1
  
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('user gano!')
      user_wins += 1
    else:
      print('piedra gana a tijera')
      print('computer gano!')
      computer_wins += 1
  
  return user_wins, computer_wins

def end(user_wins, computer_wins):

    if computer_wins == 3:
      print('el ganador es la computadora')
      return False
  
    if user_wins == 3:
      print('el ganador es el user')
      return False


  
def run_game():

  rounds = 1
  computer_wins = 0
  user_wins = 0

  while True:
  
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
  
    print('computer wins', computer_wins)
    print('user wins', user_wins)
    
    rounds += 1
  
    user_option, computer_option = choose_options()
    
    user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)

    endgame = end(user_wins, computer_wins)

    if endgame == False:
      break

    
run_game()
  