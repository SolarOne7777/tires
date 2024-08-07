async function addTire() {
    const tireData = {
        tire_id: document.getElementById('add_tire_id').value,
        tire_type: document.getElementById('add_tire_type').value,
        condition: document.getElementById('add_condition').value,
        price: parseFloat(document.getElementById('add_price').value),
        quantity: parseInt(document.getElementById('add_quantity').value)
    };

    const response = await fetch('/add_tire', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(tireData)
    });

    const result = await response.json();
    document.getElementById('add_tire_message').textContent = result.message;
}

async function sellTire() {
    const sellData = {
        tire_id: document.getElementById('sell_tire_id').value,
        quantity: parseInt(document.getElementById('sell_quantity').value)
    };

    const response = await fetch('/sell_tire', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(sellData)
    });

    const result = await response.json();
    document.getElementById('sell_tire_message').textContent = result.message;
}

async function generateInvoice() {
    const items = JSON.parse(document.getElementById('invoice_items').value);
    const response = await fetch('/generate_invoice', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ items })
    });

    const result = await response.json();
    document.getElementById('invoice_message').textContent = result.invoice;
}
