#3-4
invite_list = ["Me","You","Shema"]
print(invite_list[0] + " you invited")
print(invite_list[1] + " you invited")
print(invite_list[-1] + " you invited")
#3-5
print(invite_list)
fucker = invite_list.pop(1)
print("Oops " + fucker + " deleted")
invite_list.append("Devil")
print(invite_list[0] + " you invited")
print(invite_list[1] + " you invited")
print(invite_list[-1] + " you invited")
#3-6
print("Список гостей стал больше")
invite_list.insert(0,"New guest in start of list")
invite_list.insert(2,"New guest in middle of list")
invite_list.append("Last guest in the list")
print(invite_list[0] + " you invited")
print(invite_list[1] + " you invited")
print(invite_list[2] + " you invited")
print(invite_list[3] + " you invited")
print(invite_list[-1] + " you invited")
print(len(invite_list))
#3-7
print(invite_list)
print("Only 2 guests invited")
deleted_guest_1 = invite_list.pop(-1)
print(deleted_guest_1 + " you are not invited anymore")
deleted_guest_2 = invite_list.pop(-1)
print(deleted_guest_2 + " you are not invited anymore")
deleted_guest_3 = invite_list.pop(-1)
print(deleted_guest_3 + " you are not invited anymore")
deleted_guest_4 = invite_list.pop(-1)
print(deleted_guest_4 + " you are not invited anymore")
print(invite_list[0]+ " You are still invited \n"+ invite_list[1]+  " You are still invited")
print(len(invite_list))
del invite_list[1]
del invite_list[0]
print(invite_list)
print(len(invite_list))

