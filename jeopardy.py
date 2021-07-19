import requests
import random
from similar_text import similar_text

response = requests.get('http://jservice.io/api/clues?category=139').json()


# Print out just the first item in the entire response.
print("#1")
print(response[0]["question"])
print(response[0]["answer"])

# Print out just the question of the first item in the entire response.
print("#2")
print(response[0]["question"])

# Refactor your code so that it prints out a random question, not just the first one every time.
print("#3")
print(response[random.randint(0, len(response) - 1)]["question"])

# Now, get some user input after the question. If what they type matches the answer, print a "congratulations!" message of some sort. If it doesn't match, print a "sorry" message of some sort.
print("#4, #5, #6, #7, etc.")

score = 0
isPlaying = True

while isPlaying:
    x = random.randint(0, len(response) - 1)
    answering = True
    ans = input(response[x]["question"] + "\n")
    ans = ans.lower()
    while similar_text(ans, response[x]["answer"].lower()) >= 70 and similar_text(ans, response[x]["answer"].lower()) < 100:
        if ans == response[x]["answer"].lower():
            print("Congratulations, correct answer!")
            score += response[x]["value"]
        elif similar_text(ans, response[x]["answer"].lower()) >= 70 and similar_text(ans, response[x]["answer"].lower()) < 100:
            print("")
        else:
            print("Sorry, wrong answer. The correct answer was " + response[x]["answer"])
            score -= response[x]["value"]
            if score < 0:
                score = 0

    print("Score = " + str(score))
    y = input("Would you like to continue playing? Y or N \n")
    if y.lower() == "y":
        isPLaying = True
    else:
        isPlaying = False
    