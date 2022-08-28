my_list = [('a', 'one'), ('b', 'two'), ('c', 'three')]

# 👇️ using nested for loop

for tup in my_list:
    for item in tup:
        print(item)


print('---------------------------')

# 👇️ iterate over list of tuples with index

for index, tup in enumerate(my_list):
    print(index)
    print(tup[0])
    print(tup[1])


print('---------------------------')

# 👇️ iterate over list of tuples with unpacking

for first, second in my_list:
    print(first, second)
