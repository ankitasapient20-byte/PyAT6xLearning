def validate_status_code(response_code):
    if response_code==200:
        print("Request is success")
    else:
        print("Request is failure")

        validate_status_code(200)
        validate_status_code(400)
        validae_status_code(response_code=400)