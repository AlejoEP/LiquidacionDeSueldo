from sueldoBruto import SueldoBruto

class sueldoNeto(SueldoBruto):
    
    def jubilacion(self):
        descuento_jubilacion = (self.suma_total_final() - self.viatico - self.suma_no_renum) * 0.11
        return descuento_jubilacion
    
    def ley_19032(self):
        descuento_ley = (self.suma_total_final() - self.viatico - self.suma_no_renum) * 0.03
        return descuento_ley
    
    def obra_social(self):
        descuento_obraSocial = (self.suma_total_final() - self.viatico - self.suma_no_renum) * 0.03
        return descuento_obraSocial
    
    def descuento_final(self):
        descuento_total = self.suma_total_final() - (self.jubilacion() + self.ley_19032() + self.obra_social())
        return descuento_total        
