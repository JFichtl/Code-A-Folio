names = ["Judith", "Abel", "Tyson", "Martha", "Beverley", "David", "Anabel"]
estimated_insurance_costs = [1000.0, 2000.0, 3000.0, 4000.0, 5000.0, 6000.0, 7000.0]
actual_insurance_costs = [1100.0, 2200.0, 3300.0, 4400.0, 5500.0, 6600.0, 7700.0]

# Add your code here

total_cost = 0

for cost in actual_insurance_costs:
  total_cost += cost

average_cost = total_cost/len(actual_insurance_costs)
print("Average Insurance Cost: " + str(average_cost) + " dollars.")

median = []
data_size = len(actual_insurance_costs)
half_point = int((data_size)*0.5)

if (data_size%2==0):
  median = (actual_insurance_costs[half_point]+actual_insurance_costs[half_point+1])*0.5
elif (data_size%2==1):
  median = actual_insurance_costs[half_point]

print("Median Insurance Cost: " + str(median) + " dollars.\n")

for i in range(len(names)):
  name = names[i]
  insurance_cost = actual_insurance_costs[i]
  cost_difference = abs(insurance_cost - average_cost)
  print("The insurance cost for " + name + " is " + str(insurance_cost))
  if insurance_cost > average_cost:
    print("The insurance cost for " + name + " is " + str(cost_difference) + " dollars above average.\n")
  elif insurance_cost == average_cost:
    print("The insurance cost for " + name + " is equal to the average.\n")
  elif insurance_cost < average_cost:
    print("The insurance cost for " + name + " is " + str(cost_difference) + " dollars below average.\n")

updated_insurance_costs = [x*11/10 for x in estimated_insurance_costs]


