import requests

input_prompt = '>>> '
print("      ::::::::::: :::::::::          ::::::::  :::    ::: :::::::::: ::::::::  :::    ::: ")
print("         :+:     :+:    :+:        :+:    :+: :+:    :+: :+:       :+:    :+: :+:   :+:   ")
print("        +:+     +:+    +:+        +:+        +:+    +:+ +:+       +:+        +:+  +:+     ")
print("       +#+     +#++:++#+         +#+        +#++:++#++ +#++:++#  +#+        +#++:++       ")
print("      +#+     +#+               +#+        +#+    +#+ +#+       +#+        +#+  +#+       ")
print("     #+#     #+#               #+#    #+# #+#    #+# #+#       #+#    #+# #+#   #+#       ")
print("########### ###                ########  ###    ### ########## ########  ###    ###       ")
print("\n\n")
print("Made by IDname")
print("Enter IPv4 or IPv6 address:")
ip_address = input(input_prompt)

api_url = 'https://ipleak.net/json/' + ip_address
response = requests.get(api_url)

print("\nInformation about " + ip_address + ":")

if response.status_code == 200:
    data = response.json()

    def safe_print(label, value):
        print(f"{label}: {value if value is not None and value != '' else 'Not available'}")

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

print('Press any key to exit...')
input("3")
input("2")
input("1")