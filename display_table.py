import pandas as pd

data = [
    {
        "cloud_print_id": "123",
        "order_id": "456",
        "is_pos_order": True,
        "restaurant_code": "ABC123",
        "delivery": "No",
        "pickup": "Yes",
        "dinein": "No",
        "orderstatus": "Completed"
    },
    {
        "cloud_print_id": "789",
        "order_id": "101",
        "is_pos_order": False,
        "restaurant_code": "XYZ789",
        "delivery": "Yes",
        "pickup": "No",
        "dinein": "",
        "orderstatus": ""
    }
]

df = pd.DataFrame(data, columns=[
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