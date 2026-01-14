#Given a signed 32-bit integer x, return x with its digits reversed. 
#If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1],
#  then return 0.

#Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
class Solution:
    def reverse(self, x: int) -> int:
        if not isinstance(x,int):
            raise TypeError("X must be an integer")
        if not -(2**31) <=x <=(2**31)-1:
            raise ValueError("out of bound value")
        is_negative = x < 0
        number_str = str(abs(x))
        reverse_int = int(number_str[::-1])
        rev = -reverse_int if is_negative else reverse_int
        return rev if -(2**31) <= rev <= (2**31)-1 else 0
    
sol = Solution()
x= 1534236469
print(sol.reverse(x))


        

 