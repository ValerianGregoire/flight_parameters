#%% Imports
from find_root import find_root
from sympy import sqrt, sin, cos

#%% Earth parameters
Ts0 = 288.15#K
Ps0 = 101325#Pa
g = 9.81#m.s**-2


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

def rho(dic):
    """
    Air density at static pressure Ps and temperature T
    """
    Ps,Ts = dic['Ps'],dic['Ts']
    return Ps / (287.05*Ts)

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
    Thrust variation from local mach number M0 and static pressure Ps.
    Requires Ps and F0 to have already been computed
    """
    M0,Ps,F0 = dic['M0'],dic['Ps'],dic['F0']
    sigma = Ps / Ps0
    return F0 * (0.568 + 0.25 * (1.2 - M0)**3) * sigma**0.6

def Cs(dic):
    """
    Specific fuel consumption variation from altitude H, local mach number M0
    Requires Ts to have already been computed
    """
    M0,Cs0,Ts = dic['M0'],dic['Cs0'],dic['Ts']
    return Cs0 * sqrt(Ts/Ts0) * (1+M0)


#%% Flight Geometry & Flight Characteristics formulas
def OP_weight(dic):
    """
    Operating weight of the aircraft from its mass.
    """
    m = dic['m']
    return m*g

def Cx_max(dic):
    """
    Drag coefficient from Cz
    """
    Cz_max = dic['Cz_max']
    return 0.0295 + 0.035*Cz_max**2

def V_stall(dic):
    """
    Stall speed from mass m, air density rho, wing surface S and max lift coef
    Cz_max.
    """
    m,rho,S,Cz_max = dic['m'],dic['rho'],dic['S'],dic['Cz_max']
    return sqrt(2*m*g / (rho*S*Cz_max))

def TO_dist(dic):
    """
    Take off distance from thrust F, mass m, ground friction coef and take off
    duration TO_time.
    """
    m,F,mu,TO_time = dic['m'],dic['F'],dic['mu'],dic['TO_time']
    return (F / m - mu * g)* TO_time**2/2

def V1(dic):
    """
    Decision speed from stall speed V_stall.
    """
    V_stall = dic['V_stall']
    return 1.05 * V_stall

def VR(dic):
    """
    Rotation speed from stall speed V_stall.
    """
    V_stall = dic['V_stall']
    return 1.1 * V_stall

def V2(dic):
    """
    Take off speed from stall speed V_stall.
    """
    V_stall = dic['V_stall']
    return 1.2 * V_stall

#%% Sections to run
flight_parameters = True
flight_characteristics = True # WIP

#%% Main
if __name__ == '__main__':
    
    if flight_parameters or flight_characteristics:
        # Fill with all the available parameters
        _H = 0 # TO FILL --- Altitude
        _Ps = None # TO FILL --- Static pressure at current FL
        _Ts = None # TO FILL --- Temperature at current FL
        _rho = None # TO FILL --- Air density at current conditions
        _MTOW = 299640 # TO FILL --- Max take-off weight
        _F0 = 2*436466 # TO FILL --- Maximum thrust
        _M_fuel = 137516 # TO FILL --- Maximum fuel quantity
        _M0 = None # TO FILL --- Local mach number
        _F = None # TO FILL --- Thrust variation
        _Cs0 = 1.035e-5 # TO FILL --- Thrust specific fuel consumption
        _Cs = None # TO FILL --- Thrust specific fuel consumption variation
        
        
        # Comment-out the parameters that don't need to be computed
        # _H = find_root(Ps, _Ps, **{'H' : _H})
        _Ps = find_root(Ps, _Ps, **{'H' : _H})
        _Ts = find_root(Ts, _Ts, **{'H' : _H})
        _rho = find_root(rho, _rho, **{'Ps' : _Ps, 'Ts':_Ts})
        # _MTOW = find_root(F0, _F0, **{'MTOW' : _MTOW})
        # _F0 = find_root(F0, _F0, **{'MTOW' : _MTOW})
        # _M_fuel = find_root(M_fuel, _M_fuel, **{'MTOW' : _MTOW})
        # _M0 = find_root(F, _F, **{'H' : _H, 'M0': _M0, 'Ps': _Ps, 'F0': _F0})
        # _F = find_root(F, _F, **{'H' : _H, 'M0': _M0, 'Ps': _Ps, 'F0': _F0})
        # _Cs0 = find_root(Cs, _Cs, **{'H' : _H, 'M0': _M0,
        #                              'Cs0': _Cs0, 'Ts': _Ts})
        # _Cs = find_root(Cs, _Cs, **{'H' : _H, 'M0': _M0,
        #                             'Cs0': _Cs0, 'Ts': _Ts})
        
        
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
        print(f"Flight parameters:\n{flight_parameters}")


    if flight_characteristics:
        # Fill with all the available parameters
        _f_length = 63.73 # TO FILL --- Fuselage length
        _f_width = 6.2 # TO FILL --- Fuselage width
        _a_height = 18.29 # TO FILL --- Aircraft height
        _wingspan = 60.93 # TO FILL --- Wingspan
        _S = 427.8 # TO FILL --- Wing Surface
        _skew_angle = 32 # TO FILL --- Skew angle
        _Cz_max = 2 # TO FILL --- Max lift coefficient
        _Cx_max = None # TO FILL --- Max drag coefficient
        _passengers = 365 # TO FILL --- Number of passengers
        _m = 299640 # TO FILL --- Mass of the aircraft
        _op_weight = None # TO FILL --- Operating weight
        _MLW = 237896 # TO FILL --- Maximum Landing Weight
        _fuel_capacity = None # TO FILL --- Fuel capacity
        _mu = None  # TO FILL --- Ground coef of friction (0.02 RWY, 0.1 grass)
        _cruise_spd = 0.84 # TO FILL --- Cruise speed
        _max_cruise_spd = 0.89 # TO FILL --- Maximum cruise speed
        _V1 = None # TO FILL --- Decision speed
        _V2 = None # TO FILL ---  Take off speed
        _VR = None # TO FILL --- Rotation speed
        _V_stall = None # TO FILL --- Stall speed
        _TO_time = None # TO FILL --- Take off duration
        _TO_dist = None # TO FILL --- Take off distance (approximated)
        _range = 11133 # TO FILL --- Range
        _ceiling = 13136 # TO FILL --- Service ceiling
        
        
        # Comment-out the parameters that don't need to be computed
        # _f_length = find_root() --- NO FORMULA YET
        # _f_width = find_root() --- NO FORMULA YET
        # _a_height = find_root() --- NO FORMULA YET
        # _wingspan = find_root() --- NO FORMULA YET
        #_S = find_root(V_stall, _V_stall, **{'m' : _m,'rho' : _rho,
        #                                           'S' : _S,'Cz_max' :_Cz_max})
        # _skew_angle = find_root() --- NO FORMULA YET
        #_Cz_max = find_root(V_stall, _V_stall, **{'m' : _m,'rho' : _rho,
        #                                           'S' : _S,'Cz_max' :_Cz_max})
        _Cx_max = find_root(Cx_max, _Cx_max, **{'Cz_max':_Cz_max})
        # _passengers = find_root() --- NO FORMULA YET
        #_m = find_root(OP_weight, _op_weight, **{'m' : _m})
        _op_weight = find_root(OP_weight, _op_weight, **{'m' : _m})
        # _MLW = find_root() --- NO FORMULA YET
        # _fuel_capacity = find_root() --- NO FORMULA YET
        # _mu = find_root(TO_dist, _TO_dist, **{'m' : _m,'F' : _F,
        #                                       'mu' : _mu,'TO_time' : _TO_time})
        # _cruise_spd = find_root() --- NO FORMULA YET
        # _max_cruise_spd = find_root() --- NO FORMULA YET
        _V_stall = find_root(V_stall, _V_stall, **{'m' : _m,'rho' : _rho,
                                                   'S' : _S,'Cz_max' :_Cz_max})
        _V1 = find_root(V1, _V1, **{'V_stall' : _V_stall})
        _V2 = find_root(V2, _V2, **{'V_stall' : _V_stall})
        _VR = find_root(VR, _VR, **{'V_stall' : _V_stall})
        # _TO_time = find_root(TO_dist, _TO_dist, **{'m' : _m,'F' : _F,
        #                                       'mu' : _mu,'TO_time' : _TO_time})
        # _TO_dist = find_root(TO_dist, _TO_dist, **{'m' : _m,'F' : _F,
        #                                       'mu' : _mu,'TO_time' : _TO_time})
        # _range = find_root() --- NO FORMULA YET
        # _ceiling = find_root() --- NO FORMULA YET
        
        
        
        flight_characteristics = {
            'f_length':_f_length,
            'f_width':_f_width,
            'a_height':_a_height, 
            'wingspan':_wingspan,
            'S':_S,
            'skew_angle':_skew_angle,
            'max lift coef':_Cz_max,
            'drag coef':_Cx_max,
            'passengers':_passengers,
            'm':_m,
            'op_weight':_op_weight,
            'MLW':_MLW,
            'fuel_capacity':_fuel_capacity,
            'mu':_mu,
            
            'cruise_spd':_cruise_spd,
            'max_cruise_spd':_max_cruise_spd,
            'V1':_V1,
            'V2':_V2,
            'VR':_VR,
            'V_stall':_V_stall,
            'TO_time':_TO_time,
            'TO_dist':_TO_dist,
            'range':_range,
            'ceiling':_ceiling,
            }
    
        print(f"Flight characteristics:\n{flight_characteristics}")

