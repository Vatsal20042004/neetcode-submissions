class TimeMap:

    def __init__(self):
        self.timeMap={}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key]=self.timeMap.get(key,[])
        self.timeMap[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        if key in self.timeMap:
            left=0
            right=len(self.timeMap[key])-1
            if timestamp<self.timeMap[key][0][0]:
                return ''
            elif timestamp>self.timeMap[key][-1][0]:
                return self.timeMap[key][-1][1]
            while left<=right:
                mid=(left+right)//2
                if self.timeMap[key][mid][0]==timestamp:
                    return self.timeMap[key][mid][1]
                elif self.timeMap[key][mid][0]<timestamp:
                    left=mid+1
                else:
                    right=mid-1
            mid=(left+right)//2
            if self.timeMap[key][mid][0]<timestamp:
                return self.timeMap[key][mid][1]
            else:
                if self.timeMap[key][mid-1] in timeMap[key]:
                    return timeMap[key][mid-1][1]
                else:
                    return ''

        else:
            return ''
