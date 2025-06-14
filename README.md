# 🎉 DataSense Event Planner

A beginner-friendly Python + PostgreSQL console application to plan events, manage guests, and track RSVPs. Built with clean structure using basic Python concepts like sets, dictionaries, and tuples — without functions in main logic for simplicity!

---

## 🚀 Features

1. **Create New Event**  
   - Input: Event name, date (YYYY-MM-DD), location  
   - Stores to PostgreSQL

2. **Add Guest to Event**  
   - Input: Event ID, guest name, email, RSVP (Yes/No)  
   - Stores to PostgreSQL

3. **View Guest List**  
   - Displays all guests grouped by event  
   - Uses nested dictionaries for clean structure

4. **RSVP Summary**  
   - Shows RSVP counts (Yes / No / No Response) for each event

5. **Events With No Guests**  
   - Lists all events that have no guests added

6. **Search Guest by Email**  
   - Finds guest details with their RSVP and event info
