import operator

names = ["Mohamed", "Sara", "Xia", "Paul", "Valentina", "Jide", "Aaron", "Emily", "Nikita", "Paul"]
insurance_costs = [13262.0, 4816.0, 6839.0, 5054.0, 14724.0, 5360.0, 7640.0, 6072.0, 2750.0, 12064.0]

# Add your code here

names.append("Priscilla")
insurance_costs.append(8320.0)

# We need a way of saying to Python that we want
# to sort these medical records by cost. That is, we
# want to sort them by the second entry of each item
# on the list. This is what the itemgetter method is
# doing. We can do it without using the itemgetter 
# method by taking either zip(insurance_costs, names)
# or zip(names, insurance_cost) and sorting.

medical_records = list(zip(names, insurance_costs))
medical_records_by_cost = sorted(medical_records, key=operator.itemgetter(1) )
medical_records_by_name = sorted(medical_records, key=operator.itemgetter(0) )

print("\nThese are the medical records sorted by insurance cost:\n\n", medical_records_by_cost)

num_medical_records = len(medical_records)
print("\nThere are", num_medical_records, "medical records")

first_medical_record = medical_records[0]
print("\nHere's the first medical record:", first_medical_record)

cheapest_three = medical_records[:3]
print("\nHere are the three cheapest insurance costs in our medical records:\n\n", cheapest_three)

priciest_three = medical_records[-3:]
print("\nHere are the three priciest insurance costs in our medical records:\n\n", priciest_three)

ocurrences_paul = names.count("Paul")
print("\nThere are", ocurrences_paul, "individuals with the name Paul in our medical records")

def middle_n(lst,n):
  new_list=lst
  length = len(lst)
  if n > length:
    return lst
  else:
    pop_size=n-1
    for i in range(0,pop_size):
      new_list.pop(i)
      new_list.pop(-i)
    return new_list

middle_five = middle_n(medical_records_by_cost, 3)
print(middle_five)

