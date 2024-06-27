class Restaurant:
    name = ""
    category = ""
    rating = 0.0
    delivery = False

#Bob's Burgers
bobs_burgers = Restaurant()

bobs_burgers.name = "Bob's Burgers"
bobs_burgers.category = "American Diner"
bobs_burgers.rating = 4.7
bobs_burgers.delivery = False

#Panera
panera = Restaurant()
panera.name = "Panera Bread"
panera.category = "Bakery and Sandwich Shop"
panera.rating = 4.2
panera.delivery = False

#Pizza Hut
pizza_hut = Restaurant()
pizza_hut.name = "Pizza Hut"
pizza_hut.category = "Pizza"
pizza_hut.rating = 2.4
pizza_hut.delivery = True

print(vars(pizza_hut))  
print(vars(panera))
print(vars(bobs_burgers))
