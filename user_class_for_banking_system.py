class User:
    def __init__(self, nome='', inicial=0, checar=True):
        self.nome = nome
        self.balance = inicial
        self.checking_account = checar

    def withdraw(self, valor):
        if valor >= 0:
            if valor > self.balance:
                raise ValueError("saldo insuficiente")
            else:
                self.balance = int(self.balance - valor)
                return str(self.nome) + ' has ' + str(self.balance) + '.'

    def check(self, usuario, dinheiro):
        if dinheiro >= 0:
            if usuario.checking_account and usuario.balance > dinheiro:
                self.balance = int(self.balance + dinheiro)
                usuario.balance = int(usuario.balance - dinheiro)
                return str(self.nome) + ' has ' + str(self.balance) + ' and ' + str(usuario.nome) + ' has ' + str(usuario.balance) + '.'
            else:
                raise ValueError

    def add_cash(self, valor):
        if valor >= 0:
            self.balance = int(self.balance + valor)
            return str(self.nome) + ' has ' + str(self.balance) + '.'
