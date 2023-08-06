from sueldoBruto import SueldoBruto
from sueldoNeto import sueldoNeto

def main():
    sueldo = SueldoBruto(3,134,36,22)
    print("Sueldo Bruto:",sueldo.suma_total_final())
    r = sueldoNeto(3,134,36,22)
    print("Sueldo Neto:",round(r.descuento_final(),2))

main()