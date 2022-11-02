#Author: Akhil Sharma
#Date: 11/01/2022

#Algorithm: store assignments as dict and compute, only check for + or - 

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        op_dict = {"+" : 1, "-": -1}
        return sum(op_dict[op[1]] for op in operations)
