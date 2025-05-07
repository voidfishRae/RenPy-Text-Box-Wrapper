#Renpy Text Wrapper: texthandlertests.py
#Rae Tasker
#April 2025
# Unit Testing for texthandlercomplete.py

from texthandlercomplete import *

def main():
    
    #Test 1: Long string with periods.
    #Hello. It me. I am trying to get this text to work.
    #15 ['Hello. It me.', 'I am trying to', 'get this text', 'to work.']
    #6 ['Hello.', 'It me.', 'I am', 'trying', 'to', 'get', 'this', 'text', 'to work.', '']
    instring = "Hello. It me. I am trying to get this text to work."
    print(instring)
    print("15", checkFullText(instring))
    print("6",checkFullText(instring, 6),"\n")

     #Test 2: Long string with no periods.
     #hello i am trying to get this text to work but no periods this time wee
     #15 ['hello i am', 'trying to get', 'this text to', 'work but no', 'periods this', 'time wee']
     #36 ['hello i am trying to get this text', 'to work but no periods this time wee', '']
    instring = "hello i am trying to get this text to work but no periods this time wee"
    print(instring)
    print("15",checkFullText(instring))
    print("36",checkFullText(instring, 36),"\n")

     #Test 3: Short string with no periods.
        #hello
     #15 ['hello', '']
    instring = "hello"
    print(instring)
    print("15",checkFullText(instring),"\n")

     #Test 4: Single space.
     #
     #2 [' ', '']
    instring = " "
    print(instring)
    print("2",checkFullText(instring, 2), "\n")

     #Test 5: One long word.
     #Megametahyperlydian
     #15 ['Megametahyperly', 'dian']
     #2 ['Me', 'ga', 'me', 'ta', 'hy', 'pe', 'rl', 'yd', 'ia', 'n']
    instring = "Megametahyperlydian"
    print(instring)
    print("15", checkFullText(instring))
    print("2", checkFullText(instring, 2), "\n")

    #Test 6: Empty string.
    #
    #15 ['', '']
    instring = ""
    print(instring)
    print("15", checkFullText(instring))

main()