# 🔤 Word Guessing Game

A simple command-line word guessing game written in Python. The computer randomly selects a word, and the player must guess it one letter at a time.

## 📖 About the Project

In this game:

- The computer randomly selects a word from a predefined word list.
- The player guesses one letter at a time.
- Correct letters are revealed in their correct positions.
- Incorrect guesses are rejected.
- The game continues until the entire word is guessed.

This project is a great way to practice Python fundamentals such as loops, functions, strings, lists, and the `random` module.

---

## ✨ Features

- Random word selection
- Letter-by-letter guessing
- Displays guessed letters
- Prevents duplicate guesses
- Shows the player's progress after each guess
- Simple command-line interface

---

## 🛠 Requirements

- Python 3.x

No external libraries are required.

---

## 📁 Project Structure

```text
Word-Guessing-Game/
│
├── main.py
├── sozlar.py
└── README.md
```

### `sozlar.py`

This file contains a list of words used by the game.

Example:

```python
words = [
    "python",
    "computer",
    "keyboard",
    "programming",
    "algorithm"
]
```

---

## 🚀 Getting Started

Clone the repository:

```bash
git clone https://github.com/AbduvaxobovAbror/your-repository-name.git
```

Navigate to the project directory:

```bash
cd your-repository-name
```

Run the game:

```bash
python main.py
```

---

## 💻 Example

```text
I have chosen a 6-letter word.

------
Enter a letter: P

P-----
Guessed letters: P

Enter a letter: Y

PY----
```

The game continues until the player guesses the complete word.

---

## 📚 Technologies Used

- Python 3
- Random Module

---

## 🎯 Concepts Practiced

- Functions
- Loops (`while`)
- Conditional Statements
- Strings
- Lists
- Sets
- User Input
- Random Module

---

## 👨‍💻 Author

**Abror Abduvahobov**

GitHub: https://github.com/AbduvaxobovAbror

---

## 📄 License

This project is licensed under the MIT License.
