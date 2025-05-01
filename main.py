import requests
import sys


input_prompt = '>>> '
print("      ::::::::::: :::::::::          ::::::::  :::    ::: :::::::::: ::::::::  :::    ::: ")
print("         :+:     :+:    :+:        :+:    :+: :+:    :+: :+:       :+:    :+: :+:   :+:   ")
print("        +:+     +:+    +:+        +:+        +:+    +:+ +:+       +:+        +:+  +:+     ")
print("       +#+     +#++:++#+         +#+        +#++:++#++ +#++:++#  +#+        +#++:++       ")
print("      +#+     +#+               +#+        +#+    +#+ +#+       +#+        +#+  +#+       ")
print("     #+#     #+#               #+#    #+# #+#    #+# #+#       #+#    #+# #+#   #+#       ")
print("########### ###                ########  ###    ### ########## ########  ###    ###       ")
print("Made by IDname")

if len(sys.argv) < 2:
    print("Usage: py main.py <ip_address>")
    print("Example: py main.py 1.1.1.1")
    sys.exit(1)
ip_address = sys.argv[1] if len(sys.argv) > 1 else input(input_prompt).strip()

api_url = 'https://ipleak.net/json/' + ip_address
api_url2 = 'https://reallyfreegeoip.org/json/' + ip_address
api_url3 = 'https://ipwho.is/' + ip_address
response = requests.get(api_url)
if response.status_code == 200:
    data = response.json()
else:
    print("Request failed with status code:", response.status_code)
    print("Response:", response.text)
    data = {}

response2 = requests.get(api_url2)
if response2.status_code == 200:
    data2 = response2.json()
else:
    print("Request failed with status code:", response2.status_code)
    print("Response:", response2.text)
    data2 = {}

response3 = requests.get(api_url3)
if response3.status_code == 200:
    data3 = response3.json()
else:
    print("Request failed with status code:", response3.status_code)
    print("Response:", response3.text)
    data3 = {}

def safe_format(*values):
    return " | ".join([str(value if value is not None and value != '' else 'Not available') for value in values])

print("Information about " + ip_address + ":")
print(f"ISP Name: {safe_format(data.get('isp_name'), data2.get('isp_name'), data3.get('connection', {}).get('isp'))}")
print(f"Country: {safe_format(data.get('country_name'), data2.get('country_name'), data3.get('country'))}")
print(f"Region: {safe_format(data.get('region_name'), data2.get('region_name'), data3.get('region'))}")
print(f"City: {safe_format(data.get('city_name'), data2.get('city'), data3.get('city'))}")
print(f"Zip: {safe_format(data.get('zip_code'), data2.get('zip_code'), data3.get('postal'))}")
print(f"Latitude: {safe_format(data.get('latitude'), data2.get('latitude'), data3.get('latitude'))}")
print(f"Longitude: {safe_format(data.get('longitude'), data2.get('longitude'), data3.get('longitude'))}")
print(f"Timezone: {safe_format(data.get('time_zone'), data2.get('time_zone'), data3.get('timezone', {}).get('id'))}")

print("Extra information:")
for label, value in [
    ("Accuracy Radius", data.get('accuracy_radius')),
    ("Metro Code", data2.get('metro_code')),
    ("Domain", data3.get('connection', {}).get('domain')),
    ("Organization", data3.get('connection', {}).get('org'))
]:
    print(f"{label}: {value if value is not None and value != '' else 'Not available'}")

save_to_file = input("Do you want to save the information to a file? (y/n): ")
if save_to_file == 'y':
    with open('ip_info' + ip_address + '.txt', 'w') as file:
        def safe_write_line(category, *values):
            file.write(f"{category}: " + " | ".join([str(value if value is not None and value != '' else 'Not available') for value in values]) + "\n")

        file.write(f"Information about {ip_address}:\n")
        safe_write_line("ISP Name", data.get('isp_name'), data2.get('isp_name'), data3.get('connection', {}).get('isp'))
        safe_write_line("Country", data.get('country_name'), data2.get('country_name'), data3.get('country'))
        safe_write_line("Region", data.get('region_name'), data2.get('region_name'), data3.get('region'))
        safe_write_line("City", data.get('city_name'), data2.get('city'), data3.get('city'))
        safe_write_line("Zip", data.get('zip_code'), data2.get('zip_code'), data3.get('postal'))
        safe_write_line("Latitude", data.get('latitude'), data2.get('latitude'), data3.get('latitude'))
        safe_write_line("Longitude", data.get('longitude'), data2.get('longitude'), data3.get('longitude'))
        safe_write_line("Timezone", data.get('time_zone'), data2.get('time_zone'), data3.get('timezone', {}).get('id'))

        file.write("Extra information:\n")
        for label, value in [
            ("Accuracy Radius", data.get('accuracy_radius')),
            ("Metro Code", data2.get('metro_code')),
            ("Domain", data3.get('connection', {}).get('domain')),
            ("Organization", data3.get('connection', {}).get('org'))
        ]:
            file.write(f"{label}: {value if value is not None and value != '' else 'Not available'}\n")
        file.write("File created with github.com/IDname-git/IP-Check\n")
        print(f"Information saved to ip_info{ip_address}.txt")

else:
        print("Information not saved to file.")

input('Press any key to exit...')
