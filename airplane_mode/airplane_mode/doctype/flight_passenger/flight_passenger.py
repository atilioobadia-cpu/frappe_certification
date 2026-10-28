import frappe
from frappe.model.document import Document


class FlightPassenger(Document):
    def before_save(self):
        self.full_name = f"{self.first_name or ''} {self.last_name or ''}".strip()
