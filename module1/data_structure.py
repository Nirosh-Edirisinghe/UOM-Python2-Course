# add and remove data in stack
my_stack = []

def push(stack, value):
  stack.append(value)

def pop(stack):
  stack.pop()

push(my_stack,"10")
push(my_stack,"20")
push(my_stack,"30")
push(my_stack,"40")

pop(my_stack)
pop(my_stack)


print(my_stack)


# add delete item in queue
my_queue = []

def enqueue(queue, value):
  queue.append(value)

def dequeue(queue):
  queue.pop(0)

enqueue(my_queue,"10")
enqueue(my_queue,"20")
enqueue(my_queue,"30")

dequeue(my_queue)

print(my_queue)