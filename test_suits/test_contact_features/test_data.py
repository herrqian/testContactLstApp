TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NjJiYzVjNzc5MWNhMzAwMTMyN2MzYjAiLCJpYXQiOjE3MTg4MjMzNTl9.pwhgL7ITuKdjFn4qz8ZBeQyKKlKhX-esMYi2jWlxjLk"
COOKIE = {
    "name": "token",
    "value": TOKEN,
    "domain": "thinking-tester-contact-list.herokuapp.com",
    "path": "/",
}

invalid_test_contacts = [
    ({"lastname": "postman"}, "Path `firstName` is required"),
    ({"firstname": "tom"}, "Path `lastName` is required"),
    ({
         "firstname": "tim",
         "lastname": "miller",
         "birthdate": "01-01-2002"
     },
     "Birthdate is invalid intent"),  # the string " intent" lead to failed test
    (
        {
            "firstname": "tim",
            "lastname": "miller",
            "email": "fasdfadf"
        },
        "Email is invalid"
    ),
    (
        {
            "firstname": "tim",
            "lastname": "miller",
            "phone": "123a"
        },
        "Phone number is invalid"
    ),
    (
        {
            "firstname": "tim",
            "lastname": "miller",
            "post": "!!!!"
        },
        "Postal code is invalid"
    ),
]

valid_test_contacts = [
    {
        "firstname": "abc",
        "lastname": "efd",
        "birthdate": "2000-01-01",
        "email": "qwe@ewq.de",
        "phone": "3211231230",
        "streetOne": "Addresse Eins",
        "streetTwo": "Addresse Zwei",
        "city": "New York",
        "stateProvince": "New York",
        "post": "312334",
        "country": "USA",
    },
    {
        "firstname": "jan",
        "lastname": "have",
        "birthdate": "2009-01-01",
        "email": "qwe12@ewq.de",
        "phone": "32112311230",
        "streetOne": "di zhi yi",
        "streetTwo": "di zhi er",
        "city": "Peking",
        "stateProvince": "Peking",
        "post": "21231",
        "country": "China",
    }
]

test_data_for_select_by_names = [("abc efd", True), ("aaa", False)]

test_data_for_select_by_emails = [("qwe12@ewq.de", True), ("123@321.de", False)]

test_data_for_edit_contact = [{
    "firstname": "abc",
    "lastname": "efd",
    "birthdate": "2000-01-01",
    "email": "qwe@ewq.de",
    "phone": "111222333444",
    "streetOne": "Addresse Eins",
    "streetTwo": "Addresse Zwei",
    "city": "New York",
    "stateProvince": "New York",
    "post": "312334",
    "country": "USA",
}]

test_data_for_edit_contact_with_error_message = [
    ({
         "firstname": "",
         "lastname": "efd",
         "birthdate": "2000-01-01",
         "email": "qwe@ewq.de",
         "phone": "111222333444",
         "streetOne": "Addresse Eins",
         "streetTwo": "Addresse Zwei",
         "city": "New York",
         "stateProvince": "New York",
         "post": "312334",
         "country": "USA",
     }, "Path `firstName` is required"),
    ({
         "firstname": "abc",
         "lastname": "efd",
         "birthdate": "qafds",
         "email": "qwe@ewq.de",
         "phone": "111222333444",
         "streetOne": "Addresse Eins",
         "streetTwo": "Addresse Zwei",
         "city": "New York",
         "stateProvince": "New York",
         "post": "312334",
         "country": "USA",
     }, "Birthdate is invalid"),
    ({
         "firstname": "abc",
         "lastname": "efd",
         "birthdate": "2000-01-01",
         "email": "qweewq.de",
         "phone": "111222333444",
         "streetOne": "Addresse Eins",
         "streetTwo": "Addresse Zwei",
         "city": "New York",
         "stateProvince": "New York",
         "post": "312334",
         "country": "USA",
     }, "Email is invalid"),
]
