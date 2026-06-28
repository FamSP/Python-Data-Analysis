
# # ------- syntax for loop --------------
# integers = [1,2,3,4,5]
# for i in integers:
#     print(i)

# for i in integers:
#     print('yep!')


# # ------- loop through dictionary --------------
# ice_cream_dict = {'name': 'sappawat padtong', 'weekly intake' : 5, 'favorite ice cream': ['MCC','Chocolate']}

# for cream in ice_cream_dict.values():
#     print(cream)

# # when loop item you can discribe it in 2 variable,
# # first one will key and second will be values 

# for x,y in ice_cream_dict.items():
#     print(x)

# -------Nested for loop--------------
flavors = ['Vanilla', 'Chocalate', 'Cookie Dough']
topping = ['Hot Fudge' , 'Oreos' , 'Marshmello']

for one in flavors:
    for two in topping:
        print(one, 'topping' , two)