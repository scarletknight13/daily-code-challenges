# Time Comp: O(N)
# Space Comp: O(N)
def pivotIndex(self, arr):
        #Solution uses concept called prefix and suffix array
        #The idea is to create an array that stores the sum of numbers before an index(prefix)
        # and an array that stores the sum of numbers after an index(suffix)
        total = 0
        n = len(arr)
        pre = []
        suff = [0 for x in range(n)]
        for i in arr:
            pre.append(total)
            total += i

        total = 0
        for i in range(n - 1, -1, -1):
            suff[i] = total
            total += arr[i]
        for i in range(n):
            if pre[i] == suff[i]:
                return i
        return -1