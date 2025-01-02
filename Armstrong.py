def main():
    Armstrong()

class Armstrong:
    def __init__(self):
        print("digite um numero para ver se e um numero de Armstrong");self.number = int(input())
        self.split_num()
        self.is_armstrong()
        
    def split_num(self):
        self.confirmation = self.number
        self.number = str(self.number)
        self.number = [int(i) for i in self.number]
        
    def is_armstrong(self):
        potencia = len(self.number)
        soma = 0
        for i in range(len(self.number)):
            soma += self.number[i]**potencia
        
        if soma == int(self.confirmation):
            print("e um numero de Armstrong")
        else:
            print("nao e um numero de Armstrong")
    
        
        
if __name__ == "__main__":
    main()
