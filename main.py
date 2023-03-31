#%% Imports
from find_root import find_root
from sympy import sqrt, sin, cos

#%% Earth's parameters
Ts0 = 288.15#K
Ps0 = 101325#Pa


#%% Flight parameters formulas
def Ps(dic):
    """
    Static pressure at altitude H
    """
    H = dic['H']
    return Ps0 * (1-22.557e-6 * H)**(5.256)
    
def Ts(dic):
    """
    Temperature at altitude H
    """
    H = dic['H']
    return Ts0 - (6.5e-6 * H)

def F0(dic):
    """
    Thrust from maximum take off weight MTOW
    """
    MTOW = dic['MTOW']
    return 14.275 * MTOW**(0.868)

def M_fuel(dic):
    """
    Maximal fuel quantity from maximum take off weight MTOW
    """
    MTOW = dic['MTOW']
    return 574e-9 * MTOW**2 + 287e-3 * MTOW

def F(dic):
    """
    Thrust variation from altitude H, local mach number M0 and static pressure.
    Requires Ps and F0 to have already been computed
    """
    H,M0,Ps,F0 = dic['H'],dic['M0'],dic['Ps'],dic['F0']
    sigma = Ps / Ps0
    return F0 * (0.568 + 0.25 * (1.2 - M0)**3) * sigma**0.6

def Cs(dic):
    """
    Specific fuel consumption variation from altitude H, local mach number M0
    Requires Ts to have already been computed
    """
    H,M0,Cs0,Ts = dic['H'],dic['M0'],dic['Cs0'],dic['Ts']
    return Cs0 * sqrt(Ts/Ts0) * (1+M0)



#%% Flight Parameters

if __name__ == '__main__':
    # Fill with all the available parameters
    _H = None # TO FILL --- Altitude
    _Ps = None # TO FILL --- Static pressure at current FL
    _Ts = None # TO FILL --- Temperature at current FL
    _MTOW = None # TO FILL --- Max take-off weight
    _F0 = None # TO FILL --- Maximum thrust
    _M_fuel = None # TO FILL --- Maximum fuel quantity
    _M0 = None # TO FILL --- Local mach number
    _F = None # TO FILL --- Thrust variation
    _Cs0 = None # TO FILL --- Thrust specific fuel consumption
    _Cs = None # TO FILL --- Thrust specific fuel consumption variation
    
    
    # Comment-out the parameters that already have a value
    _H = find_root(Ps, _Ps, **{'H' : _H})
    _Ps = find_root(Ps, _Ps, **{'H' : _H})
    _Ts = find_root(Ts, _Ts, **{'H' : _H})
    _MTOW = find_root(F0, _F0, **{'MTOW' : _MTOW})
    _F0 = find_root(F0, _F0, **{'MTOW' : _MTOW})
    _M_fuel = find_root(M_fuel, _M_fuel, **{'MTOW' : _MTOW})
    _M0 = find_root(F, _F, **{'H' : _H, 'M0': _M0, 'Ps': _Ps, 'F0': _F0})
    _F = find_root(F, _F, **{'H' : _H, 'M0': _M0, 'Ps': _Ps, 'F0': _F0})
    _Cs0 = find_root(Cs, _Cs, **{'H' : _H, 'M0': _M0, 'Cs0': _Cs0, 'Ts': _Ts})
    _Cs = find_root(Cs, _Cs, **{'H' : _H, 'M0': _M0, 'Cs0': _Cs0, 'Ts': _Ts})
    
    
    # Print of the result
    flight_parameters = {
        'H':_H,
        'Ps':_Ps,
        'Ts':_Ts,
        'MTOW':_MTOW,
        'F0':_F0,
        'M_fuel':_M_fuel,
        'M0':_M0,
        'F':_F,
        'Cs0':_Cs0,
        'Cs':_Cs
        }
    print(flight_parameters)







#%% Flight Geometry formulas












