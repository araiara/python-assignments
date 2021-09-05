import argparse

parser = argparse.ArgumentParser(description="Enter the integers after --number_list and number of rotations after --rotate_by")
parser.add_argument("--my_int_list", help="enter numbers to rotate", type=int, nargs='+')
parser.add_argument("--num_rotate", help="enter number of rotations to be made", type=int)

args = parser.parse_args()

def rotate_left(my_int_list, num_rotate):
    for i in range(num_rotate):
        rotate_value = my_int_list[0]
        my_int_list = my_int_list[1:len(my_int_list)]
        my_int_list.append(rotate_value)
    return my_int_list, num_rotate
    
rotated_array, num_rotate = rotate_left(args.my_int_list, args.num_rotate)

print("Number of left rotations: {}".format(num_rotate))
for i in rotated_array: 
    print(i, end=' ') 