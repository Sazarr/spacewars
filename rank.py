class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def rank_to_index(self, rank):

        return rank + 8 if rank < 0 else rank + 7

    def index_to_rank(self, index):

        return index - 8 if index < 8 else index - 7



    def inc_progress(self, activity_rank):
        if activity_rank == 0 or activity_rank < -8 or activity_rank > 8:
            raise ValueError("Invalid rank value")

        user_index = self.rank_to_index(self.rank)
        activity_index = self.rank_to_index(activity_rank)

        diff = activity_index - user_index

        if diff == -1:
            self.progress += 1
        elif diff == 0:
            self.progress += 3
        elif diff > 0:
            self.progress += 10 * diff * diff

        self.update_rank()


    def update_rank(self):
        while self.progress >= 100 and self.rank < 8:
            self.progress -= 100
            self.rank = self.index_to_rank(self.rank_to_index(self.rank) + 1)

        if self.rank == 8:
            self.progress = 0


class User:
    Ranks = [-8, -7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7, 8]

    def __init__(self):
        self.__rank = -8
        self.__progress = 0

    @property
    def rank(self):
        return self.__rank

    @property
    def progress(self):
        return self.__progress

    def inc_progress(self, kata_rank):
        self.__validate_rank(kata_rank)
        progress_made = self.__calc_progress(kata_rank)
        new_progress = self.progress + progress_made
        extra_rank, progress_left = self.__calc_rank(new_progress)
        self.__update_rank(extra_rank)
        self.__update_progress(progress_left)

    def __validate_rank(self, in_rank):
        if (in_rank not in self.Ranks):
            raise ValueError("Rank must be in range [-8,-1]U[1,8]")

    def __calc_progress(self, kata_rank):
        diff = self.Ranks.index(kata_rank) - self.Ranks.index(self.rank)
        if (kata_rank > self.rank):
            return 10 * diff ** 2
        elif (kata_rank == self.rank):
            return 3
        elif (diff == - 1):
            return 1
        else:
            return 0

    def __calc_rank(self, new_progress):
        extra_rank = 0
        progress_left = new_progress
        if (new_progress > 99 and self.rank < 8):
            extra_rank = new_progress // 100
            progress_left = new_progress % 100
        return extra_rank, progress_left

    def __update_progress(self, new_progress):
        self.__progress = new_progress
        if (self.rank == 8 and self.progress > 0):
            self.__progress = 0

    def __update_rank(self, extra_rank):
        new_rank = self.rank + extra_rank
        if (self.rank < 0 and new_rank >= 0):
            new_rank = new_rank + 1
        if (new_rank > 8):
            self.__rank = 8
        else:
            self.__rank = new_rank