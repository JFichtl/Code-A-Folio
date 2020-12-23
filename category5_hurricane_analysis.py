# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

def convert_damages(damages):
  new_list = []
  cost = ""
  for item in damages:
    if item=="Damages not recorded":
      new_list.append("Damages not recorded")
    else:
      if item[-1]=="B":
        cost = float(item[0:-1])*1000000000
      elif item[-1]=="M":
        cost = float(item[0:-1])*1000000
      new_list.append(cost)
  return new_list    

damages = convert_damages(damages)

def construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths):
  hurricane_dictionary = {}
  for i in range(len(names)):
    hurricane_dictionary.update({ names[i] : {
    "Name" : names[i],
    "Months": months[i],
    "Years": years[i],
    "Max Sustained Winds": max_sustained_winds[i],
    "Areas Affected": areas_affected[i],
    "Damages" : damages[i],
    "Deaths": deaths[i] }
    })
  return hurricane_dictionary

hurricane_dictionary = construct_hurricane_dictionary(names, months, years, max_sustained_winds, areas_affected, damages, deaths)

# The following function groups together different hurricanes by year.

def get_hurricanes_in_year(year, hurricane_dict = hurricane_dictionary):
  hurricanes_in_year = []
  for key,value in hurricane_dict.items():
    if year==value.get("Years"):
      hurricanes_in_year.append(hurricane_dict.get(key))
  return hurricanes_in_year

# For the sake of simplicity we can just loop through the year list
# while applying the get_hurricanes_in_year function.

def get_hurricane_by_year_dictionary(hurricane_dict = hurricane_dictionary):
  year_in_hurricanes = {}
  for year in years:
    year_in_hurricanes.update({year : get_hurricanes_in_year(year, hurricane_dict)})
  return year_in_hurricanes

def get_hurricanes_in_date(date, year_or_month, hurricane_dict = hurricane_dictionary):
  hurricanes_in_date = []
  for key,value in hurricane_dict.items():
    if date==value.get(year_or_month):
      hurricanes_in_date.append(hurricane_dict.get(key))
  return hurricanes_in_date

# For the sake of simplicity we can just loop through the year list
# while applying the get_hurricanes_in_year function.

def get_hurricane_by_date_dictionary(date, hurricane_dict = hurricane_dictionary):
  date_in_hurricanes = {}
  if date == "Years":
    for year in years:
      date_in_hurricanes.update({year : get_hurricanes_in_date(year, "Years", hurricane_dict)})
  if date == "Months":
    for month in months:
      date_in_hurricanes.update({month : get_hurricanes_in_date(month, "Months", hurricane_dict)})
  return date_in_hurricanes


# We'll define a unique area list first

def unique_affected_areas_list(hurricane_dict):
  unique_affected_areas = []
  for areas in areas_affected:
    for area in areas:
      if not (area in unique_affected_areas):
        unique_affected_areas.append(area)
  return unique_affected_areas

# Now we define our counter function. This can be tested against the
# find (CTRL+F) function in the text editor.

def affected_area_counter(location, hurricane_dict):
  count = 0;
  for areas in areas_affected:
    for area in areas:
      if location == area:
        count += 1
  return count

def data_type_counter(data_point, data_type, hurricane_dict = hurricane_dictionary):
  count = 0;
  for name, attributes in hurricane_dict.items():
    if data_point == attributes.get(data_type):
      count += 1
  return count


# Now we can create a dictionary of unique affected areas against
# times affected.

def get_times_affected_dictionary(hurricane_dict = hurricane_dictionary):
  unique_areas = unique_affected_areas_list(hurricane_dict)
  times_affected_dict = {}
  for area in unique_areas:
    times_affected_dict.update({ area : affected_area_counter(area, hurricane_dict)})
  return times_affected_dict

