list1=[6,3,5,7,9]
list2=[5,7,6,8,0]
def common_numbers(list1,list2):
	list3=[]
	for x in list1:
		for y in list2:
			if x==y:
				list3.append(x)
	return list3
print (common_numbers(list1,list2))








	 

