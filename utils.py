from db import cursor as cur

#******************* Function to view guset lists*****************

def view_guest_list_nested():
    try:
        # Step 1: Fetch all events
        cur.execute("SELECT event_id, event_name FROM events")
        event_rows = cur.fetchall()

        if not event_rows:
            print(" No events available.")
            return

        # Step 2: Build nested structure
        events = []
        for e in event_rows:
            event_id, event_name = e
            cur.execute("SELECT name, email, rsvp_status FROM guests WHERE event_id = %s", (event_id,))
            guest_rows = cur.fetchall()
            guests = [
                {"name": g[0], "email": g[1], "rsvp_status": g[2]} for g in guest_rows
            ]
            events.append({
                "event_name": event_name,
                "guests": guests
            })

        # Step 3: Display
        for event in events:
            print(f"\n📅 Event: {event['event_name']}")
            if not event["guests"]:
                print("   ⚠️ No guests yet.")
            else:
                for guest in event["guests"]:
                    print(f"   👤 {guest['name']} ({guest['email']}) - RSVP: {guest['rsvp_status']}")
    except Exception as e:
        print(" Error displaying guest list:", e)


#******************* Function to show RSVP summary*****************

def show_rsvp_summary():
    try:
        # Step 1: Get all events
        cur.execute("SELECT event_id, event_name FROM events")
        event_rows = cur.fetchall()

        if not event_rows:
            print(" No events found.")
            return

        # Step 2: For each event, count RSVPs
        for event_id, event_name in event_rows:
            cur.execute("SELECT rsvp_status FROM guests WHERE event_id = %s", (event_id,))
            rsvps = [row[0] for row in cur.fetchall()]  

            summary = {
                "Yes": rsvps.count("Yes"),
                "No": rsvps.count("No"),
                "No Response": rsvps.count(None) + rsvps.count("")
            }

            print(f"\n RSVP Summary for '{event_name}' (ID: {event_id})")
            print(f" Yes: {summary['Yes']}")
            print(f" No: {summary['No']}")
            print(f" No Response: {summary['No Response']}")
    except Exception as e:
        print("Error showing RSVP summary:", e)


#******************* Function to show events with no guests*****************

def show_events_with_no_guests():
    try:
        # Step 1: Get events with no guests using LEFT JOIN
        cur.execute("""
            SELECT e.event_id, e.event_name
            FROM events e
            LEFT JOIN guests g ON e.event_id = g.event_id
            WHERE g.guest_id IS NULL
        """)
        no_guest_events = cur.fetchall()

        # Step 2: Display results
        if not no_guest_events:
            print("\n All events have at least one guest.")
        else:
            print("\n Events with No Guests:")
            for event_id, event_name in no_guest_events:
                print(f"   - {event_name} (ID: {event_id})")
    except Exception as e:
        print("Error fetching events with no guests:", e)


#******************* Function to search guests by email *****************

def search_guest_by_email():
    try:
        email = input(" Enter guest email to search: ").strip()

        if not email:
            print("Email cannot be empty.")
            return

        cur.execute("""
            SELECT g.name, g.email, g.rsvp_status, e.event_name, e.event_date
            FROM guests g
            JOIN events e ON g.event_id = e.event_id
            WHERE LOWER(g.email) = LOWER(%s)
        """, (email,))
        
        results = cur.fetchall()

        if not results:
            print("No guest found with that email.")
        else:
            print(f"\n Guest Records for '{email}':")
            for name, email, rsvp_status, event_name, event_date in results:
                print(f"👤 {name} | RSVP: {rsvp_status} | Event: {event_name} on {event_date}")
    except Exception as e:
        print("Error searching guest:", e)

