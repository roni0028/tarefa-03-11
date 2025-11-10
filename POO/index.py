# Classe Conta 
# Conta Corrente e Conta Poupança
# Atributos: numero, titular, saldo (Privados)
# O saldo deve ser protegido e acessado apenas por métodos
# A conta corrente possui limite de saque de R$ 500,00
# A conta poupança possui um método de render juros que aumenta o saldo em 5%

# metodos:
# depositar(valor)
# sacar(valor)
# exibir_saldo()

# Duas calsses herdadas (subclasses)
# ContaCorrente e ContaPoupanca
# ContaCorrente deve herdar de Conta e ter um limite de saque de R$ 500,00
# ContaPoupanca deve herdar de Conta e ter um método de render juros que aumenta o saldo em 5%

# Exemplo de saída: 
# Deposito de R$ 100,00 realizado para João
# Saque de R$ 200,00 realizado
# Saldo atual de R$ 800,00
# Saldo após rendimento: R$ 840,00
# Tentando sacar R$ 1000,00: Erro: Saldo insuficiente
# Tentando sacar R$ 600,00: Erro: Limite de saque excedido

# Implementar verificação para evitar que o saldo fique negativo

class Account: 
    def __init__(self, number, owner, balance): #construtor
        self.__number = number #atributo privado numero da conta
        self.__owner = owner #atributo privado titular da conta
        self.__balance = balance #atributo privado saldo da conta

    def deposit(self, amount): #metodo depositar 
        if amount > 0:
            self.__balance += amount
            print(f"Deposito de R$ {amount} realizado para {self.__owner}")
        else:
            print("Valor de deposito invalido")

    def withdraw(self, amount): #metodo sacar
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Saque de R$ {amount} realizado.")
            else:
                print("Saldo insuficiente")
        else:
            print("Valor de saque invalido")

    def get_balance(self): #metodo exibir saldo
        return self.__balance

    def __str__(self): #metodo para exibir a conta
        return f"Conta: {self.__number}, Titular: {self.__owner}, Saldo: R$ {self.__balance:.2f}"

class CurrentAccount(Account): #classe conta corrente 
    def __init__(self, number, owner, balance, limit): #construtor
        super().__init__(number, owner, balance) #herdando o construtor da classe Account
        self.__limit = limit #atributo privado limite de saque

    def withdraw(self, amount): #metodo sacar
        if amount > 0: 
            if amount <= self.__limit:
                super().withdraw(amount) 
            else:
                print("Limite de saque excedido")
        else:
            print("Valor de saque invalido")

    def __str__(self): #metodo para exibir a conta
        return f"Conta Corrente: {super().__str__()}, Limite: R$ {self.__limit:.2f}"

class SavingsAccount(Account): #classe conta poupança
    def __init__(self, number, owner, balance): #construtor
        super().__init__(number, owner, balance) #herdando o construtor da classe Account

    def add_interest(self): #metodo de render juros
        interest = self.__balance * 0.05
        self.__balance += interest
        print(f"Rendimento de R$ {interest:.2f} aplicado.")

    def __str__(self): #metodo para exibir a conta
        return f"Conta Poupança: {super().__str__()}"

# Teste do programa
if __name__ == "__main__":

    conta1 = CurrentAccount(1, "João", 1000, 500)
    conta2 = SavingsAccount(2, "Maria", 1000)

    print(conta1)
    print(conta2)

    conta1.deposit(100)
    conta2.deposit(100)

    print(conta1)
    print(conta2)

    conta1.withdraw(200)
    conta2.withdraw(200)

    print(conta1)
    print(conta2)
    
    conta1.withdraw(1000)