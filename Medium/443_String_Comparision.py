#my sol
class Solution:
    def compress(self, chars: List[str]) -> int:
        first = 0
        last = 0
        count =0
        op = [chars[first]]
        for i in range(len(chars)):
            if chars[i] == chars[first]:
                count+=1
                last+=1
            else:
                if count !=1:
                    if count >=10:
                        op.extend(list(str(count)))
                    else:
                        op.append(str(count))
                last = i
                first = i
                op.append(chars[i])
                count =1
        if count!=1:
            if count >=10:
                op.extend(list(str(count)))
            else:
                op.append(str(count))
        chars[:]= op
        return len(chars)
    
    
#best Efficient
while read < len(chars):
    # count same consecutive chars
    while read < len(chars) and chars[read] == char:
        read += 1
        count += 1

    # write char once
    chars[write] = char
    write += 1

    # write count digits (if count > 1)
    for digit in str(count):
        chars[write] = digit
        write += 1

        