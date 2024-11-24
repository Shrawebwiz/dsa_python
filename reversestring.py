class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def reverse_string(my_string):
    reversed_string = ""  # Initialize as an empty string
    my_stack = Stack()

    for char in my_string:
        my_stack.push(char)

    while not my_stack.is_empty():
        reversed_string += my_stack.pop()

    return reversed_string

# Example usage
input_string = "hello"
print(reverse_string(input_string))  # Output should be "olleh"
