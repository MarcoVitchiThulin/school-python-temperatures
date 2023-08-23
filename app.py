import re # importera RegEx

scale = "C"
scale_name = "celsius"

pattern_scales = re.compile(r'/([CKF])/gi') # Definiera RegEx pattern för C/K/F
pattern_numbers = re.compile(r'^\d+$') # Definiera RegEx pattern för tal

ce = 1
ke = 273.15
fa = 33.8

def convert(temp):
    match scale: # Inte särskilt välskriven, men gör sitt jobb
        case "C":
            temp_c = temp
            temp_k = temp * ke
            temp_f = temp * fa
        case "K":
            temp_c = temp - ke
            temp_k = temp
            temp_f = temp_c * fa
        case "F":
            temp_c = 5/9*(temp-32)
            temp_k = temp_c * ke
            temp_f = temp
    return str(temp_c), str(temp_k), str(temp_f)

def main():
    while True:
        command = input("C/K/F eller temperatur: ")
        if pattern_scales.findall(command):  # Använd RegEx för att kolla om command är C, K eller F
            match command:  # Byt skala
                case "C":
                    print("Byter till Celsius.")
                    scale = "C"
                case "K":
                    print("Byter till Kelvin.")
                    scale = "K"
                case "F":
                    print("Byter till Farenheit")
                    scale = "F"
        if pattern_numbers.findall(command): # Använd RegEx för att kolla om command är ett tal
            c, k, f = convert(float(command))
            print("Celsius: "+c)
            print("Kelvin: "+k)
            print("Farenheit: "+f)
        else:
            print("Ogiltligt kommando: "+command)

if __name__ == "__main__":
    main()