# 165. Compare Version Numbers

# Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.

# To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

# Return the following:

# If version1 < version2, return -1.
# If version1 > version2, return 1.
# Otherwise, return 0.



class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")

        c=0

        while len(v1)>c or len(v2)>c:
            v1_part = int(v1[c]) if c < len(v1) else 0
            v2_part = int(v2[c]) if c < len(v2) else 0

            if(v1_part>v2_part):
                return 1
            elif(v1_part<v2_part):
                return -1
            else:
                c+=1
        return 0