# Copyright (c) 2026, Atilio Obadia and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        self.status = "Completed"
        self.save()

    def on_update(self):
        try:
            if self.has_value_changed("gate_number"):
                frappe.enqueue(
                    "airplane_mode.airplane_mode.doctype.airplane_flight.airplane_flight.update_ticket_gates",
                    flight=self.name,
                    gate_number=self.get("gate_number"),
                )
        except Exception:
            pass

    def on_update_after_submit(self):
        try:
            if self.has_value_changed("gate_number"):
                frappe.enqueue(
                    "airplane_mode.airplane_mode.doctype.airplane_flight.airplane_flight.update_ticket_gates",
                    flight=self.name,
                    gate_number=self.get("gate_number"),
                )
        except Exception:
            pass


def update_ticket_gates(flight, gate_number):
    tickets = frappe.get_all("Airplane Ticket", filters={"flight": flight}, fields=["name"])
    for t in tickets:
        frappe.db.set_value("Airplane Ticket", t.name, "gate_number", gate_number)
    frappe.db.commit()
