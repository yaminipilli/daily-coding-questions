 '''Given a list of numbers and a number k,return whether any two numbera from the list add upto k.
 for example [10,15,3,7] and k of 17,retrun true since (10+7) is 17.
 
 solution:'''
 
 arr= [10, 15, 3, 7]
k = 17

arr_len = len(arr)

def compute(arr_list, k):
    
    for i in range(arr_len):

        arr_list_len = len(arr_list)
        base_num = arr_list[0]
        sum_num= 0
        arr_list.pop(0)

        arr_list_len = len(arr_list)

        for j in range(arr_list_len):
            sum_num = base_num + arr_list[j]

            if sum_num == k:
                return True
    
    return False

r = compute(arr, k)

if not r:
    print("false")
else:
    print("True")

