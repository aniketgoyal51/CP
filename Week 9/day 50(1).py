# 2225. Find Players With Zero or One Losses

# You are given an integer array matches where matches[i] = [winneri, loseri] indicates that the player winneri defeated player loseri in a match.

# Return a list answer of size 2 where:

# answer[0] is a list of all players that have not lost any matches.
# answer[1] is a list of all players that have lost exactly one match.
# The values in the two lists should be returned in increasing order.

# Note:

# You should only consider the players that have played at least one match.
# The testcases will be generated such that no two matches will have the same outcome.



class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        loss_count = Counter()

        for winner, loser in matches:
            loss_count[loser] += 1
            if winner not in loss_count:
                loss_count[winner] = 0

        no_loss = [player for player, losses in loss_count.items() if losses == 0]
        one_loss = [player for player, losses in loss_count.items() if losses == 1]

        return [sorted(no_loss), sorted(one_loss)]
