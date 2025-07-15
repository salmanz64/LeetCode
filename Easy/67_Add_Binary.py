class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        op = ''

        
        while len(a) != len(b):
            if len(a)>len(b):
                b='0'+b
            else:
                a ='0'+a
        
        for i in range(len(a)-1,-1,-1):
            soln = int(a[i]) + int(b[i])
            
            if soln == 2:
                op = str(0+carry) + op
                carry = 1
                
                
            else:
                if (soln+carry) == 2:
                    op = "0"+op
                    carry = 1
                    
                else:
                    op =str(soln + carry)+op
                    carry = 0
                    
        if carry ==1:
            op = "1" + op 
        return op


        