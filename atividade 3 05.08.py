class veiculo:
    def __init__(self, marca, modelo,ano, valor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"O {self.marca} {self.modelo} foi ligado")

    def desligar(self):
        self.ligado = False
        print(f"O {self.marca} {self.modelo} foi desligado")

    def info(self):
        status = "ligado" if self.ligado else "desligado"
        print(f"Marca: {self.marca}  Modelo: {self.modelo} Ano: {self.ano}, valor: R$ {self.valor:.2f}, Status: {status}")

    def calcular_imposto(self):
        pass

    

    class carro:
        def __init__(self, marca, modelo,ano, valor):
            veiculo.__init__(self, marca, modelo,ano, valor)

        def calcular_imposto(self):
            imposto = self.valor  * 0.015
            print(f"o imposto do carro {self.marca} {self.modelo} é de {imposto:.2f}")

        def info(self):
            status = "ligado" if self.ligado else "desligado"
            print(f"Marca: {self.marca}  Modelo: {self.modelo} Ano: {self.ano}, valor: R$ {self.valor:.2f}, Status: {status}")

    class moto:
        def __init__(self, marca, modelo,ano, valor):
            veiculo.__init__(self, marca, modelo,ano, valor)
   
        def calcular_imposto(self):
            imposto = self.valor * 0.012
            print(f"o imposto da moto {self.marca} {self.modelo} é de R${imposto:.2f}")

        def info(self):
            status = "ligado" if self.ligado else "desligado"
            print(f"Marca: {self.marca}  Modelo: {self.modelo} Ano: {self.ano}, valor: R$ {self.valor:.2f}, Status: {status}")


x = veiculo.carro("BMW", "BMW, xDrive60 M sport ", 2024,  1321.000)

x.calcular_imposto()
x.info()


y = veiculo.moto("Kawasaki", "Ninja 650", 2024, 49500.00)

y.calcular_imposto()
y.info()