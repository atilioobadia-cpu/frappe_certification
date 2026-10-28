frappe.ui.form.on("Airplane Ticket", {
    refresh(frm) {
        frm.add_custom_button("Assign Seat", () => {
            let d = new frappe.ui.Dialog({
                title: "Assign Seat",
                fields: [
                    {
                        label: "Seat Number",
                        fieldname: "seat",
                        fieldtype: "Data",
                    },
                ],
                primary_action_label: "Assign",
                primary_action(values) {
                    frm.set_value("seat", values.seat);
                    d.hide();
                },
            });
            d.show();
        });
    },
});
