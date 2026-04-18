/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component, useRef, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class StationaryBarcodeScanner extends Component {
    static template = "stationary_barcode_scanner.BarcodeScanner";
    static props = {
        ...standardFieldProps,
    };

    setup() {
        this.orm = useService("orm");
        this.notification = useService("notification");
        this.inputRef = useRef("barcodeInput");
        
        onMounted(() => {
            // Auto focus on mount if possible
            if (this.inputRef.el) {
                this.inputRef.el.focus();
            }
        });
    }

    async onKeydown(ev) {
        if (ev.key === "Enter" || ev.keyCode === 13) {
            ev.preventDefault();
            const barcode = ev.target.value.trim();
            if (barcode) {
                // Determine order ID. In Odoo 18, it's usually inside props.record.resId
                const orderId = this.props.record.resId;
                if (!orderId) {
                    this.notification.add("Sistem belum menyimpan Order ini. Save terlebih dahulu sebelum scan.", { type: "warning" });
                    return;
                }

                try {
                    const result = await this.orm.call(
                        "sale.order",
                        "action_scan_barcode",
                        [orderId, barcode]
                    );

                    if (result.success) {
                        this.notification.add(result.message, { type: "success" });
                        // Reload data to reflect changes
                        await this.props.record.load();
                    } else {
                        this.notification.add(result.message, { type: "danger" });
                    }
                } catch (error) {
                    console.error("Barcode scan error", error);
                    this.notification.add("Gagal terhubung ke server", { type: "danger" });
                }
                
                // Clear the input and refocus
                ev.target.value = "";
                this.inputRef.el.focus();
            }
        }
    }
}

registry.category("fields").add("stationary_barcode_scanner", {
    component: StationaryBarcodeScanner,
});
