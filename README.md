# kody2.0
The second generation Kody Bot, inspired by Kody 1.0, this time by more friends :)

### Here's a quick rundown of how this project works
**__pycache__** is an autogenerated file that we do not need to touch or worry about

**cogs** contains each module that each of us will be working on, either separately or in groups

**myenv** is a virtual environment with all of the projects dependencies (or imports). Rather than download the libraries on your PC, you will run this virtual environment from terminal

**bot.py** is the "brain" of the bot. all functionality will be in modules from /cogs/

**.gitignore** prevents the json file from being uploaded to discord, because it contains a secret token

**requirements.txt** includes all the dependencies we need

### How to begin coding
0. Make sure you have python installed. https://www.python.org/downloads/

1. Clone a copy of this repo to your system

2. Open the repo in VSCode

3. You should create a virtual environment to keep your dependencies consistent with others.

Run "python -m venv myenv" to create your environment. If you choose to name it something else, update that in config.json

run "myenv/Scripts/activate" and you should notice a (myenv) prefix in your terminal. You are now using the virtual environment (very easy yes yes!)

NOTE: To leave the venv, run "deactivate"

now run "pip install -r requirements.txt" to download all dependencies to your venv

4. Duplicate the modularization_test.py file from /cogs/. You can also refer to greetings.py. RENAME THIS FILE! KEEP THIS IN COGS!

This is where you will implement your piece of Kody. Feel free to import anything else you need. NOTE: When you install a library in a venv, the library becomes a dependency of this project. Anyone else who uses this codebase will be able to use that same library. This makes collaboration more smooth :>

5. When testing and debugging your own features, you should probably have your own "testing bot" so you don't disturb other people's work. In your repo, creating a file named "config.json" and paste this into it:

{
    "token": "INSERT_TOKEN_HERE"
}

with your bot token. Sharing this token will allow someone else to turn on your bot with their own code.

6. To run Kody, run "python .\bot.py". You can press CTRL C to stop running it.
