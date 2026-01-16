# train.py
import json
import time
import random
from board import Board
from adaptive_minimax import EvolvingMinimaxAgent
from minimax_agent import MinimaxAgent

trainingSchedule = [
    # games, difficulty
    (1, 'easy'),
    (1, 'medium'),
    (10, 'hard')
]

trainingDepth = 4  # i have specified this depth to maintain a balance 
# between training quality and time

class Trainer:
    def __init__(self): 
        self.evolving = EvolvingMinimaxAgent(player=1)
        self.evolving.depth = trainingDepth

    def playGame(self, oppDiff, evolvingGoesFirst=True):
        game = Board()
        
        if evolvingGoesFirst:
            # evolving agent is player 1
            self.evolving.player = 1
            opp = MinimaxAgent(player=2, difficulty=oppDiff)
            agents = {1: self.evolving, 2: opp}
        else:
            # evolving agent is player 2 (opponent goes first)
            self.evolving.player = 2
            opp = MinimaxAgent(player=1, difficulty=oppDiff)
            agents = {1: opp, 2: self.evolving}
        
        while not game.gameOver:
            agent = agents[game.turn]
            move = agent.get_move(game)
            game.drop_piece(move)
            self.evolving.record_game_state(game)
        
        self.evolving.finalize_game(game)
        
        # Return 1 if evolving agent won, 0 otherwise
        winner = game.checkWinState()
        return 1 if winner == self.evolving.player else 0

    def train(self):
        start = time.time()
        for num, diff in trainingSchedule:
            wins = 0
            print(f"\nTraining vs {diff.upper()} ({num} games, alternating first player)...")
            for i in range(num):
                # not always the evolving agent goes first but alternates to reduce bias
                evolvingFirst = (i % 2 == 0)
                result = self.playGame(diff, evolvingGoesFirst=evolvingFirst)
                wins += result
                if (i + 1) % 25 == 0:
                    print(f"  Progress: {i+1}/{num} | Wins: {wins} ({wins/(i+1)*100:.1f}%)")
            print(f"{diff.upper()} stage complete: Wins {wins}/{num} ({wins/num*100:.2f}%)")
        
        # reset evolving agent back to player 1
        self.evolving.player = 1
        self.evolving.saveWeights()
        
        print(f"\nTraining done in {time.time()-start:.1f}s.")

if __name__ == "__main__":
    trainer = Trainer()
    trainer.train()