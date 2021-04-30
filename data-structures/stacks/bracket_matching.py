def bracket_matching(s: str) -> bool:
    if s is None or s == '':
        return True

    memory = Stack()

    for i in range(0, len(s)):
        if s[i] == '(' or s[i] == '{' or s[i] == '[' :
            memory.push(s[i])
        if s[i] == ')':
            top_elem = memory.pop()
            if top_elem == '(':
                continue
            else:
                return False
        if s[i] == '}':
            top_elem = memory.pop()
            if top_elem == '{':
                continue
            else:
                return False
        if s[i] == ']':
            top_elem = memory.pop()
            if top_elem == '[':
                continue
            else:
                return False

    return True if memory.is_empty() else False


class Stack:
    def __init__(self, top=None):
        self.top = None
        self.data = None

    def push(self, data):
        data_node = DataNode(data)
        self.top = data_node
        if self.data is None:
            self.data = data_node
            return True
        else:
            data_node.next = self.data
            self.data = data_node
        return False

    def is_empty(self):
        return True if self.top is None else False

    def pop(self):
        if self.top is None:
            return None
        else:
            self.data = self.top.next
            ret_data = self.top.data
            self.top = self.top.next
            return ret_data

    def print(self):
        itr = self.data
        while itr is not None:
            print( str(itr.data) + "->", end="")
            itr = itr.next

class DataNode:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

stck = Stack()

stck.push(1)
stck.push(2)
stck.push(3)
stck.push(4)
stck.push(5)
stck.print()
print("\n")
stck.pop()
stck.pop()
stck.print()
print("\n")

print(bracket_matching("(])"))
