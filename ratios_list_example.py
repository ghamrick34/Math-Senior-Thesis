example_list = [3,5,7,9]

ratios = []
for index in range(len(example_list)-1):
    ratios.append(example_list[index+1]/example_list[index])
    
print(ratios)
