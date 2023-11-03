#A system to help speed up the prcoess of creating receipts for cutomers. 
#Lovely Loveseat Description.
lovely_loveseat_description = """Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or White."""

#Loveseat Price.
lovely_loveseat_price = 254.00

#Stylish Settee Description.
stylish_settee_description = """Stylish Settee. Leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."""

#Stylish Settee Price.
stylish_settee_price = 180.50

# Luxurious Lamp Description.
luxurious_lamp_description = """Luxurious Lamp. Glass and Iron. 36 inches Tall. Brown with Cream shade."""

#Luxurious Lamp Price.
luxurious_lamp_price = 52.15

#Calculate Sales Tax.
sales_tax = .088

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax

print("Customer One Items:")
print(customer_one_itemization)

print("Customer One Total:")
print(customer_one_total)
