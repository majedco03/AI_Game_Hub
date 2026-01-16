# 🎮 AI Game Hub

## CSC 361 - Artificial Intelligence Project

A collection of classic puzzle and strategy games featuring AI solvers and opponents, built with Python and Tkinter.

**Instructor:** Mohamed Maher Ben Ismail

---

## 📋 Overview

AI Game Hub is a unified gaming platform that brings together three classic games, each demonstrating different AI techniques and algorithms:

| Game | AI Techniques | Developer |
|------|---------------|-----------|
| **Sudoku** | CSP with MRV, Backtracking, SA | Mohammed Alwanis GitHub: Pb22j|
| **Connect 4** | Minimax with Alpha-Beta Pruning, Adaptive Learning | Majed Aldajani |
| **8-Puzzle** | A* Search, Heuristic Functions | Alwaleed AlMutairi GitHub: AlwaleedAlmutairi |

---

## 🎯 Games

### 🔢 Sudoku
A puzzle solver that demonstrates constraint satisfaction problem (CSP) techniques.

**Features:**
- Multiple difficulty levels (Easy → Extreme)
- Three solving algorithms:
  - **Naive Backtracking** - Simple recursive approach
  - **Smart CSP (MRV)** - Minimum Remaining Values heuristic for smarter cell selection
  - **Simulated Annealing** - Probabilistic optimization approach
- Step-by-step visualization of the solving process
- Statistics tracking (steps, backtracks, time)

---

### 🔴🟡 Connect 4
The classic two-player strategy game with intelligent AI opponents.

**Features:**
- Human vs Human, Human vs AI, or AI vs AI modes
- Two AI agents:
  - **Minimax Agent** - Classic game tree search with Alpha-Beta pruning
    - Easy (depth 2), Medium (depth 4), Hard (depth 6)
  - **Adaptive/Evolving Agent** - Self-improving AI that learns from each game
- Full-screen GUI with smooth animations

For detailed information about the Connect 4 AI implementation, see [Connect4_game/README.md](Connect4_game/README.md)

---

### 🧩 8-Puzzle
The sliding tile puzzle with AI-powered solving capabilities.

**Features:**
- Interactive tile sliding interface
- A* search algorithm with multiple heuristics:
  - Manhattan Distance
  - Misplaced Tiles
- Visual step-by-step solution playback
- Move counter and solution path display

---

## 🚀 Installation

### Requirements
- Python 3.8 or higher
- Tkinter (usually included with Python)
- NumPy (optional, for Sudoku's Simulated Annealing algorithm)

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/majedco03/AI_Game_Hub.git
   cd AI_Game_Hub
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # or
   .venv\Scripts\activate     # Windows
   ```

3. Install optional dependencies:
   ```bash
   pip install numpy  # For Simulated Annealing in Sudoku
   pip install py-sudoku  # For puzzle generation
   ```

---

## ▶️ Running the Application

### Launch the Game Hub (All Games)
```bash
python3 GameHubApp.py
```

### Run Individual Games
```bash
# Sudoku
python3 Sudoku_game/sudoku_gui.py

# Connect 4
python3 Connect4_game/main.py

# 8-Puzzle
python3 eight_puzzle_gui.py
```

### Train the Adaptive Connect 4 Agent
```bash
python3 Connect4_game/src/train.py
```

---

## 📁 Project Structure

```
AI_Game_Hub/
├── GameHubApp.py              # Main launcher for all games
├── README.md                  # This file
│
├── Sudoku_game/
│   ├── sudoku_gui.py          # Sudoku GUI
│   └── sudoku_game.py         # Game logic and AI solvers
│
├── Connect4_game/
│   ├── main.py                # Connect 4 launcher
│   ├── connect4_gui.py        # Connect 4 GUI
│   ├── README.md              # Detailed Connect 4 documentation
│   └── src/
│       ├── board.py           # Game board logic
│       ├── minimax_agent.py   # Minimax AI with Alpha-Beta pruning
│       ├── adaptive_minimax.py# Self-learning AI agent
│       ├── train.py           # Training script
│       └── agent_weights.json # Saved learned weights
│
└── eight_puzzle_gui.py        # 8-Puzzle game and solver
```

---

## ⌨️ Controls

- **ESC** - Exit fullscreen mode
- **F11** - Toggle fullscreen mode

---

## 👥 Team

| Name | Contribution |
|------|-------------|
| **Mohammed Alwanis** | Sudoku Solver |
| **Majed** | Connect 4 Game & AI Agents |
| **Alwaleed AlMutairi** | 8-Puzzle Solver |

---

## 📄 License

This project was developed as part of the CSC 361 - Artificial Intelligence course in King Saud University.
