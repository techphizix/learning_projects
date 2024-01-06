weight = 41.5
cost_ground = 20
cost_drone = 0
#Ground shipping

if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20 
print("Ground Shipping: $",cost_ground)

#Ground shipping premium
premium_shipping_cost = 125
premium_shipping = cost_ground + premium_shipping_cost
print("Premium Shipping: $",premium_shipping)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.5 
elif weight <= 6:
  cost_drone = weight * 9 
elif weight <= 10:
  cost_drone = weight * 12 
else:
  cost_drone = weight * 14.25  
print("Drone Shipping: $",cost_drone)

cheapest = min(cost_ground, premium_shipping, cost_drone)
print("Cheapest Shipping: $",cheapest)
