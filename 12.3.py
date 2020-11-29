import urllib.request
 
count = 0
#user enters the url 
get_url = input("Enter a url to fetch data: ")
   
# Error handling for improperly formatted or non-existent URL.
try:
    opened_url = urllib.request.urlopen(get_url)
        
except HTTPError as e:
    print('The server couldn\'t fulfill the request.')
    print('Error code: ', e.code)
except URLError as e:
    print('We failed to reach a server.')
    print('Reason: ', e.reason)
    
# status code of the request
print ("Result code of the website: " + str(opened_url.getcode()))

# read the data from the URL and print it
for i in range(7):
    if i < 5: #will read 2560 characters in 5 iterations
        print(opened_url.read(512))
        count += 512
    elif i > 5 and i <= 6: #will read the remaining characters in this block
        print(opened_url.read(440)[:441])
        count += 440
        print("characters read till now ", count)
         
print("Total character on the site is ", count + len(str(opened_url.read()))) 