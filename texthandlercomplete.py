#Renpy Text Wrapper: texthandlercomplete
#Rae Tasker
#April 2025

#Main function, checkFullText, and helper functions for splitting text up so as to not overflow a text box in Ren-py

import re

#A recursive function that checks a block of text to see if it overflows a certain allowed value
#In order of priority, the text is split at:
#    1. Period closest to desired index.
#    2. Space closest to desired index.
#    3. At desired index, even if in the middle of the word.
#Inputs: fullString, the string of text to be split up.
#Output: a list containing the split apart strings, in order
def checkFullText(fullString, maxFullLength = 15):
     outFullList = []
     splitFirstList = textCheck(fullString, maxFullLength)

     #if the second element of splitFirstList is longer than maxFullLength, recurse on the second element alone
     #append both halves of splitNextList to outFullList
     if (len(splitFirstList[1]) >= maxFullLength):
        splitNextList = checkFullText(splitFirstList[1], maxFullLength)
        outFullList.append(splitFirstList[0])
        #compile all previous elements into new list
        for element in splitNextList:
             outFullList.append(element)

     #else the second element of splitFirstList is shorter than maxFullLength
     #meaning the end of the string has been reached
     #append results of textCheck to the list to form the first element
     else:
        outFullList.append(splitFirstList[0])
        outFullList.append(splitFirstList[1])

     return outFullList

#A helper function that breaks down a string inString to segments that total maxLength in length.
#Inputs: inString, the string to split up; maxLength, the longest segment you can have as output, defaults to 15 characters.
#Outputs: a list containing both elements of inString after they have been split up.
def textCheck(inString, maxLength=15):
        outStringList = [inString,""]
        #check if the string is longer than max length
        if (len(inString) > maxLength and maxLength > 0):
            #index of all regex matches.
            periodIter = re.finditer('[.]',inString)
            periodList = []
            for period in periodIter:
                 periodList.append(period.end())

            #if periodList is empty (no matches for ".") OR the first period index is bigger than maxLength, cannot split at period
            if (periodList == [] or periodList[0] > maxLength):
                 #split at nearest space " "
                 spaceIter = re.finditer("[ ]",inString)
                 spaceList = []
                 for space in spaceIter:
                      spaceList.append(space.end())
                 # check that spaceList is not empty
                 if(spaceList == []):
                      #if it is, split at index, in middle of word. alas
                      outStringList = inString[:maxLength], inString[maxLength:]
                 else:
                      outStringList = splitAtIndex(maxLength, inString, spaceList)
            
            else:
                outStringList = splitAtIndex(maxLength, inString, periodList)

        return outStringList

#Iterates through the found values until it finds the value previous to the desired index and splits the string at that point
#Inputs: targetIndex, the index at which the string needs to be split (either a period or a space or the maximum length of the string);
#splitString: the string to be split up; foundList: a list containing the indicies of the identified regex patterns (can be empty)
#Outputs: a list contining the split string and the remaining part of the string
def splitAtIndex(targetIndex, splitString, foundList):
     prevIndex = targetIndex
     outStringLeft = splitString
     outStringRight = ""

     for foundIndex in foundList:
          if (foundIndex < targetIndex):
               prevIndex = foundIndex
          elif (foundIndex > targetIndex):
               outStringLeft, outStringRight = splitString[:prevIndex].strip(), splitString[prevIndex:].strip()
               break
          elif (foundIndex == targetIndex):
               outStringLeft, outStringRight = splitString[:foundIndex].strip(), splitString[foundIndex:].strip()
               break
          else: 
               #this should be impossible
               raise Exception("Unknown Error in splitAtIndex")
     
     outSplitString = [outStringLeft, outStringRight]
     return outSplitString

