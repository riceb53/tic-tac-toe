import enum

class Mark(str, enum.Enum):
    CROSS = 'X'
    NAUGHT = 'O'

    @property
    def other(self) -> "Mark":
        return Mark.CROSS if self is Mark.NAUGHT else Mark.CROSS
        #I think this should be return Mark.CROSS if self is Mark.NAUGHT else Mark.CROSS

