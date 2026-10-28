import frappe
import random
import string


def execute():
    tickets = frappe.get_all("Airplane Ticket", filters={"seat": ["in", ["", None]]}, fields=["name"])
    for t in tickets:
        random_int = random.randint(1, 100)
        random_letter = random.choice(string.ascii_uppercase[:5])
        seat = f"{random_int}{random_letter}"
        frappe.db.set_value("Airplane Ticket", t.name, "seat", seat, update_modified=False)
    frappe.db.commit()
