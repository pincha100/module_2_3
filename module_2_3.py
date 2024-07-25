my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
new = 0
while my_list[new] >= 0 and new < (len(my_list)-1):
    if my_list[new] > 0:
        print(my_list[new])
    new += 1
    if new == len(my_list):
        break