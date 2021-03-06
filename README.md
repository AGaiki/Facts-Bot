# Facts Bot (WIP)
This is a simple Discord bot that picks a random fact from a given list. This is a work in progress, as all the facts have to be coded into the program, rather than the program reading from  a database. This guide is sorta copied from my [Bed Wars Defense Bot guide](https://github.com/AGaiki/Hypixel-Bed-Wars-Defense-Bot). Luckily, the steps are more or less the same.

## Installation / Building - Basic
Make sure you have at least Python 3.8 installed from either [Python.org](https://www.python.org/downloads/) or the [Microsoft Store (for Windows 10 ONLY)](https://www.microsoft.com/en-us/p/python-38/9mssztt1n39l?activetab=pivot:overviewtab). For some reason, the Microsoft Store edition of Python has given me more success than the python.org version, but you can figure out what you want to use. If you are using macOS or a Linux distribution, you can install the appropriate versions of Python. For the purposes of these tutorial, we will assume you are using Windows 10. The commands are more or less the same, so no matter what OS you have, you should be able to run it successfully. After you have installed Python, you need to install [discord.py](https://pypi.org/project/discord.py/). There are two versions of discord.py available, one with only text based support and one with both text and voice based support. Since this is a very basic bot, you need not worry about installing the voice edition. 

To install, open up Command Prompt and type in the following command: 
`pip3 install discord.py`. It may show you some warnings about an outdated pip install, but that is not really an issue in this case. Running that command gives you support for Discord-specific commands that are present in the code. After you've installed the dependencies needed, you should be good to go! Follow these steps:

 1. Download the latest facts.py from [Releases](https://github.com/AGaiki/Facts-Bot/releases). You should move this somewhere other than downloads (optional, although recommended), somewhere like Documents. You can also rename it if you'd like, but this tutorial will assume you are using facts.py as your filename. Using your favorite code editor (Visual Studio Code, 
Notepad ++, Notepad?), make sure to customize the facts.py commands and responses to your heart's content, as the version from the Releases page is a template you need to edit. Make sure that your actual content is separated from each other with commas and quotes. Something like this: `"Statement 1",
 "Statement 2", etc`
 **NOTE: If you would like to create a database of content (instead of hardcoding it to your actual code), go to [Advanced.](https://github.com/AGaiki/Facts-Bot#advanced-installation)**
 3. On the very last line of the facts.py file, you need to edit the "TOKEN" field with your Discord bot token. You can find the instructions on how to do so [here](https://discordpy.readthedocs.io/en/latest/discord.html).

 4. Finally, open up Command Prompt and navigate to your facts.py. Assuming you've moved it to the Documents folder, you would type into Command Prompt: 
 `cd Documents` (or wherever you've saved it). After you have successfully navigated to the location of your facts.py file, type in: `python facts.py`(if you changed the filename from facts.py to something else, change the bot to the correct filename).
 5. Success! You have configured a bot properly! Good job! Feel free to play around with the Python syntax as you wish. **Your bot will go offline if you shut off the hosting computer, disconnect from a network, or close the Command Prompt window.** Another option to host it is following [these steps](https://github.com/AGaiki/Hypixel-Bed-Wars-Defense-Bot), which will show you how to host your bot on Repl.it.

## Advanced Installation
You are here because you either scrolled down past the basic installation instructions and/or you want to make your end product easier to modify and somewhat automate it. It will be a tad bit difficult and require more advanced coding "know-how." However, after completing this successfully, you will realize that it is more flexible in modification and more user friendly. It is recommended you create a folder housing facts.py, as soon, that folder will be populated with another folder. These steps can also be imitated with Repl.it. This guide will assume that you are housing your facts.py file in its own folder (not necessary for Repl.it). With all that in mind, let us begin!
 

 1. Make sure you have all the dependencies and the program, facts.py, itself.
 2. Create a new file in the **same folder** as facts.py (again, not necessary for hosting on Repl.it). Call it something like facts.txt (make sure you have your file extensions enabled if you are using Windows/macOS). The file name is facts, while the file extension is txt. This guide will assume you are using facts.txt as the file name.
 3. Populate facts.txt with any facts or information that you want. Remember, the actual python code itself calls for the bot to pick a random fact each time. Remember to also separate each fact by creating a new line.
 4. Move to the facts.py file. After the last `import` function and before the `bot = commands.Bot(command_prefix='!')` function, make sure to add `factstext = open("facts.txt").read().splitlines()`. Basically, we are creating a new variable called "factstext" and defining it to open a text file called "facts.txt," and then read it (`.read()`). We also add `.splitlines()` to tell the program that we are splitting the string each time we have a new line break.
 5. In our original code, we hard-coded some facts into it. It looks like this: ` fax = [ 
        'Test',
        'Test 2',
        'Test 3'
    ]`. Delete everything from the first bracket to the last. Keep the fax variable. Now, set the variable "fax" equal to the list of "factstext". You would implement it like so: `fax = list(factstext).` You can leave your "response" untouched.
    6. Success! It should (theoretically) work! If it somehow doesn't, double check your code. If debugging your code still doesn't work, open up an issue ticket, and we'll go from there!
<!--stackedit_data:
eyJoaXN0b3J5IjpbMTQyMzE3MjgyMywtOTAyOTc1MzI1LC0zOT
E4OTg4MTEsMjEyOTU1MTIsLTc4MjUzNDU2LDcxNzg4Mjk4NCw5
NzE4ODEzNDYsMjAxNTg4MCwtMTg0ODExNDk1XX0=
-->