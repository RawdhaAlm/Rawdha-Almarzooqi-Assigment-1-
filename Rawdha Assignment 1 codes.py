# Define the Customer class with attributes, constructor, and getters/setters
class Customer:
    # Constructor to initialize the Customer object with its attributes
    def __init__(self, first_name, last_name, email, phone_number, reservation_id):
        self.first_name = first_name  # Public attribute for the first name
        self.last_name = last_name    # Public attribute for the last name
        self.email = email            # Public attribute for the email
        self.phone_number = phone_number  # Public attribute for the phone number
        self.reservation_id = reservation_id  # Public attribute for the reservation ID

    # Getter for first name
    def get_first_name(self):
        return self.first_name

    # Setter for first name
    def set_first_name(self, first_name):
        self.first_name = first_name

    # Getter for last name
    def get_last_name(self):
        return self.last_name

    # Setter for last name
    def set_last_name(self, last_name):
        self.last_name = last_name

    # Getter for email
    def get_email(self):
        return self.email

    # Setter for email
    def set_email(self, email):
        self.email = email

    # Getter for phone number
    def get_phone_number(self):
        return self.phone_number

    # Setter for phone number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    # Getter for reservation ID
    def get_reservation_id(self):
        return self.reservation_id

    # Setter for reservation ID
    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    # Other required function header - use a pass statement
    # This function could be used to confirm the reservation
    def confirm_reservation(self):
        pass  # This function will confirm the reservation process

    # This function could be used to modify reservation details
    def modify_reservation(self):
        pass  # This function will allow reservation modification


# Creating a Customer object with sample data
customer_1 = Customer("Ted", "Vera", "tedvera@mac.com", "555-1234", "52523687")

# Displaying customer details using getters
print("Customer 1 Details:")
print("First Name:", customer_1.get_first_name())
print("Last Name:", customer_1.get_last_name())
print("Email:", customer_1.get_email())
print("Phone Number:", customer_1.get_phone_number())
print("Reservation ID:", customer_1.get_reservation_id())




# Define the Reservation class with attributes, constructor, and getters/setters
class Reservation:
    # Constructor to initialize the Reservation object with its attributes
    def __init__(self, reservation_id, check_in_date, check_out_date, room_type, total_cost):
        self.reservation_id = reservation_id      # Public attribute for the reservation ID
        self.check_in_date = check_in_date        # Public attribute for check-in date
        self.check_out_date = check_out_date      # Public attribute for check-out date
        self.room_type = room_type                # Public attribute for room type
        self.total_cost = total_cost              # Public attribute for the total cost

    # Getter for reservation ID
    def get_reservation_id(self):
        return self.reservation_id

    # Setter for reservation ID
    def set_reservation_id(self, reservation_id):
        self.reservation_id = reservation_id

    # Getter for check-in date
    def get_check_in_date(self):
        return self.check_in_date

    # Setter for check-in date
    def set_check_in_date(self, check_in_date):
        self.check_in_date = check_in_date

    # Getter for check-out date
    def get_check_out_date(self):
        return self.check_out_date

    # Setter for check-out date
    def set_check_out_date(self, check_out_date):
        self.check_out_date = check_out_date

    # Getter for room type
    def get_room_type(self):
        return self.room_type

    # Setter for room type
    def set_room_type(self, room_type):
        self.room_type = room_type

    # Getter for total cost
    def get_total_cost(self):
        return self.total_cost

    # Setter for total cost
    def set_total_cost(self, total_cost):
        self.total_cost = total_cost

    # Other required function header - use a pass statement
    # This function could be used to confirm the reservation
    def confirm_reservation(self):
        pass  # This function will confirm the reservation process

    # This function could be used to modify reservation details
    def modify_reservation(self):
        pass  # This function will allow reservation modification


# Creating a Reservation object with sample data
reservation_1 = Reservation("52523687", "Sun, Aug 22, 2010", "Tue, Aug 24, 2010", "2 Queen Beds, Non-Smoking", 201.48)

# Displaying reservation details using getters
print("Reservation Details:")
print("Reservation ID:", reservation_1.get_reservation_id())
print("Check-In Date:", reservation_1.get_check_in_date())
print("Check-Out Date:", reservation_1.get_check_out_date())
print("Room Type:", reservation_1.get_room_type())
print("Total Cost: $", reservation_1.get_total_cost())




