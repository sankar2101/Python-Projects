import requests
import pandas as pd

url="https://potlam-dev.azurewebsites.net/apicall/Cloud_print_list.php"

payload = {
    "public_key": "d3b429c5e6b68400446efd72deae46de"
}

try:
    response = requests.post(url, json=payload, timeout=30)
    response.raise_for_status()

    if response.status_code == 200:
        data = response.json()

        if 'orders' in data and data['orders']:
            orders = data['orders']

            df = pd.DataFrame(orders, columns=[
                "cloud_print_id",
                "order_id",
                "is_pos_order",
                "restaurant_code",
                "delivery",
                "pickup",
                "dinein",
                "orderstatus"
            ])

            print(df.to_string(index=False))
        else:
            print("No orders currently available in the system.")
    else:
        print(f"Failed to retreive data. Status code: {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
except requests.exceptions.Timeout:
    print("The request timed out.")
except requests.execptions.HTTPError as e:
    print(f"HTTP error occured: {e}")
except Exception as e:
    print(f"An error occurred: {e}")