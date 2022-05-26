
class BoardSquare():
    
    def __init__(self,value):
        self.value = value #El value puede ser ' ', 'N' o 'S'
        #Se agregan valores booleanos a cada lado del cuadrado para
        #saber si el peón se puede mover hacia ese lado
        self.topBorder = True
        self.rightBorder = True
        self.botBorder = True
        self.leftBorder = True