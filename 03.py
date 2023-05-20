# Ask the user for a number and return a list that contains only elements
# from the original list a that are smaller than that number given by the user.

original_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
n = int(input())


# Solutions

generator_solution = list(x for x in original_list if x < n)
filter_solution = filter(lambda x: x < n, original_list)

assert generator_solution == list(filter_solution)

print(list(generator_solution))
