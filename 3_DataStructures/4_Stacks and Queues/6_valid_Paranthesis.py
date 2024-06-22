from collections import deque


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = deque()
    for i in s:
        if i in ("(", "[", "{"):
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                if (
                    ((i == ")" and stack.pop() != "("))
                    or ((i == "]" and stack.pop() != "["))
                    or ((i == "}" and stack.pop() != "{"))
                ):
                    return False

    # if no paranthesis found after matching all, return True else False
    return not stack


print(isValid("()[]{}"))
print(isValid("()[]{]"))
print(isValid("()[]{}{"))
