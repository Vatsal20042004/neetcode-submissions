class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        op=['+','-','*','/']
        for i in tokens:
            if i not in op:
                stack.append(i)
            else:
                b=int(stack.pop())
                a=int(stack.pop())
                
                match i:
                    case '+': res=a+b
                    case '-': res = a-b
                    case '*': res=a*b
                    case '/': res=int(a/b)

                stack.append(res)

            
        return int(stack[0])
        