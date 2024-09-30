# Define the Customer class with attributes, constructor, and getters/setters
class Customer:
    # Constructor to initialize the Customer object with its attributes
    def __init__(self, first_name, last_name, email, phone_number, reservation_id):
        self._first_name = first_name  # Private attribute for the first name
        self._last_name = last_name    # Private attribute for the last name
        self._email = email            # Private attribute for the email
        self._phone_number = phone_number  # Private attribute for the phone number
        self._reservation_id = reservation_id  # Private attribute for the reservation ID

    # Getter for first name
    def get_first_name(self):
        return self._first_name

    # Setter for first name
    def set_first_name(self, first_name):
        self._first_name = first_name

    # Getter for last name
    def get_last_name(self):
        return self._last_name

    # Setter for last name
    def set_last_name(self, last_name):
        self._last_name = last_name

    # Getter for email
    def get_email(self):
        return self._email

    # Setter for email
    def set_email(self, email):
        self._email = email

    # Getter for phone number
    def get_phone_number(self):
        return self._phone_number

    # Setter for phone number
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    # Getter for reservation ID
    def get_reservation_id(self):
        return self._reservation_id

    # Setter for reservation ID
    def set_reservation_id(self, reservation_id):
        self._reservation_id = reservation_id

    # Function header - use a pass statement
    # This function could be used to confirm the customer's reservation
    def confirm_reservation(self):
        pass  # Functionality to confirm reservation goes here

    # Function header - use a pass statement
    # This function could be used to modify reservation details
    def modify_reservation(self):
        pass  # Functionality to modify the reservation goes here

    # Function header - use a pass statement
    # This function could be used to cancel the reservation
    def cancel_reservation(self):
        pass  # Functionality to cancel the reservation goes here


# Creating a Customer object with sample data
customer_1 = Customer("Ted", "Vera", "tedvera@mac.com", "555-1234", "52523687")

# Displaying customer details using getters
print("Customer 1 Details:")
print("First Name:", customer_1.get_first_name())
print("Last Name:", customer_1.get_last_name())
print("Email:", customer_1.get_email())
print("Phone Number:", customer_1.get_phone_number())
print("Reservation ID:", customer_1.get_reservation_id())

# Using setters to modify the first name and phone number
customer_1.set_first_name("Theodore")
customer_1.set_phone_number("555-5678")

# Displaying updated customer details after using setters
print("\nUpdated Customer 1 Details:")
print("First Name:", customer_1.get_first_name())
print("Last Name:", customer_1.get_last_name())
print("Email:", customer_1.get_email())
print("Phone Number:", customer_1.get_phone_number())
print("Reservation ID:", customer_1.get_reservation_id())




# Define the Reservation class with attributes, constructor, and getters/setters
class Reservation:
    # Constructor to initialize the Reservation object with its attributes
    def __init__(self, reservation_id, check_in_date, check_out_date, room_type, total_cost):
        self._reservation_id = reservation_id      # Private attribute for the reservation ID
        self._check_in_date = check_in_date        # Private attribute for check-in date
        self._check_out_date = check_out_date      # Private attribute for check-out date
        self._room_type = room_type                # Private attribute for room type
        self._total_cost = total_cost              # Private attribute for total cost

    # Getter for reservation ID
    def get_reservation_id(self):
        return self._reservation_id

    # Setter for reservation ID
    def set_reservation_id(self, reservation_id):
        self._reservation_id = reservation_id

    # Getter for check-in date
    def get_check_in_date(self):
        return self._check_in_date

    # Setter for check-in date
    def set_check_in_date(self, check_in_date):
        self._check_in_date = check_in_date

    # Getter for check-out date
    def get_check_out_date(self):
        return self._check_out_date

    # Setter for check-out date
    def set_check_out_date(self, check_out_date):
        self._check_out_date = check_out_date

    # Getter for room type
    def get_room_type(self):
        return self._room_type

    # Setter for room type
    def set_room_type(self, room_type):
        self._room_type = room_type

    # Getter for total cost
    def get_total_cost(self):
        return self._total_cost

    # Setter for total cost
    def set_total_cost(self, total_cost):
        self._total_cost = total_cost

    # Function header - use a pass statement
    # This function could be used to confirm the reservation
    def confirm_reservation(self):
        pass  # Functionality to confirm the reservation goes here

    # Function header - use a pass statement
    # This function could be used to modify reservation details
    def modify_reservation(self):
        pass  # Functionality to modify the reservation goes here

    # Function header - use a pass statement
    # This function could be used to cancel the reservation
    def cancel_reservation(self):
        pass  # Functionality to cancel the reservation goes here


# Creating a Reservation object with sample data
reservation_1 = Reservation("52523687", "Sun, Aug 22, 2010", "Tue, Aug 24, 2010", "2 Queen Beds, Non-Smoking", 201.48)

# Displaying reservation details using getters
print("Reservation Details:")
print("Reservation ID:", reservation_1.get_reservation_id())
print("Check-In Date:", reservation_1.get_check_in_date())
print("Check-Out Date:", reservation_1.get_check_out_date())
print("Room Type:", reservation_1.get_room_type())
print("Total Cost: $", reservation_1.get_total_cost())

# Using setters to modify the check-in date and room type
reservation_1.set_check_in_date("Mon, Aug 23, 2010")
reservation_1.set_room_type("King Bed, Non-Smoking")

# Displaying updated reservation details after using setters
print("\nUpdated Reservation Details:")
print("Reservation ID:", reservation_1.get_reservation_id())
print("Check-In Date:", reservation_1.get_check_in_date())
print("Check-Out Date:", reservation_1.get_check_out_date())
print("Room Type:", reservation_1.get_room_type())
print("Total Cost: $", reservation_1.get_total_cost())




