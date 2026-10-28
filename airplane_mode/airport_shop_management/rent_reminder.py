import frappe
from frappe.utils import nowdate, add_days, get_first_day, get_last_day


def send_rent_reminders():
    """Send rent reminders to tenants if enabled in settings."""
    settings = frappe.get_single("Airport Shop Settings")
    if not settings.enable_rent_reminders:
        return

    shops = frappe.get_all("Shop", filters={"status": "Occupied"}, fields=["name", "tenant_name", "tenant_email", "rent_amount"])
    for shop in shops:
        if shop.tenant_email:
            frappe.sendmail(
                recipients=[shop.tenant_email],
                subject="Rent Due Reminder",
                message=f"""
                <p>Dear {shop.tenant_name},</p>
                <p>This is a reminder that rent of {shop.rent_amount} is due for shop {shop.name}.</p>
                <p>Please make the payment at your earliest convenience.</p>
                """,
                reference_doctype="Shop",
                reference_name=shop.name,
            )
