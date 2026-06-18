class Glomerulo:

    def __init__(self):
        # valores de referência aproximados
        self.Qa = 125       # fluxo plasmático glomerular (nL/min)
        self.deltaP = 40    # diferença de pressão hidrostática (mmHg)
        self.Kf = 0.08      # coeficiente de filtração
        self.proteina = 7   # concentração plasmática (g/dL)


    def pressao_oncotica(self):
        """
        Pressão oncótica do plasma.
        Simplificação proporcional à concentração de proteínas.
        """

        pi = 25 * (self.proteina / 7)

        return pi


    def calcular_peuf(self):
        """
        Pressão efetiva de ultrafiltração

        Peuf = ΔP - π
        """

        return self.deltaP - self.pressao_oncotica()


    def calcular_fpn(self):
        """
        Taxa de filtração por néfron

        FPN = Kf * Peuf * efeito(Qa)
        """

        peuf = self.calcular_peuf()

        if peuf <= 0:
            return 0

        # efeito simplificado do fluxo plasmático
        efeito_Qa = (self.Qa / 125) ** 0.3

        return self.Kf * peuf * efeito_Qa