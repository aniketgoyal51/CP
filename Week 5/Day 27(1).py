# Question
# Number of Laser Beams in a Bank
# Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor 
# plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is 
# empty, while'1' means the cell has a security device.

# There is one laser beam between any two security devices if both conditions are met:

# The two devices are located on two different rows: r1 and r2, where r1 < r2.
# For each row i where r1 < i < r2, there are no security devices in the ith row.
# Laser beams are independent, i.e., one beam does not interfere nor join with another.

# Return the total number of laser beams in the bank.



class Solution(object):
    def numberOfBeams(self, bank):
        """
        :type bank: List[str]
        :rtype: int
        """
        ans=0
        fi=0
        si=1
        while si!=len(bank) and fi!=len(bank)-1:
            # print("--------------")
            # print(fi)
            # print(si)
            # print("--------------")

            if(fi==si):
                si+=1
                continue
            if "1" not in bank[fi]:
                # si+=1
                fi+=1
                continue 
            if "1" not in bank[si]:
                si+=1
                continue
            count=bank[fi].count("1")
            count1=bank[si].count("1")
            ans+=count*count1
            fi+=1
            si+=1
            # print(count)
            # print(count1)
        return ans