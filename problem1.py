# Normal Version
# def insert_elements(arr , elements):
#      for items in elements:
#          arr.append(items)
#
# def pritnt_elements(arr):
#     for items in arr:
#         print(items)



#Optimized Version--

# def insert_elements(arr , elements):
#     arr.extend(elements)
#
# def pritnt_elements(arr):
#     print(*arr, sep="\n")

arr = []
insert_elements(arr, [10 ,20 , 30 , 40 , 50])
pritnt_elements(arr)