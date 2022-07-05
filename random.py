import random

num_value = 45

# ran_num = random.randrange(1, (num_value + 1))
# print(ran_num)

def random_things():
    random_value = random.randrange(1, (num_value + 1))
    return random_value
    
sub_num = 0
list_num = [0]
for value in range(6):
    
    ran_num = random_things()
    for list_value in list_num:
        if list_value == ran_num:
            ran_num = random_things()
        
    # if sub_num == ran_num:
    #     ran_num = random_things()
        
    print(ran_num)
    list_num.append(ran_num)