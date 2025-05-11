class MergeArrays:
    def merge(self, array1, array2):
        # Initialize pointers and the merged result list
        i, j, merged = 0, 0, []

        # Loop through both arrays while there are elements in both
        while i < len(array1) and j < len(array2):
            # Compare elements and append the smaller one to the merged list
            if array1[i] < array2[j]:
                merged.append(array1[i])
                i += 1
            else:
                merged.append(array2[j])
                j += 1

        # Append any remaining elements from array1 (if any)
        merged.extend(array1[i:])
        # Append any remaining elements from array2 (if any)
        merged.extend(array2[j:])

        return merged


sol = MergeArrays()
print(sol.merge(array1=[1, 2, 9], array2=[5, 6, 7]))
















