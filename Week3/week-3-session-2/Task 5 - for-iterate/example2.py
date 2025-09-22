
rivers = {
  "London": "Thames", 
  "Leeds": "Aire", 
  "Liverpool": "Mersey",
  "York": "Ouse"
}

# loop through the dict extracting key and value

for c,r in rivers.items():
    print( c,r )
    
# create 2 further for loops to iterate: 1. just through the keys, 2. just through the values
for c in rivers:
    print(c)

for c,r in rivers.items():
    print(r)
# hint: we looked at built in function for dicts last session