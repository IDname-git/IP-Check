import requests
input_prompt = '>>> '
print("      ::::::::::: :::::::::          ::::::::  :::    ::: :::::::::: ::::::::  :::    ::: ")
print("         :+:     :+:    :+:        :+:    :+: :+:    :+: :+:       :+:    :+: :+:   :+:   ")
print("        +:+     +:+    +:+        +:+        +:+    +:+ +:+       +:+        +:+  +:+     ")
print("       +#+     +#++:++#+         +#+        +#++:++#++ +#++:++#  +#+        +#++:++       ")
print("      +#+     +#+               +#+        +#+    +#+ +#+       +#+        +#+  +#+       ")
print("     #+#     #+#               #+#    #+# #+#    #+# #+#       #+#    #+# #+#   #+#       ")
print("########### ###                ########  ###    ### ########## ########  ###    ###       ")
print("")
print("Made by IDname")
print("Enter IPv4 or IPv6 address:")
ip_address = input(input_prompt)

api_url = 'https://ipleak.net/json/' + ip_address
response = requests.get(api_url)

print("Information about " + ip_address + ":")

if response.status_code == 200:
    data = response.json()

    def safe_print(label, value):
        print(f"{label}:  {value if value is not None and value != '' else'Not available'}")

    safe_print("ISP Name", data.get("isp_name"))
    safe_print("Country", data.get("country_name"))
    safe_print("Region", data.get("region_name"))
    safe_print("City", data.get("city_name"))
    safe_print("Latitude", data.get("latitude"))
    safe_print("Longitude", data.get("longitude"))
    safe_print("Accuracy Radius", data.get("accuracy_radius"))
    safe_print("Timezone", data.get("time_zone"))
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)

save_to_file = input("Do you want to save the information to a file? (y/n): ")
if save_to_file == 'y':
    with open('ip_info' + ip_address + '.txt', 'w') as file:
        file.write(f"Information about {ip_address}:\n")
        file.write(f"ISP Name: {data.get('isp_name')}\n")
        file.write(f"Country: {data.get('country_name')}\n")
        file.write(f"Region: {data.get('region_name')}\n")
        file.write(f"City: {data.get('city_name')}\n")
        file.write(f"Latitude: {data.get('latitude')}\n")
        file.write(f"Longitude: {data.get('longitude')}\n")
        file.write(f"Accuracy Radius: {data.get('accuracy_radius')}\n")
        file.write(f"Timezone: {data.get('time_zone')}\n")
        file.write("Ip checked with https://github.com/IDname-git/IP-Check")
    print(f"Information saved to ip_info{ip_address}.txt")
else:
    print("Information not saved to file.")

print('Press any key to exit...')
input("3")
input("2")
input("1")
