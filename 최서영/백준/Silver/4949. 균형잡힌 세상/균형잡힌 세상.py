while True:
    s = input()
    if s == ".":
        break
    
    stack = []
    balanced = True
    
    for ch in s :
        if ch == '(' or ch == '[':
            stack.append(ch)
            
        elif ch == ')':
            if not stack or stack[-1] != '(': # stack[-1] : 스택의 맨 위(가장 최근에 열린 괄호)
                balanced = False
                break
            stack.pop()
            
        elif ch == ']':
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()
            
    if balanced and not stack :
        print("yes")
    else :
        print("no")