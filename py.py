class Solution:
    def calculate(self, s):    
        def calc(tmp):
            def update(op, v):
                if op == "+": stack.append(v)
                if op == "-": stack.append(-v)
                if op == "*": stack.append(stack.pop() * v)
                if op == "/": stack.append(int(stack.pop() / v))
        
            num, stack, sign = 0, [], "+"
            
            while tmp < len(s):
                if s[tmp].isdigit():
                    num = num * 10 + int(s[tmp])
                elif s[tmp] in "+-*/":
                    update(sign, num)
                    num, sign = 0, s[tmp]
                elif s[tmp] == "(":
                    num, j = calc(tmp + 1)
                    tmp = j - 1
                elif s[tmp] == ")":
                    update(sign, num)
                    return sum(stack), tmp + 1
                tmp += 1
            update(sign, num)
            return sum(stack)

        return calc(0)
