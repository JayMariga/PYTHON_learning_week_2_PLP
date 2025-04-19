my_list = [10, 20, 30, 40,]   #Appending elements to my_list

my_list.insert (1, 15)  #Inserting 15 at index 1
print(my_list)  #Output: [10, 15, 20, 30, 40]

my_list_2 = [50, 60, 70]  #Creating another list so as to extend it to my_list
my_list.extend(my_list_2)  #Extending my_list with my_list_2
print(my_list)  #Output: [10, 15, 20, 30, 40, 50, 60, 70]

my_list.remove(70)  #Removing last element from my_list
print(my_list)  #Output: [10, 15, 20, 30, 40, 50, 60]

my_list.sort() #Sorting my_list in ascending order
print(my_list)  #Output: [10, 15, 20, 30, 40, 50, 60]

#my_list.reverse()  #Reversing my_list
#print(my_list)  #Output: [60, 50, 40, 30, 20, 15, 10]

#my_list.sort(reverse=True)  #Sorting my_list in descending order
#print(my_list)  #Output: [60, 50, 40, 30, 20, 15, 10]

print(my_list[3])  #printing value of 30 after it has been sorted in ascending order 
#Output: 30




