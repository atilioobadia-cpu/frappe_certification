import frappe
import random
import string
from frappe.model.document import Document


class AirplaneTicket(Document):
    def before_insert(self):
        random_int = random.randint(1, 100)
        random_letter = random.choice(string.ascii_uppercase[:5])  # A-E
        self.seat = f"{random_int}{random_letter}"

    def before_save(self):
        # Auto-set full name is on Flight Passenger, not here
        total = self.flight_price or 0
        for addon in (self.add_ons or []):
            total += addon.amount or 0
        self.total_amount = total

    def validate(self):
        # Remove duplicate add-ons
        seen = set()
        unique_addons = []
        for addon in (self.add_ons or []):
            if addon.item in seen:
                continue
            seen.add(addon.item)
            unique_addons.append(addon)
        self.add_ons = unique_addons

        # Capacity check
        if self.flight:
            flight = frappe.get_doc("Airplane Flight", self.flight)
            airplane = frappe.get_doc("Airplane", flight.airplane)
            capacity = airplane.capacity or 0
            existing_tickets = frappe.db.count(
                "Airplane Ticket",
                filters={"flight": self.flight, "docstatus": ["!=", 2]},
            )
            if existing_tickets >= capacity:
                frappe.throw(
                    f"Cannot create ticket: flight {self.flight} has reached its capacity of {capacity} seats."
                )

    def before_submit(self):
        if self.status != "Boarded":
            frappe.throw("Cannot submit ticket unless status is Boarded")
