import copy

class Solution:
    def merge(self, intervals):
        if intervals == []:
            return intervals
        intervals.sort()
        begin = intervals[0][0]
        end = intervals[0][1]
        rst = list()
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                rst.append([begin, end])
                begin = intervals[i][0]
                end = intervals[i][1]
            else:
                if intervals[i][1] > end:
                    end = intervals[i][1]
        rst.append([begin, end])
        return rst
                    
                    
    def cover_spcace(self,dirA,dirB):
        print(dirA, dirB)
        if max(dirA[0], dirB[0]) <= min(dirA[1],dirB[1]):
            return True
        else:
            return False
        
    def merge_set(self, dirA,dirB):
        newDir = (min(dirA[0],dirB[0]),max(dirA[1],dirB[1]))
        return newDir
        
if __name__ == "__main__":
    listA = [[1,3],[2,6],[8,10],[15,18]]
    listA =[[1,4],[4,5]]
    listA = [[1,4],[0,2],[3,5]]

    rst = [[1,6],[8,10],[15,18]]
    S = Solution()
    print(S.merge(listA))