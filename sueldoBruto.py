class SueldoBruto():

    def __init__(self,antiguedad,horas_N, horas_E, horas_F) -> None:
        self.sueldoBasico = 139731
        self.antiguedad = antiguedad
        self.horas_nocturnas = horas_N
        self.horas_extras = horas_E
        self.feriado = horas_F
        self.presentismo = 16500

    def calcular_antiguedad(self):
        calculo = self.antiguedad * 1397.31
        return calculo

    def calcular_horas_nocturnas(self):
        calculo = self.horas_nocturnas * 160.42
        return calculo
    
    def calcular_horas_extras(self):
        calculo = self.horas_extras * 1203.17
        return calculo 
    
    def calcular_horas_feriado(self):
        calculo = self.feriado * 698.6
        return calculo
   
    def suma_total_de_argumentos(self):
        metodo1 = self.calcular_antiguedad()
        metodo2 = self.calcular_horas_nocturnas()
        metodo3 = self.calcular_horas_extras()
        metodo4 = self.calcular_horas_feriado()
        resultado = metodo1 + metodo2 + metodo3 + metodo4
        return resultado 
    
    def suma_total_final(self):
        viatico = 25000
        suma_no_renum = 37000

        resultado1 = self.sueldoBasico + self.presentismo + viatico + suma_no_renum
        resultado2 = self.suma_total_de_argumentos()
        resultado_final = resultado1 + resultado2
        return resultado_final




