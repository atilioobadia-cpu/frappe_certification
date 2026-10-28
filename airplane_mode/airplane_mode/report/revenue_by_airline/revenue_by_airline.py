

def execute(filters=None):
    columns = [
        {"fieldname": "airline", "label": "Airline", "fieldtype": "Link", "options": "Airline", "width": 200},
        {"fieldname": "revenue", "label": "Revenue", "fieldtype": "Currency", "width": 150},
    ]

    # Get all airlines
    airlines = frappe.get_all("Airline", fields=["name"], order_by="name")
    
    # Get revenue per airline from submitted tickets
    revenue_data = frappe.db.sql("""
        SELECT 
            airplane.airline,
            SUM(ticket.total_amount) as revenue
        FROM `tabAirplane Ticket` ticket
        JOIN `tabAirplane Flight` flight ON flight.name = ticket.flight
        JOIN `tabAirplane` airplane ON airplane.name = flight.airplane
        WHERE ticket.docstatus = 1
        GROUP BY airplane.airline
    """, as_dict=True)
    
    revenue_map = {d.airline: d.revenue or 0 for d in revenue_data}
    
    data = []
    total_revenue = 0
    for airline in airlines:
        rev = revenue_map.get(airline.name, 0) or 0
        data.append({
            "airline": airline.name,
            "revenue": rev,
        })
        total_revenue += rev
    
    # Add total row
    data.append({
        "airline": "Total",
        "revenue": total_revenue,
    })
    
    # Chart
    chart = {
        "data": {
            "labels": [d["airline"] for d in data if d["airline"] != "Total"],
            "datasets": [{"name": "Revenue", "values": [d["revenue"] for d in data if d["airline"] != "Total"]}],
        },
        "type": "donut",
    }
    
    # Summary
    summary = [
        {"value": total_revenue, "label": "Total Revenue", "datatype": "Currency"},
    ]
    
    return columns, data, None, chart, summary
