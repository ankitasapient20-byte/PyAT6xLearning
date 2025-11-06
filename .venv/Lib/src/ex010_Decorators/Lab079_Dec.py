def add_security(func):

    def wrapper():
        print("1. Before the func is calleed.")
        print("2. Add Helmet, Dashcash, gloves, knee gaurds")
        print("3. After the func is called.")
        print("4. Secure driving, Leave all the items")

        return wrapper()



    @add_security
    def drive_ola_scooter():
        print("I am driving Ola scooter")

    @add_security
    def drive_zypp_scooter():
        print("I am driving Zypp scooter")

drive_ola_scooter()
drive_zypp_scooter()