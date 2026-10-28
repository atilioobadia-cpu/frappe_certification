import frappe
from frappe.website.website_generator import WebsiteGenerator


class Shop(WebsiteGenerator):
    pass


def get_list(doctype, txt, filters, limit_start, limit_page_length=20, order_by=None):
    from frappe.www.list import get_list as _get_list

    return _get_list(
        doctype,
        txt,
        filters,
        limit_start,
        limit_page_length=limit_page_length,
        ignore_permissions=True,
    )


def get_list_context(context):
    context.title = "Shops"
    context.get_list = get_list
    context.list_template = "templates/includes/list/list.html"
    context.row_template = "airport_shop_management/doctype/shop/templates/shop_row.html"
    context.no_breadcrumbs = True
    return context
