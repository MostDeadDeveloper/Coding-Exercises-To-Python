"""

Problem #4 One Sentence, One Word, But Many Words

Problem:

	Given A Sentence, containing words and strings, remove all same instances of the same words/strings. 
	Make sure that the entire sentence does not contain any duplicate words.
	There are no specifics involved if the first,second,third....last duplicate words must remain in the sentence,
	As long as the sentence does not contain any duplicate words, that is fine.
	
Sample Input 1 : 
I am a God but you are more than a God

Sample Output 1-1 :
I am a God but you are more than a

Sample Output 1-2:
I am a but you are more than a God.


Sample Input 2 :
HAHA HAHA HAHA HAHA HAHA

Sample Output 2 :
HAHA


Sample Input 3 :
You are A Python Programmer. Thus, you are obsessed with one line comments and super efficient programs.

Sample Output 3-1 :

You are A Python Programmer. Thus, obsessed with one line comments and super efficient programs.


Sample Output 3-2 :

A Python Programmer. Thus, you are obsessed with one line comments and super efficient programs.

Note : For Sample Input&Output 3, there are multiple Possible Outputs. I did not list them all for that is time consuming and repetitive.

"""
import sys
import time

def checker(words):
    words = words.split()
    
    i = 0
    j = 1
    try:
        while i != len(words):
            while j != len(words):
                if (((words[i]).lower() == (words[j]).lower()) and (i != j)):
                    words.pop(j)
                else: j+=1
            i+=1
            j = i+1
    except: pass
    return words

sentence = input()
print(' '.join(checker(sentence)))

time.sleep(5)

