from chef import Chef

class ChineseChef(Chef):
    # def make_chicken(self):
    #     print("The chef makes a chicken")
    
    # def make_salad(self):
    #     print("The chef makes a salad")
    
    # def make_special_dish(self):
    #     print("The chef makes orange chicken")

    # So, instead of writing all of the above code, we can do one small thing, that is inherit 
    # We can write the top two lines of codes instead
    def make_special_dish(self):
        print("The chef makes orange chicken")
# since, the chef file also had make_special_dish function, so, if we would have run the file, make_special_dish function would have showed the result of the Chef class, so, we'll have to overwrite the same function to get the special dish of ChineseChef


    def make_fried_rice(self):
        print("The chef makes fried rice")