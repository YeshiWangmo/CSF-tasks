def find_common_elements(list1, list2):
   # Convert the lists to sets
   set1 = set(list1)
   set2 = set(list2)

   # Find the intersection of the two sets
   common_elements = set1.intersection(set2)

   # Convert the result back to a list
   return list(common_elements)
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

common = find_common_elements(list1, list2)
print(common) # Output: [4, 5]
