def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    for i in served_orders:
        
        if len(take_out_orders) > 0 and i == take_out_orders[0] :
            take_out_orders.pop(0)
        
        elif len(dine_in_orders) > 0 and i == dine_in_orders[0] :
            dine_in_orders.pop(0)
        
        else:
            return False
    
    if len(take_out_orders) == 0 and len(dine_in_orders) == 0:
        return True
    return False

print(is_first_come_first_served([1, 9], [7, 8], [1, 7, 8]))