# 950. Reveal Cards In Increasing Order

# You are given an integer array deck. There is a deck of cards where every card has a unique integer. The integer on the ith card is deck[i].

# You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

# You will do the following steps repeatedly until all cards are revealed:

# Take the top card of the deck, reveal it, and take it out of the deck.
# If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
# If there are still unrevealed cards, go back to step 1. Otherwise, stop.
# Return an ordering of the deck that would reveal the cards in increasing order.

# Note that the first entry in the answer is considered to be the top of the deck.



from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        # [2,3,5,7,11,13,17]
        # [17]
        result=[0]*len(deck)
        index=deque(range(len(deck)))


        for i in sorted(deck):
            q=index.popleft()
            result[q]=i
            if(index):
                index.append(index.popleft())
        return result