frappe.ui.form.on("Airplane", {
    refresh(frm) {
        if (!frappe.user.has_role("Airport Authority Personnel")) {
            frm.set_df_property("initial_audit_completed", "hidden", 1);
            frm.set_df_property("initial_audit_completed", "read_only", 1);
        }
    },
});
