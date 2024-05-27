class JogoDaVelha():
    def __init__(self):
        self.l1 = ["0","1","2"]
        self.l2 = ["3","4","5"]
        self.l3 = ["6","7","8"]


    def jogador1(self,val):
        if val == "0":
            self.l1[0] = "O"
        elif val == "1":
            self.l1[1] = "O"
        elif val == "2":
            self.l1[2] = "O"
        elif val == "3":
            self.l2[0] = "O"
        elif val == "4":
            self.l2[1] = "O"
        elif val == "5":
            self.l2[2] = "O"
        elif val == "6":
            self.l3[0] = "O"
        elif val == "7":
            self.l3[1] = "O"
        elif val == "8":
            self.l3[2] = "O"
            
    def jogador2(self,val):
        if val == "0":
            self.l1[0] = "X"
        elif val == "1":
            self.l1[1] = "X"
        elif val == "2":
            self.l1[2] = "X"
        elif val == "3":
             self.l2[0] = "X"
        elif val == "4":
             self.l2[1] = "X"
        elif val == "5":
             self.l2[2] = "X"
        elif val == "6":
             self.l3[0] = "X"
        elif val == "7":
             self.l3[1] = "X"
        elif val == "8":
             self.l3[2] = "X"
    
    def tabuleiro(self):
        print(self.l1)
        print(self.l2)
        print(self.l3)
     