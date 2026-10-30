# Demo 1
# 1)	
# The Code
customer = "karachi crafts"
price = 2400
orders = 3
delivery_cost = 350
order_total = orders *price + delivery_cost
print(f"Dear {customer} your total cost for {orders} orders is {order_total}")
print(f"The data type of the total cost is {type(order_total)}")

# 2)
# The Code:	
order_subtotal =7200
sales_tax = 0.18
tax_amount  =  order_subtotal *sales_tax
total_amount_after_tax =order_subtotal + tax_amount
print(f"The tax amount is {tax_amount} and the total amount after tax is {total_amount_after_tax}")
print(f"The data type of Tax amount is {type(tax_amount)}")

# The data type is float because the tax amount is in float form and python converts the other values to float and then performs the operation so is the with the results.
# 3)	 
# The Code:
total_bill =7200
total_friends = 4
one_person_share = total_bill  / total_friends 
whole_amt_for_one = total_bill  // total_friends
remaining_amt = total_bill  % total_friends
print(f"Amount each one need to pay is { one_person_share }" )
print(f"The whole amount each one need to pay is { whole_amt_for_one }" )
print(f"The remaining amount  is { remaining_amt }" )


# 4)	
# The Code:
phone_cost = 15000
discount_amt = 0.10* phone_cost
amt_after_discount = phone_cost-discount_amt
tax = 0.18 *amt_after_discount
final_amt =amt_after_discount + tax
print (f"The final price {final_amt}")

# The Other Way:
phone_cost = 15000
tax = 0.18 * 15000
after_tax = phone_cost +tax
discount = after_tax * 0.10
final_amt =after_tax - discount
print (f"The final price {final_amt}")


# 5)	
# The Code:

items = 23
full_boxes = items//6
remaining_items =  items - (full_boxes *6)
if remaining_items>0:
 total_boxes = full_boxes + 1
else:
 total_boxes = full_boxes

shipment_cost =total_boxes * 120

print("Full boxes:",full_boxes)
print("left items:",remaining_items)
print("Total Boxes:", total_boxes)
print("Shipment Cost",shipment_cost)




