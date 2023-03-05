# Descubra o Secret Number
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: ")) # Foi convertido com 'int' para transformar a string em integer
    guess_count += 1 # (guess_count = guess_count + 1)/ Foi preciso incrementar meu guess count, mas como estabeleci um limite, só foi até o 3.
    if guess == secret_number:
        print("You won!")
        break # Para terminar o loop, se não terei o total de 3 tentativas, mesmo acertando o secret number
else: # Nosso while também pode ter um else, assim como o if
    print("Sorry, you failed!")

