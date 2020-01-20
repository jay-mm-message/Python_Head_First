import pprint

people = {}
people['Arthur'] = {    'Occupation: Sandwich-Maker',
                        'Gender: Male',
                        'Home Planet: Earth',
                        'Name: Arthur Dent' }
people['Ford'] = {  'Occupation: Researcher',
                    'Gender: Male',
                    'Home Planet: Betelguest Seven',
                    'Name: Ford Prefect' }
people['Robot'] = { 'Occupation: Paranoid Android',
                    'Gender: Unknown',
                    'Home Planet: Unknown',
                    'Name: Marvin' }
people['Trillian'] = {  'Occupation: Mathematician',
                        'Gender: Female',
                        'Home Planet: Earth',
                        'Name: Tricia McMillan' }

print('people: ', people)

pprint.pprint(people)
