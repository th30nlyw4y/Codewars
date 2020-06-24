class User:

    ranks = [x for x in range(-8, 9) if x != 0]

    def __init__(self):
        self.progress = 0
        self._index = 0
        self.rank = User.ranks[self._index]

    @staticmethod
    def validate_input(activity_rank):
        if not (-9 < activity_rank < 9) or activity_rank == 0:
            raise ValueError

    def progress_check(self):
        if self.progress >= 100:
            self._index += self.progress//100 if (self._index + self.progress//100) < 16 else 15
            self.rank = User.ranks[self._index]
        self.progress = self.progress % 100 if (self._index < 15) else 0

    def inc_progress(self, activity_rank):
        self.validate_input(activity_rank)
        if self.rank < activity_rank:
            self.progress += 10 * (self._index - User.ranks.index(activity_rank))**2
        elif self._index == User.ranks.index(activity_rank):
            self.progress += 3
        elif self._index - User.ranks.index(activity_rank) == 1:
            self.progress += 1
        self.progress_check()





