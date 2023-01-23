from replit import clear
import random

print('''
_                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/        
''')
print("Mexico states Edition / Estados de Mexico Edicion")
print("✄ - - - - - - - - - - - - - - - - - - - -")
print("Hangman instructions:\n The 'PC' chooses a secret word (from the states of Mexico), while you as a player try to guess the word by guessing letter by letter. However, each wrong answer takes one life out of the 6 starting life points. Once it gets to zero, the game is over.\n")
print("✄ - - - - - - - - - - - - - - - - - - - -")
print("El Ahorcado Instrucciones: La 'Pc', elije una palabra secreta (de los estados de mexico), mientras que tu como jugador trata de adivinar la palabra al ir adivinando letra por letra . Sin embargo, cada respuesta incorrecta lo acerca un poco más a perder ya que cuentas con 6 vidas.\n")

frames = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["aguascalientes", "bajacalifornia", "campeche", "chiapas", "chihuahua", "mexico", "coahuila", "colima", "durango", "guanajuato", "guerrero", "hidalgo", "jalisco", "michoacan", "morelos", "nayarit", "nuevoleon", "puebla", "sinaloa", "queretaro", "oaxaca", "sanluispotosi", "sonora", "tabasco", "tamaulipas", "tlaxcala", "veracruz", "yucatan", "zacatecas" ]

chosen_word = random.choice(word_list)

# Display de rayas 
box = ["_" for letter in chosen_word]

# Game variable setup
lives = 6
used_letters = []
end_game = False

# Que se continue ejecutando el juego
while not end_game:
    # Display current word
    print(" ".join(box))
    
    # Ask to guess a letter
    guess = input("Guess a letter / Adivina una letra: \n").lower()
    
    # Check if the letter hasn't been used yet
    if guess in used_letters:
        print("You already used this letter / Ya utilizaste esta letra")
        continue
    used_letters.append(guess)
    
    # Comprobar la letra si adivinar cambiar posicion guiones
    if guess in chosen_word:
        for position, letter in enumerate(chosen_word):
            if letter == guess:
                box[position] = letter
                print("Has Adivinado / You have guessed")
    else:
        # Reduce lives count by 1
        lives -= 1
        print(f"No has Adivinado, pierdes una vida / you haven't guessed, you lose a life \n Tus Vidas: {lives}")
        if lives == 0:
            print("Has Perdido! / You loose! :C")
            end_game = True
    
    # Comprobar que no hayan espacios para ganar  
    if "_" not in box:
        print("Has Ganado!!! / You Win !!!")
        end_game = True

    print(frames[lives])

print("✄ - - - - - - - - - - - - - - - - - - - -")