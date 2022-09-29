Battleships Game

This is a program to run a "Battleships" logic game in a mock terminal.

# User Stories
As a user I want the computer to be able to make intelligent choices, meaning that its coordinates 
for attacking are random up until it hits a ship, and it then tries to find the rest of the ship.

I want to be able to place my own ships both manually and automatically.

# Features
1. Intelligent targeting by computer
2. Allowing the player to place ships manually and automatically.
3. Turn counter to limit player moves and enforce end condition.
4. Feedback for invalid inputs and guesses.
5. Allow the player to set the board size.
6. Automatically scale the number of ships for players based on board size.

# Build Log
- Python essntials template added.
- Python files for each class created and defined.
- Nesting order between classes established in doc string.
- README file intiated with user stories, features to be included, Build Log, Error, Testing, and Deployment headers. Deployment content completed.
- Create a minimal viable product version first. Use one ship, random only not manual placement of ships, maybe without error handling yet, or win conditions. Test deployment on Heroku.
        1. Establish ship class
        2. Give one ship subclass its objects
        3. Define what is a board and pass through the ship subclass
        4. Define the players and pass through the board
        5. Define the game structure and pass through player
        6. Initate game function through run.py file.
- Create a ship class and add docstring explaining its objects.
- Create only the 'Carrier' class for now, with explaination of its objects.
- A lot of work done on Boards. So far it does three things:
    - Create an instance of a board for player and computer
    - Print this to the terminal for user to see
    - Define boards by handling them as coordinates inside arrays
    All this is done within a scalable frame, allowing for user input of board size.
- Remembered to import random module for use in Boards class.
- Player instance initialisation created, and the make guess function which currently gives the computer only a random choice, takes in the players input as
coordinates, and validates both as already guessed.
# Errors

# Testing

# Deployment
    ## Deploying to Heroku
    1 Create an account with Heroku, and navigate to the main page by clicking on "Heroku" at top left of screen.
    2 Click the "New" button in the upper right of screen, select "create new app" from the drop-down menu.
    3 Type an app name in the prompted text field, ensuring the chosen name is available.
    4 Select the appropriate region, between "America" and "Europe".
    5 Click the button below "Create App"
    6 Navigate to settings from the upper menu bar.
    7 In the second section of settings, "Config Vars", click "Reveal Config Vars".
    8 Add a config var with KEY=PORT, and VALUE=8000.
    9 In the next section, add two buildpacks, one for python and one for nodejs, in that order.
    10 Navigate to the "Deploy" section where you found the "Settings" tab.
    11 In the second section, "deployment method", connect to your GitHub account.
    12 Once you've allowed GitHub to connect with Heroku, a new subsection should appear with a search bar for a repository connected to the relevant GitHub account.
    13 Hit the "Search" button and select the "Connect" button beside the relevant repository.
    14 Now you can choose a branch to deploy from or leave as default "main".
    15 Click the "Enable Auotmatic Deploys" button.
    16 You can monitor the build progress through the "Overview" tab.
    17 Clicking "Open app" in the upper right of screen with attempt to run the program in a new window.