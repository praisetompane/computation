from bubble_sort.uses_cases.arbitary_key_sort import sort as keyed_bubble_sort
from selection_sort.uses_cases.arbitary_key_sort import sort as keyed_selection_sort

database = {
    "transactions": [
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
    ],
    "clients": [
        {"First Name": "Raj", "Last Name": "Nayyar"},
        {"First Name": "Suraj", "Last Name": "Sharma"},
        {"First Name": "Karan", "Last Name": "Kumar"},
        {"First Name": "Jade", "Last Name": "Canary"},
        {"First Name": "Raj", "Last Name": "Thakur"},
        {"First Name": "Raj", "Last Name": "Sharma"},
        {"First Name": "Kiran", "Last Name": "Kamla"},
        {"First Name": "Armaan", "Last Name": "Kumar"},
        {"First Name": "Jaya", "Last Name": "Sharma"},
        {"First Name": "Ingrid", "Last Name": "Galore"},
        {"First Name": "Jaya", "Last Name": "Seth"},
        {"First Name": "Armaan", "Last Name": "Dadra"},
        {"First Name": "Ingrid", "Last Name": "Maverick"},
        {"First Name": "Aahana", "Last Name": "Arora"},
    ],
}


def test_sort_by_transaction_amount():

    assert keyed_bubble_sort(database["transactions"], key="transaction_amount") == [
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    ]


def test_sort_by_name():

    assert keyed_bubble_sort(database["transactions"], key="name") == [
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    ]


def test_sort_by_name_then_last_name():
    assert keyed_selection_sort(database["clients"], ["First Name", "Last Name"]) == [
        {"First Name": "Aahana", "Last Name": "Arora"},
        {"First Name": "Armaan", "Last Name": "Dadra"},
        {"First Name": "Armaan", "Last Name": "Kumar"},
        {"First Name": "Ingrid", "Last Name": "Galore"},
        {"First Name": "Ingrid", "Last Name": "Maverick"},
        {"First Name": "Jade", "Last Name": "Canary"},
        {"First Name": "Jaya", "Last Name": "Seth"},
        {"First Name": "Jaya", "Last Name": "Sharma"},
        {"First Name": "Karan", "Last Name": "Kumar"},
        {"First Name": "Kiran", "Last Name": "Kamla"},
        {"First Name": "Raj", "Last Name": "Nayyar"},
        {"First Name": "Raj", "Last Name": "Sharma"},
        {"First Name": "Raj", "Last Name": "Thakur"},
        {"First Name": "Suraj", "Last Name": "Sharma"},
    ]
