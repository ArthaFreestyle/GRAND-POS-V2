{
    "name": "Stationary Barcode Scanner",
    "version": "18.0.1.0.0",
    "category": "Sales",
    "summary": "Scan barcode untuk menambah barang stationary ke Sales Order secara cepat",
    "description": "Addon untuk mempercepat input barang stationary yang banyak variasinya menggunakan barcode scanner",
    "author": "Grand POS Team",
    "depends": ["sale", "barcodes"],
    "data": [
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "stationary_barcode_scanner/static/src/css/barcode_scanner.css",
            "stationary_barcode_scanner/static/src/js/barcode_scanner.js",
            "stationary_barcode_scanner/static/src/xml/barcode_scanner.xml",
        ],
    },
    "installable": True,
    "application": False,
    "auto_install": False,
    "license": "LGPL-3",
}
