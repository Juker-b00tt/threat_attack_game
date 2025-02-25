class Player:
    def __init__(self, name, role="angel"):
        self.name = name
        self.role = role #angel or demon
        self.crosses = 1 #start with one crosses

    def become_demon(self):
        self.role = 'demon'
        print(f"{self.name} は悪魔になった!")

    def become_angel(self):
        self.role = 'angel'
        print(f"{self.name} は天使になった!")
    
    def add_cross(self):
        self.crosses += 1
        print(f"{self.name} は十字架を手に入れた! (合計: {self.crosses})")
    
    def use_cross(self):
        if self.crosses > 0:
            self.crosses -= 1
            print(f"{self.name} は十字架を使った! (残り: {self.crosses})")
            return True
        else:
            print(f"{self.name} は十字架がない!")
            return False