#Exo 1:

my_list = [1.0, 2.0, 3.0, 4.0, 5.0, 1.0]
def get_max_under(my_list, value):
    if value < 0:
        raise ValueError("votre liste doit avoir une valeur positif !")
    my_list.sort(reverse=True)
    for i in my_list:
        if i in value:
            return i
        

print(get_max_under(my_list, 3.1))
    
    
    
    
    
    
    
    
    
    