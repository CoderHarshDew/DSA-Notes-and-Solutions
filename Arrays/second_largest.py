# Problem: Second Largest
# Source: GeeksForGeeks
# Difficulty: Easy
# Category: Array
# Notes:
# - Returns -1 if all elements are equal or array length < 2.
# - Mutates the input array by removing the maximum values.

class Solution:
    def getSecondLargest(self, arr):
        greatest = max(arr)
        itr = arr.count(greatest)
        arr_len = len(arr)
        if arr_len == itr:
            return -1
        for i in range(itr):
            arr.remove(greatest)
        return max(arr)

# --- Minimal driver / usage examples for local runs (not required by GFG) ---
if __name__ == "__main__":
    s = Solution()
    # Basic cases
    print(s.getSecondLargest([1, 2, 3]))          # 2
    print(s.getSecondLargest([10, 10, 9]))        # 9
    print(s.getSecondLargest([5, 5, 5]))          # -1
    print(s.getSecondLargest([1]))                # -1 (len < 2 handled by logic)
    print(s.getSecondLargest([2, 2, 3, 3, 1]))    # 2

    # Be aware: the method MUTATES the list (removes all max elements)
    a = [4, 7, 7, 2]
    out = s.getSecondLargest(a)
    print(out, a)  # 4, and a becomes [4, 2]
