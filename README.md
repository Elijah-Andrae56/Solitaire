# Solitaire

This repository contains a simple command line implementation of the solitaire card game written in Python. The code lives inside the `Cards` directory and is split across a few modules.

## Module overview

- **`cards.py`** – Defines the `Card` class used to represent each playing card.
- **`deck.py`** – Provides the `BuildDeck` helper that generates and shuffles a standard deck.
- **`piles.py`** – Implements data structures for the tableau, foundations and stock pile.
- **`moves.py`** – Contains logic for handling player moves.
- **`main.py`** – Entrypoint for starting the game.

## Running the game

Ensure you have Python installed (version 3.10 or newer is recommended). Then run:

```bash
python Cards/main.py
```

The game will prompt you in the terminal for actions such as flipping or grabbing cards.

## Running the tests

Any automated tests can be executed using [pytest](https://pytest.org/). From the repository root run:

```bash
pytest
```

At present the project does not contain formal unit tests so running the above command will simply report that no tests were found.
