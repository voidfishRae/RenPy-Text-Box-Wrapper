# RenPy-Text-Box-Wrapper
Breaks up large blocks of text into blocks of specified length to avoid unintended overflow on a text box.
Intended for use with RenPy (works as of RenPy ver 8.3.7).
Created by Rae Tasker (May 2025)

Attempts to split text with the following priority, in relation to the character limit (chosen by user, defaults to 15): 
  1. Nearest preceeding fullstop/period.
  2. Nearest preceeding space.
  3. Middle of the word as last resort.

Limitation Note:
Developed for use with RenPy (https://www.renpy.org/), which is a visual novel game software. In this style of game, the pacing and placement of the text is very important, and should be taken into account when writing the script. As RenPy already has means of throwing Exceptions if an overflow occurs, I think that would be a better option for handling this issue. However, this program fills a niche that is not currently handled by RenPy, and so still serves purpose if a writer should choose it.

How to Run the Included Example:
1. Create a new RenPy game (for instance, textTest).
2. Place texthandlercomplete.py into the directory labelled "game" (renpy -> textTest -> game).
3. Replace the script.rpy file with the one included in this repository.
4. Run the game.
