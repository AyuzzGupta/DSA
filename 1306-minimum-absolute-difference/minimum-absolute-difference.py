class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        mnd = arr[1] - arr[0]

        # Minimum difference find karo
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] < mnd:
                mnd = arr[i] - arr[i - 1]

        l = []

        # Minimum difference wale pairs add karo
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] == mnd:
                l.append([arr[i - 1], arr[i]])

        return l
