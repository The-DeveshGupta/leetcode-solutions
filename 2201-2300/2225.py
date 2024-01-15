class Solution:

    def __init__(self):
        self.lost_none = []
        self.lost_once = []
        self.lost_more = []

    def _exist(self, _list, num):
        b_left, b_right = bisect_left(_list, num), bisect_right(_list, num)
        return b_left != b_right

    def _insert(self, _list, num):
        b_left = bisect_left(_list, num)
        _list.insert(b_left, num)

    def _remove(self, _list, num):
        b_right = bisect_right(_list, num)
        _list.pop(b_right - 1)

    def have_won(self, player):
        if self._exist(self.lost_none, player) or self._exist(self.lost_once, player) or self._exist(self.lost_more,
                                                                                                     player):
            pass
        else:
            self._insert(self.lost_none, player)

    def have_lost(self, player):
        if self._exist(self.lost_more, player):
            pass
        elif self._exist(self.lost_once, player):
            self._remove(self.lost_once, player)
            self._insert(self.lost_more, player)
        else:
            if self._exist(self.lost_none, player):
                self._remove(self.lost_none, player)
            self._insert(self.lost_once, player)

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        for match in matches:
            self.have_won(match[0])
            self.have_lost(match[1])
        return self.lost_none, self.lost_once
