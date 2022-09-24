class TimeMap:

    def __init__(self):
        self.obj = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        
        if key not in self.obj:
            self.obj[key] = [[value, timestamp]]
        else:
            self.obj[key].append([value, timestamp])        
        return
        

    def get(self, key: str, timestamp: int) -> str:
        
        if key not in self.obj:
            return ''
        else:
            valuesList = self.obj[key]
            valToReturn = ''

            low = 0
            high = len(valuesList) - 1

            while low <= high:

                mid = (low+high)//2
                currObj = valuesList[mid]
                currVal = currObj[0]
                currTimestamp = currObj[1]

                if currTimestamp > timestamp:
                    high = mid - 1

                elif currTimestamp <= timestamp:
                    valToReturn = currVal
                    low = mid + 1

            return valToReturn
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
