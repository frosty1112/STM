try:

    js_data= json.loads(data)

except :

    js_data= None

# Apply some condition for printing correct data

if not js_data or 'status' not in js_data or js_data['status'] != 'OK' : # here check json data status

    print ('===Not able to Retrieve try again===')   # if status not found positive then it will print if

print (data)   

continue

counter = -1 # counter variable starting value contain -1 that will be use in next steps

information = js_data[' results '][ 0 ][ 'address_components' ]

for i in information :

    counter = counter + 1   # here counter variable increasing by 1

if js_data[ ' results' ][ 0 ][ " address_components "][counter ]["types"]==['country','political']:

    print (js_data["results"][0][" address_components "][counter ]['country_code'] )   #this will print your country code name.

else:

    continue
