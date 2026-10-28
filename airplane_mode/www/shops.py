import frappe

def get_context(context):
    context.shops = frappe.get_all(
        "Shop",
        filters={"is_published": 1},
        fields=["name", "shop_name", "shop_number", "airport", "status", "route"],
        order_by="shop_name",
    )
    context.title = "Shops"
    context.no_cache = 1
