medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

updated_medical_data = medical_data.replace("#", "")

def display_records(records):
  for record in medical_records_clean:
    print("{name} is {age} years old with a BMI of {bmi} and an insurance cost of ${insurance_cost}\n".format(name = record[0], age = record[1], bmi = record[2], insurance_cost = record[3]))

def data_organizer(data, separator1, separator2, data_type):
  num_records = 0
  for item in data.split(";"):
    num_records += 1
  print("There are {num_records} {data_type} records in the data".format(num_records = num_records, data_type = data_type))
  data_split = data.split(";")

  # Now we initialize a new list in which each entry is 
  # another list consisting of the medical data of a 
  # single person. The following loop will split each string
  # containing the name, age, etc... into a list that may
  # be accesed via indices. E.G. index 0 will return the name 
  # of the person.

  records=[]
  for entry in data_split:
    records.append(entry.split(","))

  # Now for the data cleanup process. We need to take each
  # string and strip it of unnecesary characters. We can 
  # fix this in another list. Essentially we need to
  # recreate the record making process but adding a cleanup
  # code to acces each item in each individual record.
  # instead of appending a split element, we will append a
  # stripped element. This marks the end of our data organizer
  # function.

  records_clean = []
  for record in records:
    record_clean = []
    for item in record:
      record_clean.append(item.strip())
    records_clean.append(record_clean)
  return records_clean

def data_cleanup(records, garbage):

  # This is a variation on the data cleanup function
  # in which we may specify the character that we want
  # to get rid of. For example, in "bagel!!!!!" we can
  # rid ourselves of the plethora exclamation points
  # by declaring garbage to be "!"

  records_clean = []
  for record in records:
    record_clean = []
    for item in record:
      record_clean.append(item.strip(garbage))
    records_clean.append(record_clean)
  return records_clean

def data_group_list(records):

  # This function will give us a list of every data 
  # type, if our raw data has names, costs, ages, etc...
  # this will return a master list that will contain lists
  # for every data type. i.d. it will contain a list of names,
  # a list of ages, etc...

  group_list = []
  record_size = len(records[0])
  for i in range(record_size):
    data_list = []
    for record in records:
      data_list.append(record[i])
    group_list.append(data_list)
  return group_list

def average_value(records):
  average = 0
  size = len(records)
  for record in records:
    cost = float(record)
    average += cost/size
  return average



# This begins the data cleanup process by splitting the
# string in the semicolons and giving us a list with 
# strings of data.


medical_records_clean = data_organizer(updated_medical_data, ";", ",", "medical")

medical_data_group = data_group_list(medical_records_clean)

names = medical_data_group[0]
ages = medical_data_group[1]
bmis = medical_data_group[2]
insurance_costs = medical_data_group[3]

average_bmi=average_value(bmis)
average_cost=average_value(insurance_costs)

print("The average BMI is {average_bmi}".format(average_bmi = average_bmi))
print("The average isurance cost is {average_cost}\n".format(average_cost = average_cost))

#display_records(medical_records_clean)




