class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items
        self.total = self.calculate_total()

    def calculate_total(self):
        return sum(qtd * preco for nome, qtd, preco in self.items)


class OrderProcessor:
    def __init__(self):
        self.inventory = {"Notebook": 10, "Mouse": 50, "Teclado": 30}

    def process_order(self, order):
        if not self._is_stock_available(order):
            raise Exception("Estoque insuficiente para um ou mais itens.")

        self._update_inventory(order)
        self._save_order(order)
        self._send_confirmation_email(order)
        
        return order.total

    def _is_stock_available(self, order):
        return all(self.inventory.get(item, 0) >= qtd for item, qtd, _ in order.items)

    def _update_inventory(self, order):
        for item, qtd, _ in order.items:
            self.inventory[item] -= qtd

    def _save_order(self, order):
        with open(f"pedido_{order.order_id}.txt", "w") as f:
            f.write(f"Pedido #{order.order_id} - Total: R${order.total}")

    def _send_confirmation_email(self, order):
        print(f"Enviando e-mail para cliente do pedido #{order.order_id} - Total: R${order.total}")
