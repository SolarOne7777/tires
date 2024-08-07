from flask import Flask, jsonify, request

app = Flask(__name__)

class Tire:
    def __init__(self, tire_id, tire_type, condition, price):
        self.tire_id = tire_id
        self.tire_type = tire_type
        self.condition = condition
        self.price = price

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_tire(self, tire, quantity):
        if tire.tire_id in self.stock:
            self.stock[tire.tire_id]['quantity'] += quantity
        else:
            self.stock[tire.tire_id] = {'tire': tire, 'quantity': quantity}

    def remove_tire(self, tire_id, quantity):
        if tire_id in self.stock:
            if self.stock[tire_id]['quantity'] >= quantity:
                self.stock[tire_id]['quantity'] -= quantity
                if self.stock[tire_id]['quantity'] == 0:
                    del self.stock[tire_id]
            else:
                return False
        return True

    def check_inventory(self):
        return self.stock

class Invoice:
    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, tire, quantity):
        self.items.append((tire, quantity))
        self.total += tire.price * quantity

    def generate_invoice(self):
        invoice_details = "Invoice:\n"
        for tire, quantity in self.items:
            invoice_details += f"Tire ID: {tire.tire_id}, Type: {tire.tire_type}, Quantity: {quantity}, Price: {tire.price * quantity}\n"
        invoice_details += f"Total Amount: {self.total}"
        return invoice_details

class Warehouse:
    def __init__(self):
        self.inventory = Inventory()

    def add_to_inventory(self, tire, quantity):
        self.inventory.add_tire(tire, quantity)

    def sell_tire(self, tire_id, quantity):
        return self.inventory.remove_tire(tire_id, quantity)

    def generate_invoice(self, items):
        invoice = Invoice()
        for item in items:
            tire = Tire(tire_id=item['tire_id'], tire_type=item['tire_type'], condition=item['condition'], price=item['price'])
            invoice.add_item(tire, item['quantity'])
        return invoice.generate_invoice()

warehouse = Warehouse()

@app.route('/add_tire', methods=['POST'])
def add_tire():
    data = request.json
    tire = Tire(tire_id=data['tire_id'], tire_type=data['tire_type'], condition=data['condition'], price=data['price'])
    warehouse.add_to_inventory(tire, data['quantity'])
    return jsonify({"message": "Tire added successfully!"})

@app.route('/sell_tire', methods=['POST'])
def sell_tire():
    data = request.json
    success = warehouse.sell_tire(data['tire_id'], data['quantity'])
    if success:
        return jsonify({"message": "Tire s
