from db import conn, cursor as cur
import datetime
from models import add_event
from models import add_guests
from utils import view_guest_list_nested
from utils import show_rsvp_summary
from utils import show_events_with_no_guests
from utils import search_guest_by_email

print("📅 Welcome to DataSense Event Planner!")

while True:
    print("\nMenu:")
    print("1. Create New Event")
    print("2. Add Guest to Event")
    print("3. View Guest List")
    print("4. Show RSVP Summary")
    print("5. Show Events with No Guests")
    print("6. Search Guest by Email")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    if choice == '1':
        add_event()
        

    elif choice == '2':
        add_guests()

    elif choice == '3':
        view_guest_list_nested()

    elif choice == '4':
        show_rsvp_summary()

    elif choice == '5':
        show_events_with_no_guests()

    elif choice == '6':
        search_guest_by_email()

    elif choice == '7':
        print("Thank you for using DataSense Event Planner. Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

cur.close()
conn.close()