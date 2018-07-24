from random import randint
responce=["yes", "no", "wrong", "ask again", "nope", "very well", "posibly", "correct"]
user=raw_input("What is your question")
print(user + responce[randint(0,7)])