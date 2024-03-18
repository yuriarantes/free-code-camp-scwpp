def increment_space(space: int, value: str, char= ' ') -> str:
    str = ''

    for i in range(space-len(value)):
        str += char 

    str += value

    return str

class Category:
    def __init__(self, name) -> None:
        self.name = name
        self.ledger = []

    def __str__(self) -> None:
        len_space_title = int((30-(len(self.name)))/2)

        lines = {
            'title': f"{'*'*len_space_title}{self.name}{'*'*len_space_title}",
            'content': '',
            'footer': f"Total: {format(self.get_balance(),'.2f')}",
        }

        for v in self.ledger:
            amount = format(v['amount'],'.2f')

            len_space = int(30-(len(v['description']) + len(str(amount))))

            lines['content'] += f"{v['description']}{' '*len_space}{amount}\n"

        return f"{lines['title']}\n{lines['content'][:-1]}\n{lines['footer']}"

    def deposit(self, amount: float, description = '') -> bool:
        deposit_info = {
            "amount": amount, 
            "description": description
        }
        
        self.ledger.append(deposit_info)

        return True

    def get_balance(self) -> float:
        all_amount = []

        for value in self.ledger:
            all_amount.append(value['amount']) 
        
        return sum(all_amount)
    
    def withdraw(self, amount: float, description = '') -> bool:
        if not self.check_funds(amount):
            return False

        withdraw_info = {
            "amount": amount*-1, 
            "description": description
        }

        self.ledger.append(withdraw_info)

        return True
    
    def transfer(self, amount: float, category: 'Category') -> bool:
        if amount and category:
            if self.withdraw(amount, f"Transfer to {category.name}"):
                category.deposit(amount, f"Transfer from {self.name}")

                return True

        return False
    
    def check_funds(self, amount: float) -> bool:
        if amount > self.get_balance():
            return False

        return True

def create_spend_chart(categories):
    info_categories = {}

    for category in categories:
        info_categories[category.name] = 10

    print(info_categories)

    layout = {
        'title':'Percentage spent by category',
        'chart':[],
    }

    for percent in range(100,-1, -10):
        layout['chart'].append({percent: ''})

    pass

food = Category("Food")

pharmacy = Category("Pharmacy")

food.deposit(12, "Refri")
food.deposit(122.87, "Pacote marmita")

food.withdraw(122.00, "Supermercado")


food.transfer(2, pharmacy)

print("\n\n")

print(food)

print("\n\n")

print(pharmacy)

print("\n\n")

categories = [food, pharmacy]

create_spend_chart(categories)