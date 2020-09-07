def most_frequent(List): 
    if List == int:
        raise TypeError

    return max(set(List), key = List.count) 
  
List = [1,2,3,4,5,6,6,8,8,6,9]
List2 = [87.5, 88.5, 60.5, 90.5, 88.5]
print(most_frequent(List)) 
print(most_frequent(List2)) 
