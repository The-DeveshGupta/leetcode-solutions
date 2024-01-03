class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        beams = 0
        prev_device = 0

        for row in bank:
            device = sum([int(cell) for cell in row])
            if device:
                beams += prev_device * device
                prev_device = device

        return beams
