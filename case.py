class Case:

    def __init__(self, position, isPlayable, isFree) -> None:
        self.position = position
        self.isPlayable = False
        self.isFree = True

    def __str__(self):
        if self.isFree:
            return "F"
        else:
            return
    
    def __repr__(self) -> str:
        return f"{self.position}"
