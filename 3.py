my_file = open('shampoo_sales.csv', 'r')

value_list=[]

for line in my_file:

    my_list = line.split(",")

    if my_list[0]!="Date":
        value_list.append(float(my_list[1]))

print(sum(value_list))

my_file.close()