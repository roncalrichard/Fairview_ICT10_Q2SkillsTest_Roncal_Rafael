from pyscript import document, display


nonmetals = {
    'H':  {'name': 'Hydrogen',   'num': 1,  'mass': '1.008 u'},
    'He': {'name': 'Helium',     'num': 2,  'mass': '4.0026 u'},
    'C':  {'name': 'Carbon',     'num': 6,  'mass': '12.011 u'},
    'N':  {'name': 'Nitrogen',   'num': 7,  'mass': '14.007 u'},
    'O':  {'name': 'Oxygen',     'num': 8,  'mass': '15.999 u'},
    'F':  {'name': 'Fluorine',   'num': 9,  'mass': '18.998 u'},
    'Ne': {'name': 'Neon',       'num': 10, 'mass': '20.180 u'},
    'P':  {'name': 'Phosphorus', 'num': 15, 'mass': '30.974 u'},
    'S':  {'name': 'Sulfur',     'num': 16, 'mass': '32.06 u'},
    'Cl': {'name': 'Chlorine',   'num': 17, 'mass': '35.45 u'},
    'Ar': {'name': 'Argon',      'num': 18, 'mass': '39.948 u'},
    'Se': {'name': 'Selenium',   'num': 34, 'mass': '78.971 u'},
    'Br': {'name': 'Bromine',    'num': 35, 'mass': '79.904 u'},
    'Kr': {'name': 'Krypton',    'num': 36, 'mass': '83.798 u'},
    'I':  {'name': 'Iodine',     'num': 53, 'mass': '126.90 u'},
    'Xe': {'name': 'Xenon',      'num': 54, 'mass': '131.29 u'},
    'Rn': {'name': 'Radon',      'num': 86, 'mass': '222 u'}
}

def nonmetal_checker(event):

    input_symbol = document.getElementById("element").value.strip()
    

    formatted_symbol = input_symbol.capitalize() if len(input_symbol) <= 2 else input_symbol

    if formatted_symbol in nonmetals:
        element_data = nonmetals[formatted_symbol]
        
  
        display(formatted_symbol, target="out_symbol")
        display(element_data['name'], target="out_name")
        display(str(element_data['num']), target="out_num")
        display(element_data['mass'], target="out_mass")
        display("", target="error_message") 
    else:

        display("-", target="out_symbol")
        display("-", target="out_name")
        display("-", target="out_num")
        display("-", target="out_mass")
        display(f"'{input_symbol}' this is not a nonmetal symbol >:(.", target="error_message")