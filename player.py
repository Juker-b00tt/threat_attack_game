class Player:
    def __init__(self, name, is_demon=False):
        self.name = name
        self.role = "悪魔" if is_demon else "天使" #angel or demon
        self.crosses = 0 if is_demon else 1 #start with one crosses

    def __repr__(self):
        return self.name
    
    def become_demon(self):
        self.role = '悪魔'
        print(f"{self.name} は悪魔になった!")

    def become_angel(self):
        self.role = '天使'
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