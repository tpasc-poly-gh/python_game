import random

r = "rock"
p = "paper"
s = "scissors"

choices = [r, p, s]
def rps(p_choice: str):
    c_c_index = random.randint(0, 2)

    c_choice = choices[c_c_index]

    p_c_index = choices.index(p_choice)

    if p_c_index == c_c_index:
        print("Tie!")
        return
    
    p_c_i_next = (p_c_index + 1) % len(choices)

    if p_c_i_next == c_c_index:
        print(f"Lose! computer chose: {c_choice}")
    else:
        print(f"Win! computer chose: {c_choice}")