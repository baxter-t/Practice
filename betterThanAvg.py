'''
    Better than average

    Given an array of class points, and your points, determine if you are better than the average
'''

def better_than_average(class_points, your_points):
    return sum(class_points)/len(class_points) < your_points

print(better_than_average([1,2,3,4], 4))