# Define the Hotel class with attributes, constructor, and getters/setters
class Hotel:
    # Constructor to initialize the Hotel object with its attributes
    def __init__(self, hotel_name, address, phone_number, available_rooms, room_rates):
        self.hotel_name = hotel_name          # Public attribute for the hotel name
        self.address = address                # Public attribute for the hotel address
        self.phone_number = phone_number      # Public attribute for the phone number
        self.available_rooms = available_rooms  # Public attribute for available rooms
        self.room_rates = room_rates          # Public attribute for the room rates

    # Getter for hotel name
    def get_hotel_name(self):
        return self.hotel_name

    # Setter for hotel name
    def set_hotel_name(self, hotel_name):
        self.hotel_name = hotel_name

    # Getter for address
    def get_address(self):
        return self.address

    # Setter for address
    def set_address(self, address):
        self.address = address

    # Getter for phone number
    def get_phone_number(self):
        return self.phone_number

    # Setter for phone number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

    # Getter for available rooms
    def get_available_rooms(self):
        return self.available_rooms

    # Setter for available rooms
    def set_available_rooms(self, available_rooms):
        self.available_rooms = available_rooms

    # Getter for room rates
    def get_room_rates(self):
        return self.room_rates

    # Setter for room rates
    def set_room_rates(self, room_rates):
        self.room_rates = room_rates

    # Other required function header - use a pass statement
    # This function could be used to check room availability
    def check_availability(self):
        pass  # This function will check if rooms are available

    # This function could be used to manage room bookings
    def manage_booking(self):
        pass  # This function will handle room booking management


# Creating a Hotel object with sample data
hotel_1 = Hotel("Comfort Inn & Suites Los Alamos", "2455 Trinity Drive, Los Alamos, NM 87544", "505-661-1110", 50, 89.95)

# Displaying hotel details using getters
print("Hotel Details:")
print("Hotel Name:", hotel_1.get_hotel_name())
print("Address:", hotel_1.get_address())
print("Phone Number:", hotel_1.get_phone_number())
print("Available Rooms:", hotel_1.get_available_rooms())
print("Room Rates: $", hotel_1.get_room_rates(), "per night")

 

# Define the Payment class with attributes, constructor, and getters/setters
class Payment:
    # Constructor to initialize the Payment object with its attributes
    def __init__(self, payment_method, amount, taxes_and_fees, transaction_id, payment_status):
        self.payment_method = payment_method    # Public attribute for the payment method
        self.amount = amount                    # Public attribute for the total amount
        self.taxes_and_fees = taxes_and_fees    # Public attribute for taxes and fees
        self.transaction_id = transaction_id    # Public attribute for the transaction ID
        self.payment_status = payment_status    # Public attribute for the payment status

    # Getter for payment method
    def get_payment_method(self):
        return self.payment_method

    # Setter for payment method
    def set_payment_method(self, payment_method):
        self.payment_method = payment_method

    # Getter for amount
    def get_amount(self):
        return self.amount

    # Setter for amount
    def set_amount(self, amount):
        self.amount = amount

    # Getter for taxes and fees
    def get_taxes_and_fees(self):
        return self.taxes_and_fees

    # Setter for taxes and fees
    def set_taxes_and_fees(self, taxes_and_fees):
        self.taxes_and_fees = taxes_and_fees

    # Getter for transaction ID
    def get_transaction_id(self):
        return self.transaction_id

    # Setter for transaction ID
    def set_transaction_id(self, transaction_id):
        self.transaction_id = transaction_id

    # Getter for payment status
    def get_payment_status(self):
        return self.payment_status

    # Setter for payment status
    def set_payment_status(self, payment_status):
        self.payment_status = payment_status

    # Other required function header - use a pass statement
    # This function could be used to process the payment
    def process_payment(self):
        pass  # This function will process the payment

    # This function could be used to validate payment details
    def validate_payment(self):
        pass  # This function will validate the payment information


# Creating a Payment object with sample data
payment_1 = Payment("Mastercard ending in 9904", 201.48, 21.58, "1234567890", "Success")

# Displaying payment details using getters
print("Payment Details:")
print("Payment Method:", payment_1.get_payment_method())
print("Amount: $", payment_1.get_amount())
print("Taxes and Fees: $", payment_1.get_taxes_and_fees())
print("Transaction ID:", payment_1.get_transaction_id())
print("Payment Status:", payment_1.get_payment_status())
