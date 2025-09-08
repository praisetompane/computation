from bubble_sort.uses_cases.arbitary_key_sort import sort

database = [
    {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
    {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
    {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
]


def test_sort_by_transaction_amount():

    assert sort(database, key="transaction_amount") == [
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    ]


def test_sort_by_name():

    assert sort(database, key="name") == [
        {"name": "aamir", "transaction_amount": 800, "device": "iphone-8"},
        {"name": "dhaval", "transaction_amount": 400, "device": "google pixel"},
        {"name": "kathy", "transaction_amount": 200, "device": "vivo"},
        {"name": "mona", "transaction_amount": 1000, "device": "iphone-10"},
    ]
