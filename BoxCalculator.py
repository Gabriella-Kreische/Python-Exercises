#User will insert the number of itens and python will calculate how many boxes will be necessary
#Each box will need to be full, Big box can have 5 items, medium box can have 3 items and small box can have 1 item.
Big_box = 5
Med_box = 3
Small_box = 1
No_items = int(input("Please enter the number of items (more or equal to 5) you would like to pack: "))
if (No_items >= Big_box):
    No_Big_boxes = No_items // Big_box
    No_remainderbb = No_items % Big_box
    total_boxes = No_Big_boxes
    print("The number of big boxes you will need is " + str(No_Big_boxes))
    if (No_remainderbb >= Med_box):
        No_Med_boxes = No_remainderbb // Med_box
        No_remainder_mb = No_remainderbb % Med_box
        total_boxes = No_Med_boxes + No_Big_boxes
        print("The number of medium boxes you will need is " + str(No_Med_boxes))
        if (No_remainder_mb >= Small_box):
            No_small_boxes_2 = No_remainder_mb // Small_box
            total_boxes = No_Med_boxes + No_Big_boxes + No_small_boxes_2
            print("The number of small boxes you will need is " + str(No_small_boxes_2))
    elif (No_remainderbb >= Small_box):
        No_small_boxes_1 = No_remainderbb // Small_box
        total_boxes = No_Big_boxes + No_small_boxes_1
        print("The number of small boxes you will need is " + str(No_small_boxes_1))
print("The total number of boxes you will use is " + str(total_boxes))