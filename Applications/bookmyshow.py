def show_movies(movies):
    print("Available Movies:")

    for i,j in movies.items():
        print(f"{i} | Price: {j['price']} | Seats: {j['seats']}")

def check_availability(movies,movie_name,seats_needed):
    if movie_name not in movies:
        print("Movie Not Found")
        return False

    if seats_needed <= 0:
        print("Please Enter Seats Greater than 0")
        return False

    if movies[movie_name]['seats'] < seats_needed:
        print("Not Enough Seats")
        return False

    return True

def book_tickets(movies,movie_name,seats_needed,bookings):
    if check_availability(movies,movie_name,seats_needed):
        cost=seats_needed*movies[movie_name]['price']
        movies[movie_name]["seats"] -= seats_needed
        bookings.append({"Movie":movie_name,"seats":seats_needed,"cost":cost})
        print(f"Booked {seats_needed} seats for {movie_name} | Total : {cost}")
    return movies,bookings


def view_booking(bookings):
    if not bookings:
        print("No Bookings Yet")
    else:
        print("===Your Bookings===")
        for i,j in enumerate(bookings,1):
            print(f"{i}. {j['Movie']} | {j['seats']} | Cost : {j['cost']}")

def update_booking(movies, bookings):
    if not bookings:
        print("No Bookings Yet")
        return movies, bookings

    view_booking(bookings)

    booking_no = int(input("Enter Booking Number to Update: "))

    if booking_no < 1 or booking_no > len(bookings):
        print("Invalid Booking Number")
        return movies, bookings

    booking = bookings[booking_no - 1]

    movie_name = booking["Movie"]
    old_seats = booking["seats"]

    new_seats = int(input("Enter New Number of Seats: "))

    available = movies[movie_name]["seats"] + old_seats

    if new_seats > available:
        print("Not Enough Seats Available")
        return movies, bookings

    movies[movie_name]["seats"] = available - new_seats

    booking["seats"] = new_seats
    booking["cost"] = new_seats * movies[movie_name]["price"]

    print("Booking Updated Successfully")

    return movies, bookings

def cancel_booking(movies, bookings):
    if not bookings:
        print("No Bookings Yet")
        return movies, bookings

    view_booking(bookings)

    booking_no = int(input("Enter Booking Number to Cancel: "))
    if booking_no < 1 or booking_no > len(bookings):
        print("Invalid Booking Number")
        return movies, bookings

    booking = bookings.pop(booking_no - 1)
    movie_name = booking["Movie"]
    seats = booking["seats"]

    movies[movie_name]["seats"] += seats

    print("Booking Canceled Successfully")
    return movies, bookings


def main():
    movies={"F1":{"price":250,"seats":10},
            "Interstellar":{"price":210,"seats":20},
            "Dark Knight":{"price":260,"seats":12}
    }

    bookings=[]

    while True:
        print("================BookMyShow Ticket Booking==================")
        print("1. Show Movies")
        print("2. Book Tickets")
        print("3. View My Bookings")
        print("4. Update Bookings")
        print("5. Cancel Bookings")
        print("6. Exit")

        choice=int(input("Enter your choice: "))
        if choice == 1:
            show_movies(movies)

        elif choice == 2:
            movie_name=input("Enter Movie Name: ")
            seats_needed=int(input("Enter Seats needed: "))
            movies,bookings=book_tickets(movies,movie_name,seats_needed,bookings)

        elif choice == 3:
            view_booking(bookings)

        elif choice == 4:
            movies, bookings = update_booking(movies, bookings)

        elif choice == 5:
            movies, bookings = cancel_booking(movies, bookings)

        elif choice == 6:
            print("Thank You!!!")
            break

        else:
            print("Invalid Choice")

main()