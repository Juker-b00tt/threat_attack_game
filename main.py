from player import Player
import random

class Game:
    def __init__(self, num_players=10):
        self.players = [Player(f"プレイヤー{i+1}") for i in range(num_players)]
        self.turns = 5
        self.current_turn = 1
        self.running = True
        self.assign_initial_demons()
    
    def assign_initial_demons(self):
        demons = random.sample(self.players, 2)
        for demon in demons:
            demon.become_demon()
    
    def start(self):
        print("天使と悪魔ゲームへようこそ！")
        while self.running and self.current_turn <= self.turns:
            print(f"\n--- ターン {self.current_turn} ---")
            self.play_turn()
            self.current_turn += 1
        self.end_game()
    
    def play_turn(self):
        for player in self.players:
            if player.role == "angel":
                self.scan_threat(player)
    
    def scan_threat(self,player):
        result = random.choice(["success", "fail"])
        if result == "success":
            player.add_cross()
        else:
            print(f"{player.name} のスキャン失敗！")
            if player.use_cross():
                player.become_angel()
            else:
                player.become_demon()
    
    def end_game(self):
        total_crosses = sum(player.crosses for player in self.players if player.role =="angel")
        if total_crosses >= 5:
            print("🎉勝利！十字架を５つ以上集めた！")
        else:
            print("💀ゲームオーバー💀十字架が足りなかった...")
        self.running = False

if __name__ =="__main__":
    game = Game()
    game.start()