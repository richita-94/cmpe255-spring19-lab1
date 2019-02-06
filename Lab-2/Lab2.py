def mean_num_friends(x):
    sum = 0
    for i in x:
        sum = sum + i
    mean = sum/len(x)
    return mean
    
def median_num_friends(x):
    x.sort() 
    l=len(x)

    if (l%2 == 1):
        median = x[l//2]
        
    else:
        median = sum(x[l//2-1:l//2+1])/2.0
    return median

num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]
print("mean={}".format(mean_num_friends(num_friends)))
print("median={}".format(median_num_friends(num_friends)))