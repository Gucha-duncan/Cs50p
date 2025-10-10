def main():
 students = {
    'Javy': 'Eldoret',
    'ManuBett': 'Kericho',
    'Alphonce': 'Siaya',
    'Mulu':'Ukambani',
}

 for student in students:
    print(f"{student} lives in {students[student]}")
    
    
 cities = [
    {'name': "Nairobi", 'country':'Kenya', 'continent': 'Africa'},
     {'name': "London", 'country':'England', 'continent': 'Europe'},
       {'name': "New York", 'country':'USA', 'continent': 'North America'},
         {'name': "Kampala", 'country':'Uganda', 'continent': 'Africa'},
           {'name': "Kisumu", 'country':'Kenya', 'continent': 'Africa'},
]

 for city in cities:
    print(f"{city['name']} is located in {city['country']}, {city['continent']}")
 
 spacecraft ={'name':'Voyager 1', 'distance':163}
 spacecraft.update({'founder':'Gucha'})
 print(create_report(spacecraft))
 
def create_report(spacecraft):
     
     return f"{spacecraft['name']} has covered {distance_converter(spacecraft['distance'])} miles today, founder is {spacecraft.get('founder', 'Unknown')}"

def distance_converter(distance):
    return distance * 1450707999    
 
main()
