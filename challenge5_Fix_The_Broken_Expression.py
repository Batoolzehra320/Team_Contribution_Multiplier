from collections import deque
def is_valid(s):
    balance = 0
    for ch in s:
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
            if balance < 0:
                return False
    return balance == 0
def removeInvalidParentheses(expr):
    visited = set()
    queue = deque([expr])
    visited.add(expr)
    result = []
    found = False
    while queue:
        s = queue.popleft()
        if is_valid(s):
            result.append(s)
            found = True
        if found:
            continue
        for i in range(len(s)):
            if s[i] not in "()":
                continue
            next_s = s[:i] + s[i+1:]
            if next_s not in visited:
                visited.add(next_s)
                queue.append(next_s)
    return result
print(removeInvalidParentheses("(q))"))