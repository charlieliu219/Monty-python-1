import nltk
import random

def generate_word():
    nltk.download('words')
    word_list = nltk.corpus.words.words()
    random_index = random.randint(0, len(word_list))
    word = word_list[random_index]
    return word


# # check if letter is in the word
# def check_letter(letter, word):
#     if letter in word :
#         print(f"{letter} is in the word! :) ")
#         return True
#     else :
#         print(f"{letter} is NOT in the word :(")
#         return False

# # if a letter is in the word, print the letter in right position
# def unmask_letter(letter, word, mask) :
#     i = 0
#     while i < len(word) :
#         if word[i] == letter :
#              mask[i] = word[i]
#         i += 1
        
        
# ___________________________________main________________________________
# changes to implement:
# 1. use set to check if a letter is in the word
# 2. use ,join() to print the word 
# 3. add lives 


word = generate_word()
letters_in_word = set(word)
used_letters = set()
lives = len(letters_in_word)

print('-' for letter in word)
print(f"\n You have {lives} lives to guess this common English word. Give me each letter at a time! \n")


while True : 
    input_letter = input("guess a letter: ") 
    used_letters.add(input_letter) # add user input to input_letters
    print('You have guessed: ', ' '.join(used_letters))
    
    # if lives == 0:
    #     print('You have lost the game! The word is ', word)
    #     break
    
    if input_letter in word:
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(f'Now you have: {word_list} \n')
    else:
        print(f'{input_letter} is not in the word. Try another one!\n')     
        lives -= 1
        
    if letters_in_word == word_list: 
        print("Yes! The word is exactly {word}!\n")
        break
    
           
        


