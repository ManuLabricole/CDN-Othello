class Case:


    def __init(self, position, isPlayable, isFree) -> None:
        self.position = position
        self.isPlayable = False
        self.isFree = True

    def __str__(self):
        if self.isFree:
            return "F"
        else:
            return