def rgb(r, g, b):
    
    my_list = ['00' if x < 0 else 'FF' if x > 255 else hex(x).split('x')[-1].upper() for x in (r,g,b)]
    
    my_list = [f'0{x}' if len(x) < 2 else x for x in my_list]
    
    return ''.join(my_list)
