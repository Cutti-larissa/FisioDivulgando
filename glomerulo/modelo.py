class Glomerulo:

    def __init__(self):

        # valores de referência
        self.Qa = 125       # nL/min
        self.deltaP = 40    # mmHg
        self.Kf = 0.08
        self.proteina = 7   # g/dL


    def pressao_oncotica(self):

        # relação aproximada de Starling
        return 25 * (self.proteina / 7)


    def calcular_peuf(self):

        pi = self.pressao_oncotica()

        return self.deltaP - pi



    def calcular_fpn(self):

        peuf = self.calcular_peuf()

        if peuf <= 0:
            return 0

        # efeito do fluxo plasmático
        efeito_Qa = (self.Qa / 125)**0.3

        return self.Kf * peuf * efeito_Qa



    def resetar(self):

        self.Qa = 125
        self.deltaP = 40
        self.Kf = 0.08
        self.proteina = 7