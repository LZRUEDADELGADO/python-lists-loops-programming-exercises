parking_state = [
    [1, 1, 1],
    [0, 0, 0],
    [1, 1, 2]
]

def get_parking_lot(parking_lot):
    
    total_slots = 0
    available_slots = 0
    occupied_slots = 0

    
    for row in parking_lot:
        for slot in row:
            if slot != 0: 
                total_slots += 1
                if slot == 1:  
                    occupied_slots += 1
                elif slot == 2:  
                    available_slots += 1

   
    return {
        "total_slots": total_slots,
        "available_slots": available_slots,
        "occupied_slots": occupied_slots
    }


state = get_parking_lot(parking_state)
print(state)

