The Colored Sentence Program
-----
By: Kaden Hansen

CSP or The Colored Sentence Program is a python program I wrote last year.
The fundamentals of it are made. However, bug fixes are still underway. Feel
free to test it out though!

*Note: Please read all the text I have provided in the
terminal when you run the program. Everything is explained much
better and hopefully much clearer there.

CSP (Colored Sentence Program) is a program that allows you to create,
save, and delete colored sentences. It has an introduction for new users,
but it's very long. If you want to skip it, type "s" and then "cc" or "ac"
in the main menu to view your color or action choices. 

You can create sentences, save them in existing or new files and view them in
a formatted list by typing "pr" in the main menu. You can also delete sentences
or entire files by typing "d" to access the Deletion Menu. To choose a color, you
can use built-in or custom RGB colors, which can be saved for later use. The RGB
menu is accessed by typing "rgb" in the main menu.

Beginner's Legend:
-----
first.txt: your first sentence file to save sentences
in. To change this, read the introduction found in the
program file.

file_accessed_number.txt: Tells the program if it
needs to first create a file before trying to use an
existing one. More info in the long intro to the program.

(a '0' on the first line tells the program to ask to save
a new file before asking to use an existing file. When you
create or use a file, the number on the first line in this
file automattically turns to '1'. This tells the program
that it can look for existing files in the directory.

I made it this way so that you can have manual control over if
you wanted to create a new file before you start the program.
You do not need to do this, but I tried to make the program as
customizable as possible.)

save_file: All of the txt filenames used by the program.

(i. e. first.txt will have its own line in this file
as "first" to tell the program it is in the CSP directory)

saved_color_codes: The saved_custom RGB ansi codes with the
name first and the ANSI code second. The program uses this
line to one, name the color and two, use the correct color
code.

(i. e. "sea blue-[38;2;46;122;234m")

Sadly, because the RGB menu I have implemented into this program
is not general enough, I have not included it in text_colors.py.
You can manually make any color you wish for python files you
make with the info I found on the internet. 

Warning: If you encounter an issue where two file names in save_file.txt
combine into one line while the program is running, please stop the program
and restart it. The program will tell you what to do next. I'm sure I fixed
this issue, but there still may be a chance this is in effect.

© 2023 Kaden Hansen. All Rights Reserved.
