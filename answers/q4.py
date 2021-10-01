
# what will the solution be? Does it even work?

old_dict = {1: 0}
new_dict = {1: 3, 4: 5}

new_dict.update(old_dict)

print(new_dict[1])  # 3 ?


# update is an inplace and returns None