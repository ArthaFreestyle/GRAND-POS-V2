from odoo import models, fields, api, _
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    # Transient field solely for rendering the widget
    stationary_barcode = fields.Char(string="Scan Barcode", store=False)

    @api.model
    def action_scan_barcode(self, order_id, barcode):
        """
        API endpoint to handle barcode scan from the front-end widget
        order_id: integer corresponding to sale.order ID
        barcode: string from scanner
        """
        order = self.browse(order_id)
        if not order.exists():
            return {'success': False, 'message': _("Order not found.")}
            
        if order.state not in ['draft', 'sent']:
            return {'success': False, 'message': _("You can only scan items in draft or sent states.")}

        # Look up product by barcode prioritizing active products that can be sold
        product = self.env['product.product'].search([
            ('barcode', '=', barcode),
            ('sale_ok', '=', True)
        ], limit=1)

        if not product:
            return {'success': False, 'message': _("Produk dengan barcode %s tidak ditemukan atau tidak dapat dijual.") % barcode}

        # Check if the product already exists in the order lines
        existing_line = order.order_line.filtered(lambda l: l.product_id.id == product.id)
        
        if existing_line:
            # Increment quantity
            existing_line[0].product_uom_qty += 1.0
            return {
                'success': True, 
                'message': _("Quantity %s %s ditambah menjadi %s") % (product.name, product.barcode, existing_line[0].product_uom_qty)
            }
        else:
            # Create a new order line
            new_line = self.env['sale.order.line'].create({
                'order_id': order.id,
                'product_id': product.id,
                'product_uom_qty': 1.0,
            })
            return {
                'success': True,
                'message': _("Produk %s berhasil ditambahkan.") % product.name
            }
