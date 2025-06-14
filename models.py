from db import conn, cursor as cur
import datetime

#******************* Function to add events*****************

def add_event():

    event_name = input("Enter event name: ").strip()
    event_date_input = input("Enter event date (YYYY-MM-DD): ").strip()
    location = input("Enter event location: ").strip()

    try:
        # Convert string to date object
        event_date = datetime.datetime.strptime(event_date_input, "%Y-%m-%d").date()
        cur.execute(
                "INSERT INTO events (event_name, event_date, location) VALUES (%s, %s, %s)",
                (event_name, event_date, location)
            )
        conn.commit()
        print(" Event created successfully.")
    except ValueError:
            print(" Invalid date format. Please use YYYY-MM-DD.")
    except Exception as e:
            print(" Failed to create event:", e)
            conn.rollback()

#******************* Function to add guests*****************

def add_guests():

    cur.execute("SELECT event_id, event_name FROM events")
    events = cur.fetchall()
    if not events:
            print("No events found. Please create an event first.")
    else:
        print("\n Available Events:")
        for e in events:
            print(f"{e[0]}. {e[1]}")
            
        try:
            event_id = int(input("Enter Event ID to add guest: "))
            guest_name = input("Enter guest name: ")
            email = input("Enter guest email: ")
            rsvp = input("RSVP (Yes/No): ").capitalize()

            # Create dictionary for guest
            guest = {
                "name": guest_name,
                "email": email,
                "rsvp_status": rsvp
            }

            # Check if guest already exists for this event
            cur.execute(
                 "SELECT * FROM guests WHERE event_id = %s AND email = %s",
                 (event_id, guest["email"])
            )
            existing = cur.fetchone()

            if existing:
                print(" Guest already exists for this event.")
            else:
                cur.execute(
                    "INSERT INTO guests (event_id, name, email, rsvp_status) VALUES (%s, %s, %s, %s)",
                    (event_id, guest["name"], guest["email"], guest["rsvp_status"])
                )
                conn.commit()
                print(" Guest added successfully.")
        except Exception as e:
            print(" Error adding guest:", e)
            conn.rollback()
