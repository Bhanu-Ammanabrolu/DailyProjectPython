with open("story.txt", "r") as f:
    story = f.read()

words = set()
start_of_word = -1

target_sign = "<"
target_sign_end = ">"
for i, char in enumerate(story):
    if char == "<":
        start_of_word = i

    if char == ">" and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

answers = {}

for each_word in words:
    user_choice = input("Enter a word for" + each_word + ": ")
    answers[each_word] = user_choice

for word in words:
    story = story.replace(word, answers[word])

print(story)