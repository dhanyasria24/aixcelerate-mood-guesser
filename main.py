
# AIXcelerate - Mood Guesser
# Level 1: Count the Moods
# Level 2: Guess the Mood

# Training sentences given in the instructions
train_data = [
    ("I got full marks in the test today!", "Happy"),
    ("We won the college cricket match", "Happy"),
    ("My friends planned a surprise party for me", "Happy"),
    ("The food in the canteen was really tasty", "Happy"),
    ("I am so excited for the weekend trip", "Happy"),
    ("Our project got selected for the exhibition", "Happy"),
    ("I finally learned how to ride a bicycle", "Happy"),
    ("Mom made my favourite sweets today", "Happy"),
    ("I lost my phone on the bus", "Sad"),
    ("I failed in the mathematics exam", "Sad"),
    ("My best friend is moving to another city", "Sad"),
    ("It rained and our picnic was cancelled", "Sad"),
    ("I missed the last bus and felt very upset", "Sad"),
    ("My laptop stopped working before the submission", "Sad"),
    ("I felt lonely during the long holidays", "Sad")
]


# LEVEL 1: Count the number of Happy and Sad sentences

def count_moods(data):

    happy_count = 0
    sad_count = 0

    for sentence, mood in data:
        if mood == "Happy":
            happy_count += 1
        elif mood == "Sad":
            sad_count += 1

    return (happy_count, sad_count)


# LEVEL 2: Words used to identify the mood
# Each list contains exactly 8 words (roll number ends in 8)

happy_words = [
    "full", "won", "surprise", "tasty",
    "excited", "selected", "learned", "favourite"
]

sad_words = [
    "lost", "failed", "moving", "cancelled",
    "missed", "upset", "stopped", "lonely"
]


# Function to guess whether a sentence is Happy or Sad

def guess_mood(sentence):

    # Convert the sentence into lowercase
    sentence = sentence.lower()

    # Remove punctuation so words can be matched easily
    clean_characters = []

    for character in sentence:
        if character.isalnum() or character.isspace():
            clean_characters.append(character)
        else:
            clean_characters.append(" ")

    words = "".join(clean_characters).split()

    happy_score = 0
    sad_score = 0

    # Check each word against the two mood lists
    for word in words:

        if word in happy_words:
            happy_score += 1

        elif word in sad_words:
            sad_score += 1

    # Compare the scores and decide the mood
    if happy_score > sad_score:
        return "Happy"

    elif sad_score > happy_score:
        return "Sad"

    else:
        # If both scores are equal, choose Happy as the tie-break rule.
        return "Happy"


# Display Level 1 result
print("LEVEL 1 - COUNT THE MOODS")

result = count_moods(train_data)

print("Happy sentences:", result[0])
print("Sad sentences:", result[1])


# Display Level 2 result
print("\nLEVEL 2 - GUESS THE MOOD")

test_sentences = [
    "I won a prize today!",
    "I lost my notebook.",
    "My friends gave me a surprise.",
    "I felt upset today."
]

for sentence in test_sentences:
    mood = guess_mood(sentence)
    print(sentence, "->", mood)

# LEVEL 3: Test the Mood Guesser

practice_data = [
    ("I won a medal in the sports meet", "Happy"),
    ("I lost my notebook before the exam", "Sad"),
    ("My friends gave me a lovely surprise", "Happy"),
    ("The train was late and I felt upset", "Sad"),
    ("Today was a great day", "Happy")
]

correct_answers = 0

print("\nLEVEL 3 - TESTING THE PROGRAM")

for sentence, actual_mood in practice_data:

    predicted_mood = guess_mood(sentence)

    print("\nSentence:", sentence)
    print("Actual mood:", actual_mood)
    print("Predicted mood:", predicted_mood)

    if predicted_mood == actual_mood:
        correct_answers += 1

# Calculate accuracy percentage
total_sentences = len(practice_data)

accuracy = (correct_answers / total_sentences) * 100

print("\nCorrect predictions:", correct_answers)
print("Total sentences:", total_sentences)
print("Accuracy:", accuracy, "%")
