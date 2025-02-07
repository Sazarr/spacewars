class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0

    def rank_to_index(self, rank):
        """Convert rank to a continuous index for easier calculations."""
        return rank + 8 if rank < 0 else rank + 7

    def index_to_rank(self, index):
        """Convert index back to the ranking system."""
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
            self.progress = 0  # Cap progress at rank 8


# Example usage
user = User()
print(user.rank)  # -8
print(user.progress)  # 0

user.inc_progress(-7)
print(user.progress)  # 10

user.inc_progress(-5)
print(user.progress)  # 0
print(user.rank)  # -7
