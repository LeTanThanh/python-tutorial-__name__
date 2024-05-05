def calculate_tax(price, tax):
  return price * tax

def print_billing_doc():
  tax_rate = 0.1
  products = [
    {"name": "Book", "price": 30},
    {"name": "Pen", "price": 5}
  ]

  print("Name\tPrice\tTax")

  for product in products:
    tax = calculate_tax(product['price'], tax_rate)
    print(f"{product['name']}\t{product['price']}\t{tax}")

print(f"__name__: {__name__}")

if __name__ == "__main__":
  print_billing_doc()
