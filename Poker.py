from itertools import combinations

# Define card rank values (Ace is high only)
RANKS = "23456789TJQKA"
RANK_VALUES = {r: i for i, r in enumerate(RANKS, start=2)}


def get_hand_rank(hand):
    """ Determines the best poker hand from a given set of 5 cards. """
    suits = [s for _, s in hand]
    ranks = sorted([RANK_VALUES[r] for r, _ in hand], reverse=True)

    # Count occurrences of each rank
    rank_counts = {r: ranks.count(r) for r in ranks}
    sorted_ranks = sorted(rank_counts.keys(), key=lambda r: (-rank_counts[r], -r))

    # Check for flush (all suits same)
    is_flush = len(set(suits)) == 1

    # Check for straight (consecutive ranks)
    is_straight = ranks == list(range(ranks[0], ranks[0] - 5, -1))

    if is_flush and is_straight:
        return ("straight-flush", sorted_ranks)

    if 4 in rank_counts.values():
        return ("four-of-a-kind", sorted_ranks)

    if sorted(rank_counts.values()) == [2, 3]:
        return ("full house", sorted_ranks)

    if is_flush:
        return ("flush", sorted_ranks)

    if is_straight:
        return ("straight", sorted_ranks)

    if 3 in rank_counts.values():
        return ("three-of-a-kind", sorted_ranks)

    if list(rank_counts.values()).count(2) == 2:
        return ("two pair", sorted_ranks)

    if 2 in rank_counts.values():
        return ("pair", sorted_ranks)

    return ("high card", sorted_ranks)
def hand(hole_cards, community_cards):
    """ Determines the best possible hand from 7 available cards. """
    cards = hole_cards + community_cards
    possible_hands = combinations(cards, 5)

    # Find the best hand out of all possible 5-card hands
    best_hand = max(map(get_hand_rank, possible_hands), key=lambda h: (hand_strength[h[0]], h[1]))
    return best_hand

# Define strength of hand types
hand_strength = {
    "high card": 1,
    "pair": 2,
    "two pair": 3,
    "three-of-a-kind": 4,
    "straight": 5,
    "flush": 6,
    "full house": 7,
    "four-of-a-kind": 8,
    "straight-flush": 9
}
