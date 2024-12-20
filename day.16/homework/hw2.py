my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

even_index_elements = [my_list[i] for i in range(len(my_list)) if i % 2 == 0]
print("Elements at even indices:", even_index_elements)