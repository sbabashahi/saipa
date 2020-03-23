/authnz/register/   no authorization
    
    Post
        username min 5 max 20 char
        password min 5 max 10 char

    example input
    
        {"username":"saeed1", "password": "123456"}
    
    example output
    
        {"data": {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InNhZWVkMiIsImV4cCI6MTU4NzU3MjU2NiwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU4NDk4MDU2Nn0.-8DZiYaO55fHnJbc9JgyeQ7Tgx16W24soy_BjbrxhY0"
        },
        "message": null,
        "current_time": 1584980566,
        "success": true,
        "index": null,
        "total": null}

/authnz/login/  no authorization

    Post
        username min 5 max 20 char
        password min 5 max 10 char

    example input
    
        {"username":"saeed1", "password": "123456"}
    
    example output
    
        {"data": {
            "token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6InNhZWVkMiIsImV4cCI6MTU4NzU3MjU2NiwiZW1haWwiOiIiLCJvcmlnX2lhdCI6MTU4NDk4MDU2Nn0.-8DZiYaO55fHnJbc9JgyeQ7Tgx16W24soy_BjbrxhY0"
        },
        "message": null,
        "current_time": 1584980566,
        "success": true,
        "index": null,
        "total": null}

/upload_excel/  need authorization, need superuser access

    Post
    
    example input
    
        {"file": file_upload} in postman use body form-data
    
    example output
    
        {"data": {},
        "message": null,
        "current_time": 1584980927,
        "success": true,
        "index": null,
        "total": null}

/car/list/  need authorization, need superuser access

    Get
    
        pagination using index=0&size=20
        
    example output
    
        {"data": [
            {
                "name": "Pride 131",
                "total": 2000,
                "total_sold": 1000
            },
            {
                "name": "Pride 132",
                "total": 4000,
                "total_sold": 0
            },
            .
            .
            .
            {
                "name": "212",
                "total": 38000,
                "total_sold": 0
            },
            {
                "name": "213",
                "total": 40000,
                "total_sold": 0
            }
        ],
        "message": null,
        "current_time": 1584980980,
        "success": true,
        "index": 0,
        "total": 32}
    
/car_stock/list/    need authorization

    Get
    
        pagination using index=0&size=20
       
    {"data": [
        {
            "name": "Pride 131",
            "date": "11/10/1398",
            "total": 1000,
            "total_sold": 1000
        },
        {
            "name": "Pride 132",
            "date": "12/10/1398",
            "total": 2000,
            "total_sold": 0
        },
        .
        .
        .
        {
            "name": "212",
            "date": "01/01/1399",
            "total": 19000,
            "total_sold": 0
        },
        {
            "name": "213",
            "date": "01/01/1399",
            "total": 20000,
            "total_sold": 0
        }
    ],
    "message": null,
    "current_time": 1584981191,
    "success": true,
    "index": 0,
    "total": 64}

/car/buy/   need authorization

    Post
        name car name max 20 min 2
        date "day/month/year" max 10 min 8  convert jalali to georgian, system default is georgian
        count optional int default is 1

    example input
    
        {"name":"Pride 131", "date": "11/10/1398", "count": 10}
    
    example output
    
        {"data": null,
        "message": "Done",
        "current_time": 1584981662,
        "success": true,
        "index": null,
        "total": null}

JWT Authorization

    set in headet
    
        Authorization: JWT YOUR_JWT_TOKEN