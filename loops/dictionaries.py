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
 