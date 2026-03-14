class SnapshotArray:

    def __init__(self, length: int):
        self.snap_id = 0
        self.data = [[(0, 0) for _ in range(length)]]
        

    def set(self, index: int, val: int) -> None:
        if self.data[index][-1][0] == self.snap_id:
            self.data[index][-1] = (self.snap_id, val)
        else:
            self.data[index].append((self.snap_id, val))
        

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1
        

    def get(self, index: int, snap_id: int) -> int:
        history = self.data[index]
        ids = [s for s, v in history]
        pos = bisect_right(ids, snap_id) - 1
        return history[pos][1]
        


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)