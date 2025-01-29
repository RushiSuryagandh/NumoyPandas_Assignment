list1='rushi,RUSHI  ,kskjdks,RUSHI,kdhsjkd '
for item in list1:
    store_user,store_list,_,_,_=list1.strip().split(',')
print(store_user,store_list)