# Define the Hotel class with private attributes, constructor, and getters/setters
class Hotel:
    # Constructor to initialize the Hotel object with its attributes
    def __init__(self, hotel_name, address, phone_number, available_rooms, room_rates):
        self._hotel_name = hotel_name          # Private attribute for the hotel name
        self._address = address                # Private attribute for the address
        self._phone_number = phone_number      # Private attribute for the phone number
        self._available_rooms = available_rooms  # Private attribute for the available rooms
        self._room_rates = room_rates          # Private attribute for the room rates

    # Getter for hotel name
    def get_hotel_name(self):
        return self._hotel_name

    # Setter for hotel name
    def set_hotel_name(self, hotel_name):
        self._hotel_name = hotel_name

    # Getter for address
    def get_address(self):
        return self._address

    # Setter for address
    def set_address(self, address):
        self._address = address

    # Getter for phone number
    def get_phone_number(self):
        return self._phone_number

    # Setter for phone number
    def set_phone_number(self, phone_number):
        self._phone_number = phone_number

    # Getter for available rooms
    def get_available_rooms(self):
        return self._available_rooms

    # Setter for available rooms
    def set_available_rooms(self, available_rooms):
        self._available_rooms = available_rooms

    # Getter for room rates
    def get_room_rates(self):
        return self._room_rates

    # Setter for room rates
    def set_room_rates(self, room_rates):
        self._room_rates = room_rates

    # Function header - use a pass statement
    # This function could be used to check room availability
    def check_availability(self):
        pass  # Functionality to check room availability goes here

    # Function header - use a pass statement
    # This function could be used to manage room bookings
    def manage_booking(self):
        pass  # Functionality to manage room bookings goes here


# Creating a Hotel object with sample data
hotel_1 = Hotel("Comfort Inn & Suites Los Alamos", "2455 Trinity Drive, Los Alamos, NM 87544", "505-661-1110", 50, 89.95)

# Displaying hotel details using getters
print("Hotel Details:")
print("Hotel Name:", hotel_1.get_hotel_name())
print("Address:", hotel_1.get_address())
print("Phone Number:", hotel_1.get_phone_number())
print("Available Rooms:", hotel_1.get_available_rooms())
print("Room Rates: $", hotel_1.get_room_rates(), "per night")

# Using setters to modify the hotel name and phone number
hotel_1.set_hotel_name("Holiday Inn Los Alamos")
hotel_1.set_phone_number("505-555-1111")

# Displaying updated hotel details after using setters
print("\nUpdated Hotel Details:")
print("Hotel Name:", hotel_1.get_hotel_name())
print("Address:", hotel_1.get_address())
print("Phone Number:", hotel_1.get_phone_number())
print("Available Rooms:", hotel_1.get_available_rooms())
print("Room Rates: $", hotel_1.get_room_rates(), "per night")

 

# Define the Payment class with private attributes, constructor, and getters/setters
class Payment:
    # Constructor to initialize the Payment object with its attributes
    def __init__(self, payment_method, amount, taxes_and_fees, transaction_id, payment_status):
        self._payment_method = payment_method    # Private attribute for the payment method
        self._amount = amount                    # Private attribute for the amount
        self._taxes_and_fees = taxes_and_fees    # Private attribute for taxes and fees
        self._transaction_id = transaction_id    # Private attribute for the transaction ID
        self._payment_status = payment_status    # Private attribute for the payment status

    # Getter for payment method
    def get_payment_method(self):
        return self._payment_method

    # Setter for payment method
    def set_payment_method(self, payment_method):
        self._payment_method = payment_method

    # Getter for amount
    def get_amount(self):
        return self._amount

    # Setter for amount
    def set_amount(self, amount):
        self._amount = amount

    # Getter for taxes and fees
    def get_taxes_and_fees(self):
        return self._taxes_and_fees

    # Setter for taxes and fees
    def set_taxes_and_fees(self, taxes_and_fees):
        self._taxes_and_fees = taxes_and_fees

    # Getter for transaction ID
    def get_transaction_id(self):
        return self._transaction_id

    # Setter for transaction ID
    def set_transaction_id(self, transaction_id):
        self._transaction_id = transaction_id

    # Getter for payment status
    def get_payment_status(self):
        return self._payment_status

    # Setter for payment status
    def set_payment_status(self, payment_status):
        self._payment_status = payment_status

    # Function header - use a pass statement
    # This function could be used to process the payment
    def process_payment(self):
        pass  # Functionality to process the payment goes here

    # Function header - use a pass statement
    # This function could be used to validate the payment
    def validate_payment(self):
        pass  # Functionality to validate payment information goes here


# Creating a Payment object with sample data
payment_1 = Payment("Mastercard ending in 9904", 201.48, 21.58, "1234567890", "Success")

# Displaying payment details using getters
print("Payment Details:")
print("Payment Method:", payment_1.get_payment_method())
print("Amount: $", payment_1.get_amount())
print("Taxes and Fees: $", payment_1.get_taxes_and_fees())
print("Transaction ID:", payment_1.get_transaction_id())
print("Payment Status:", payment_1.get_payment_status())

# Using setters to modify the payment method and payment status
payment_1.set_payment_method("Visa ending in 4321")
payment_1.set_payment_status("Pending")

# Displaying updated payment details after using setters
print("\nUpdated Payment Details:")
print("Payment Method:", payment_1.get_payment_method())
print("Amount: $", payment_1.get_amount())
print("Taxes and Fees: $", payment_1.get_taxes_and_fees())
print("Transaction ID:", payment_1.get_transaction_id())
print("Payment Status:", payment_1.get_payment_status())
  
