# Asteroids

A small Asteroids-style game written in Python using Pygame.

The player controls a ship, avoids incoming asteroids, and can shoot them. When a shot hits an asteroid, the asteroid splits or disappears. If the player collides with an asteroid, the game ends.

## Requirements

- Python
- uv
- Pygame

This project is intended to be run with `uv`, because it manages the Python version and dependencies for the project. Unfortunately, pygame doesn't yet support Python 3.14. Until it's updated, it is recommend to use Python 3.13.

## Run the game

From the project folder, run:

```bash
uv run main.py
```

Do not run the game directly with:

```bash
python main.py
```

unless you have installed the required dependencies manually in your current Python environment.

If you see this error:

```text
ModuleNotFoundError: No module named 'pygame'
```

it means that `pygame` is not installed in the Python environment you are currently using.

## Install dependencies manually

If you do not want to use `uv`, you can install Pygame manually:

```bash
pip install pygame
```

Then run:

```bash
python main.py
```

However, using `uv run main.py` is recommended for this project.

## Project structure

```text
.
├── main.py
├── constants.py
├── player.py
├── asteroid.py
├── asteroidfield.py
├── shot.py
└── logger.py
```

## Notes

This project is mainly for practicing Python, Pygame, game loops, sprite groups, collision detection, and basic object-oriented programming.

The game currently ends when the player is hit by an asteroid.
