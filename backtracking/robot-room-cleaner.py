# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot: 'Robot') -> None:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(i: int, j: int, dir_idx: int) -> None:
            visited.add((i, j))
            robot.clean()


            for _ in range(4):
                di, dj = directions[dir_idx]
                ni, nj = i + di, j + dj

                if (ni, nj) not in visited and robot.move():
                    dfs(ni, nj, dir_idx)
                    go_back()


                dir_idx = (dir_idx + 1) % 4
                robot.turnRight()

        dfs(0, 0, 0)