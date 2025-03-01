from player import Player
import random

class Game:
    def __init__(self, players):
        self.players = players
        self.player = players[0]
        self.turn_count = 0
        self.running = True

    def start(self):
        while self.running and self.turn_count < 5:
            self.turn_count += 1
            print(f"\n===== {self.turn_count}ターン目 =====")

            player = self.players[0]
            print(f"{player.name} の現在の十字架の数: {player.crosses}")

            self.show_menu(player)

            if self.turn_count == 3:
                self.midgame_report()

        self.end_game()
    
    def midgame_report(self):
        angels, demons = self.count_roles()
        print("\n=== ここで3ターン目の中間発表です ===")
        print(f"天使: {angels}人")
        print(f"悪魔: {demons}人")
    
    def count_roles(self):
        angels = sum(1 for player in self.players if player.role == "天使")
        demons = sum(1 for player in self.players if player.role == "悪魔")
        return angels, demons
    
    def show_menu(self, player):
        print("次のアクションを選んでね")
        print("1. 審判の部屋に入る")
        print("2. 誰かと接触する")
        print("3. 何もしない")

        choice = input("選択: ")

        if choice == "1":
            self.judgement_room(player)
        elif choice == "2":
            self.interact(player)
        elif choice == "3":
            print(f"{player.name} は何もしなかった...")
        else:
            print("!!!INVALID SELECT!!!TRY AGAIN!!!")
    
    def play_turn(self, player):
        self.show_menu(player)
    
    def interact(self, player):
        target = random.choice([p for p in self.players if p != player])
        print(f"{player.name} は {target.name} に接触した...")
        
        if target.role == "悪魔":
            if player.role == "天使":
                print(f"{target.name} は悪魔だった！👿")
                if player.use_cross():
                    player.become_angel()
                else:
                    player.become_demon()
            else:
                print("何も起こらなかった")

    def end_game(self):
        total_crosses = sum(p.crosses for p in self.players if p.role == "天使")
        if total_crosses >= 5:
            print("おめでとう！十字架を５つ以上集めることができた！")
        else:
            print("💀ゲームオーバー💀十字架が足りなかった...")
        self.running = False
    
    def judgement_room(self, player):
        print(f"\n {player.name} は審判の部屋に入った...")
        print(f"👁️ あなたは現在【{player.role}】です")

if __name__ =="__main__":
    players = [Player(f"Player{i}", random.choice([True, False])) for i in range(10)]
    game = Game(players)
    game.start()