# Space Invaders Clone
## Table of Contents
- [Space Invaders Clone](#space-invaders-clone)
  - [General Description and Objectives](#general-description-and-objectives)
    - [Space Invaders Clone](#space-invaders-clone-1)
    - [Software Purpose](#software-purpose)
    - [Target Audience](#target-audience)
    - [Application Area](#application-area)
    - [Expected Lifetime](#expected-lifetime)
    - [Key Features and Attractions](#key-features-and-attractions)
  - [Requirements](#requirements)
  - [Functional and Non-Functional Requirements Specification](#functional-and-non-functional-requirements-specification)
    - [Functional Requirements](#functional-requirements)
    - [Non-Functional Requirements](#non-functional-requirements)
  - [Architecture Description or Model](#architecture-description-or-model)
    - [Structural Overview](#structural-overview)
    - [Design Patterns](#design-patterns)
  - [Functional Description or Model of the Software](#functional-description-or-model-of-the-software)
    - [Data Flow](#data-flow)
    - [Processing Logic](#processing-logic)
    - [Key Functions and Methods](#key-functions-and-methods)
  - [User Manual](#user-manual)
    - [Starting the Game](#starting-the-game)
    - [Gameplay Instructions](#gameplay-instructions)
    - [Troubleshooting and FAQ](#troubleshooting-and-faq)
    - [Additional Information](#additional-information)
  - [Successful Use Case Scenarios](#successful-use-case-scenarios)
    - [Use Case 1: Casual Gaming Experience](#use-case-1-casual-gaming-experience)
    - [Use Case 2: Introducing Classic Games to Youngsters](#use-case-2-introducing-classic-games-to-youngsters)
    - [Use Case 3: Python Learning Tool](#use-case-3-python-learning-tool)
  - [Problematic Use Case Scenarios](#problematic-use-case-scenarios)
    - [Problem Scenario 1: Performance Issues on Older Hardware](#problem-scenario-1-performance-issues-on-older-hardware)
    - [Problem Scenario 2: Inconsistent Sound Effects](#problem-scenario-2-inconsistent-sound-effects)
    - [Problem Scenario 3: Difficulty in Understanding Game Mechanics](#problem-scenario-3-difficulty-in-understanding-game-mechanics)
  - [Project Complexity](#project-complexity)
  - [Reliability and Usability](#reliability-and-usability)
  - [Technical Documentation and Third-Party Utilization](#technical-documentation-and-third-party-utilization)
  - [Comprehensive and Satisfactory Testing](#comprehensive-and-satisfactory-testing)

## General Description and Objectives
### Space Invaders Clone

This project is a Space Invaders-style game developed using Pygame, a popular set of Python modules designed for writing video games. The game is a classic arcade-style game where players control a spaceship and defend against waves of alien invaders.

### Software Purpose

**Space Invaders Clone** recreates the classic Space Invaders experience, combining nostalgic gameplay with modern Python programming. Utilizing the Pygame library, it offers engaging and interactive graphics, appealing to both retro game enthusiasts and modern players.

### Target Audience

The game targets retro arcade game enthusiasts and casual gamers of all ages. Its straightforward yet entertaining gameplay makes it suitable for a wide range of players, offering an accessible and enjoyable experience to everyone.

### Application Area

This software is a prime example in the field of entertainment and educational programming. It serves as an ideal resource for those learning game development or Python programming, particularly in mastering the Pygame library.

### Expected Lifetime

The expected lifetime of this game extends over several years, with potential updates for compatibility with newer Python and Pygame versions. **This projection is based on typical lifecycles of similar software projects.**

### Key Features and Attractions

- Faithful recreation of the classic Space Invaders gameplay using modern programming techniques.
- Simple, engaging, and perfect for quick gaming sessions.
- Demonstrates the use of Pygame in a real-world scenario, offering learning opportunities for budding developers.
- The code is modular and well-structured, facilitating easy understanding and customization.
- Includes unit tests, highlighting a commitment to code quality and reliability.

## Requirements
Before running the Space Invaders Clone, ensure your system meets the following requirements:

- **Python Version**: Python 3.
- **Dependencies**: Pygame 2.5.2.
- **Operating System**: Compatible with Windows, macOS, and Linux.
- **Hardware Requirements**:
  - CPU: Any modern CPU with at least 1 GHz speed.
  - RAM: Minimum of 512 MB, 1 GB recommended for smoother performance.
  - Graphics: No specific requirements; should run on integrated graphics of most modern systems.
  - Storage: Minimal; enough to store the game and its resources, usually under 100 MB.
  - Display: Any standard display with a minimum resolution of 800x600.

## Functional and Non-Functional Requirements Specification
### Functional Requirements

1. **Gameplay Mechanics**: Classic Space Invaders mechanics with player-controlled spaceship shooting at alien invaders.
2. **Player Control**: Ability to move the spaceship horizontally and shoot bullets.
3. **Alien Behavior**: Aliens move across the screen and descend towards the player, increasing the difficulty.
4. **Scoring System**: Players earn points for destroying aliens, displayed on-screen.
5. **Game Levels/Stages**: Potential for increasing difficulty with game progression.
6. **Sound Effects**: Includes audio for shooting and hits/destroys.
7. **Game Over Conditions**: The game ends when aliens reach the player.
8. **User Interface**: Basic interface with start and game over screens.

### Non-Functional Requirements

1. **Performance**: Smooth and responsive gameplay on standard gaming setups.
2. **Scalability**: Modular design for easy expansion and addition of new features.
3. **Usability**: Simple and intuitive gameplay without the need for complex instructions.
4. **Maintainability**: Focus on maintainability with modular code and unit tests.
5. **Compatibility**: Compatible with systems supporting Python and Pygame.
6. **Security**: Minimal security concerns, given the standalone and non-network nature of the game.

## Architecture Description or Model
The game is structured into modules for character management, game logic, and graphical interface. The main functions of the game were tested using unit tests.

### Structural Overview

The Space Invaders Clone project is structured into several distinct modules, each handling a specific aspect of the game:

- `main.py`: Serves as the entry point of the game, managing the game loop and integrating other modules.
- `game_logic.py`: Contains core gameplay mechanics, including player actions, alien behavior, and collision detection.
- `ui_module.py`: Manages the user interface, displaying scores, buttons, and game over screens.
- `resource_manager.py`: Handles loading and managing game resources like images and sounds.
- `test_game_logic.py` and `test_resource_manager.py`: Unit tests for validating the functions in their respective modules.

These modules interact to create a cohesive gaming experience, with `main.py` orchestrating the overall game flow.

### Design Patterns

The project demonstrates the following design patterns and architectural decisions:

- **Modular Design**: The game's functionality is divided into different modules (`game_logic`, `ui_module`, and `resource_manager`), promoting separation of concerns and easier maintainability.
- **Procedural Programming**: The code primarily follows procedural programming principles, with functions performing specific tasks and maintaining game state.
- **Singleton Pattern**: Global variables are used in modules like `main.py`cin a Singleton-like approach where a single instance of the game state is maintained throughout the game's runtime.

## Functional Description or Model of the Software
The software operates with a main game loop, where each cycle updates the game state, processes user inputs, and renders the graphical interface. It uses algorithms for collision detection and character movement.

### Data Flow

The Space Invaders Clone game operates on a straightforward data flow model:

1. **Initialization**: The game begins in the `main.py` module, where Pygame is initialized, and game resources are loaded using `resource_manager.py`.
2. **User Input Handling**: Player actions (like moving the spaceship and firing bullets) are captured via Pygame's event handling system within the game loop in `main.py`.
3. **Game Logic Processing**: `game_logic.py` processes these inputs, updating the game state accordingly. This includes moving the player's spaceship, managing bullet movement, and handling alien movements.
4. **Collision Detection**: Also within `game_logic.py`, collision between bullets and aliens or the player and aliens is checked, and the game state is updated (like incrementing the score or ending the game).
5. **Rendering**: The `ui_module.py` takes the updated game state and renders the game screen, including the player's spaceship, aliens, bullets, and the score.

### Processing Logic

The core logic of the game revolves around several key operations:

- **Event Processing**: The game continuously checks for player inputs (like keyboard presses) and responds accordingly, such as moving the spaceship or firing bullets.
- **Game State Update**: Based on player actions and predefined game rules, the game updates its state - like moving aliens, bullets, and checking for collisions.
- **Rendering**: After each update, the game renders the new state on the screen, providing real-time feedback to the player.

### Key Functions and Methods

- `player`, `alien`, `bullet`, `bomb` in `game_logic.py`: These functions are responsible for rendering different game elements on the screen.
- `is_collision` in `game_logic.py`: A critical function that checks whether two objects (like a bullet and an alien) have collided, influencing the game flow.
- `load_image` and `load_sound` in `resource_manager.py`: These functions load the visual and audio assets required for the game.


## User Manual
### Starting the Game

1. **Launch**: Run `main.py` using a Python interpreter that supports Pygame. Alternatively, you can run the [`game.exe`](https://drive.google.com/file/d/1EXU5v6TH-HvRjNOb-XOfDgGzu_-V72Oq/view?usp=drive_link). Ensure all game resources (images and sounds) are correctly placed in their respective directories.
2. **Initial Screen**: Upon launch, the game displays a start menu with options like 'EASY', 'MEAN', and 'HARD'. Choose your desired difficulty level by clicking on these options.

### Gameplay Instructions

1. **Movement**: Use the left and right arrow keys on your keyboard to move your spaceship horizontally.
2. **Shooting**: Press the spacebar to shoot bullets at the descending aliens.
3. **Objective**: The goal is to shoot down as many aliens as possible before they reach the bottom of the screen. 
4. **Scoring**: Each alien shot increases your score, displayed at the top of the screen.
5. **End Game**: The game ends when an alien reaches the bottom of the screen or collides with your spaceship.

### Troubleshooting and FAQ

- **Game Doesn't Start**: Ensure Python and Pygame are correctly installed and that all game files are in their respective directories.
- **No Sound**: Check your system's audio settings and ensure the Pygame mixer is correctly initialized.
- **Game Too Fast/Slow**: The game's speed might vary based on your system's capabilities. Adjusting the game loop timing in `main.py` can help.

### Additional Information

- **Switching Difficulty**: You can switch the game's difficulty from the initial screen at any point before starting the gameplay.
- **Pausing the Game**: Currently, the game does not support a pause feature. You may stop the game by closing the game window.


## Successful Use Case Scenarios
### Use Case 1: Casual Gaming Experience

**User Profile**: Caio, a college student with a love for classic arcade games.

**Context**: Caio discovers the Space Invaders Clone while searching for a simple and enjoyable game to play during her study breaks.

**Narrative**:
- **Start**: Caio runs `main.py` and is greeted by the familiar Space Invaders theme.
- **During**: He selects 'EASY' difficulty and starts playing. Using arrow keys for movement and spacebar to shoot, he finds himself immersed in the nostalgic gameplay.
- **End**: After several rounds, he successfully beats her high score. He leaves the game feeling refreshed and entertained.

**Result**: Caio finds the game perfect for quick, relaxing breaks, helping him de-stress during his busy study schedule.

### Use Case 2: Introducing Classic Games to Youngsters

**User Profile**: João, a father looking to introduce his children to the games of his youth.

**Context**: João wants his children to experience the games he grew up with, starting with Space Invaders.

**Narrative**:
- **Start**: João sets up the game on his home computer and explains the basic controls to his kids.
- **During**: They take turns playing, each trying to outdo the other's high score. João helps them understand the strategies involved in the game.
- **End**: They spend a fun evening together, with his children gaining a new appreciation for classic games.

**Result**: The game becomes a regular family bonding activity, with João's children eager to explore more classic games.

### Use Case 3: Python Learning Tool

**User Profile**: Wesley, a computer science teacher looking for engaging ways to teach Python programming.

**Context**: Wesley wants his students to see practical applications of Python in an enjoyable way.

**Narrative**:
- **Start**: Wesley uses the Space Invaders Clone as an example in his class, showing the source code and explaining how it's structured.
- **During**: Students are tasked with modifying the code to change game elements, such as adding new alien types or altering game mechanics.
- **End**: Students are able to creatively express themselves through code and better understand Python programming.

**Result**: The project enhances students' learning experience, making Python programming more tangible and enjoyable.

## Problematic Use Case Scenarios
### Problem Scenario 1: Performance Issues on Older Hardware

**User Profile**: Alex, who has an older computer system.

**Problem**: Alex experiences lag and slow response times while playing the game.

**Cause**: The game might be too resource-intensive for older hardware.

**Solution**: Lower the game's resolution in the `main.py` file or update the hardware. If these options are not viable, running the game on a more modern system is recommended.

### Problem Scenario 2: Inconsistent Sound Effects

**User Profile**: Sara, who plays the game on her laptop.

**Problem**: Occasionally, sound effects are either delayed or don't play at all.

**Cause**: This could be due to issues with Pygame's mixer initialization or conflicts with other audio software.

**Solution**: Restart the game and check if the problem persists. Ensure that the latest version of Pygame is installed and no other audio-intensive applications are running simultaneously.

### Problem Scenario 3: Difficulty in Understanding Game Mechanics

**User Profile**: Pedro, a new player to Space Invaders Clone.

**Problem**: Pedro finds it hard to grasp the game mechanics and controls.

**Cause**: Lack of an in-game tutorial or help section.

**Solution**: Refer to the user manual and README for detailed instructions. Practice in 'EASY' mode to get familiar with the game's mechanics.


## Project Complexity
The project has moderate complexity, focusing on the robustness of the game loop and efficient implementation of collision algorithms.

## Reliability and Usability
The game is designed to be intuitive and easy to play, with a clear user interface and a stable gaming experience.

## Technical Documentation and Third-Party Utilization
The code documentation is comprehensive, allowing other developers to understand and modify the game as needed.

## Comprehensive and Satisfactory Testing
Tests have been conducted to ensure the stability of the game and the correct implementation of gameplay rules. The core functions of the game were tested using unit tests.