def get_data_frequency_dictionary(data_type, data_list, hurricane_dict = hurricane_dictionary):
  unique_areas = unique_affected_areas_list(hurricane_dict)
  data_frequency_dict = {}
  for data in data_list:
    data_frequency_dict.update({ data : data_type_counter(data, data_type, hurricane_dict)})
  return data_frequency_dict


#years_in_hurricanes = get_data_frequency_dictionary("Years", years, hurricane_dictionary)
#print(years_in_hurricanes)

# We can write a "super" function that takes the data type we're interested
# in and either returns a list of hurricanes by that value or the
# uppermost value of that 

def analyze(value, return_type, hurricane_dict = hurricane_dictionary):
  def unique_value_counter(hurricane, hurricane_dict):
    count = 0;
    unique_areas = unique_affected_areas_list(hurricane_dict)
    for name, attributes in hurricane_dict.items():
      if name == hurricane and not(attributes.get(value)=="Damages not recorded"):
        count += attributes.get(value)
    return count
    
  def categorize_by_value(hurricane_dict):
    unique_areas = unique_affected_areas_list(hurricane_dict)
    value_by_area = {}
    for name in names:
      value_by_area.update({ name : unique_value_counter(name, hurricane_dict) } )
    return value_by_area

  def most_affected(hurricane_dict):
    areas_by_freq = get_times_affected_dictionary(hurricane_dict)
    count = 0
    area = ""
    for hurricane, frequency in areas_by_freq.items():
      if frequency > count:
        count = frequency
        area = hurricane
    return {area: count}

  def uppermost(hurricane_dict):
    count = 0
    name = ""
    for hurricane, attributes in hurricane_dict.items():
      if attributes.get(value)=="Damages not recorded":
        print("WARNING: Damages not recorded for " + hurricane + " hurricane.")
      elif value == "Years":
        hurricane_dates = get_data_frequency_dictionary("Years", years)
        for year, frequency in hurricane_dates.items():
          if frequency > count:
            count = frequency
            name = year
      elif value == "Months":
        hurricane_dates = get_data_frequency_dictionary("Months", months)
        for month, frequency in hurricane_dates.items():
          if frequency > count:
            count = frequency
            name = month
      elif not(value == "Years") and not(value == "Months") and attributes.get(value) > count:
        count = attributes.get(value)
        name = hurricane
    return {name: count}

  if value == "Frequency" and return_type.lower() == "uppermost":
    return most_affected(hurricane_dict)
  elif return_type.lower() == "uppermost":
    return uppermost(hurricane_dict) 
  elif return_type.lower() == "list":
    return categorize_by_value(hurricane_dict)

deadliest_hurricane = analyze("Deaths", "Uppermost")
most_affected_area = analyze("Frequency", "uppermost")
costliest_hurricane = analyze("Damages", "uppermost")
categorize_by_max_sustained_winds = analyze("Max Sustained Winds", "uppermost")
year_in_hurricanes = analyze("Years", "uppermost")
month_in_hurricanes = analyze("Months", "uppermost")

print(deadliest_hurricane)
print(most_affected_area)
print(costliest_hurricane)
print(year_in_hurricanes)
print(month_in_hurricanes)
print(categorize_by_max_sustained_winds)
# We see that we get the expected values.


mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}

def get_hurricane_rating(scale, metric, hurricane_dict = hurricane_dictionary):
  hurricane_master_list = analyze(metric, "List")
  hurricanes_categorized = {}
  ratings = [ x for (x,y) in scale.items()]
  for name, data in hurricane_master_list.items():
    if scale.get(ratings[-1]) < data:
      hurricanes_categorized.update({ name : len(scale)-1 })
    else:
      for i in range(len(scale)-1):
        if scale.get(i) <= data and scale.get(i+1) > data and data < 10000:
          hurricanes_categorized.update({ name : i })
  return hurricanes_categorized

print(get_hurricane_rating(mortality_scale, "Deaths"))
print(get_hurricane_rating(damage_scale, "Damages"))


