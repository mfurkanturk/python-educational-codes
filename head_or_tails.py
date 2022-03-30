import random

test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

rand = random.randint(1, 2)
if rand== 1:
    print("Heads")
else:
    print("Tails")
