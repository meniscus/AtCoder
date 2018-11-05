read_line = input().split()

a_to_b_fare = int(read_line[0])
b_to_c_fare = int(read_line[1])
discounted = b_to_c_fare / 2

total_fare = int(a_to_b_fare + discounted)

print(total_fare)



