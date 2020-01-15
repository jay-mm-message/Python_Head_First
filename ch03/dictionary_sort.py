
found = {   'Name':'Ford Prefect',
            'Gander':'Male',
            'Occupation':'Researcher',
            'Home Planet':'Betelgeuse Seven'}

found['No'] = '001'

print('sort before')
for key in found:
    print('key: ', key, ', value: ', found[key])

print()
print('sort after')
for key in sorted(found):
    print('key: ', key, ', value: ', found[key])
