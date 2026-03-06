# -----A02: Balanced Parentheses Checker-----

def is_balanced(s):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    s = input("Enter bracket string: ")
    if is_balanced(s):
        print("Balanced")
    else:
        print("Not Balanced")