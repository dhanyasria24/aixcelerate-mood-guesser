# Mood Guesser

## Level 3: Testing

Accuracy on the 5 practice sentences: **100%**

1. **Which sentence went wrong (or was closest to going wrong), and why?**

All five sentences were classified correctly. However, "Today was a great day" was closest to going wrong because it did not contain any words from my Happy or Sad lists. My program selected Happy because I chose Happy as the tie-breaking rule.

2. **One change that would make my program better:**

I can improve my program by adding more useful clue words and teaching it to understand negative words like "not". This will help the program identify emotions more accurately.

## Learning questions

1. **Total score of "good party today" and its mood:**

   good = +2, party = +1, today = 0

   Total score = **+3**

   Mood = **Happy**

2. **Total score of "bad exam day" and its mood:**

   bad = -2, exam = 0, day = -1

   Total score = **-3**

   Mood = **Sad**

3. **Why did "exam" get a score of 0, and is that good or bad?**

   The word "exam" appeared once in a Happy sentence and once in a Sad sentence. Therefore, its score became zero. This is useful because the word does not strongly indicate either mood, although it also means the word cannot help the program make a decision.

4. **Why is "not good" labelled Happy by this method, and how could it be fixed?**

   The word "good" has a positive score of +2, while "not" has a score of 0. Therefore, the total score becomes +2 and the sentence is labelled Happy. This is incorrect because "not" changes the meaning of "good". The program could be improved by checking negative words and understanding phrases such as "not good".

## AI declaration

I used an AI tool: **Yes**

If yes, what I asked it:

I used ChatGPT to understand the AIXcelerate instructions, learn Python concepts, get guidance on writing the mood guessing program, and understand how to test the program and calculate accuracy.

## Reflection

What was hardest, and what I learned that I did not know before:

The hardest part was understanding how to identify the mood of a sentence using Python. I learned how to use functions, lists, loops and conditions to solve a problem. I also learned that a simple program can sometimes make incorrect predictions and that it can be improved by learning from examples.
