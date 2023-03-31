# Flight Parameters
Quick tool to compute the flight parameters of an airplane using limited amounts of data.


## User guide
Head to the main.py file, starting at the Flight Parameters section.
The instructions are given in the comments:
  - Replace all the "None" with known values then head to the find_root function calls.
  - Comment-out all the variables for which a value is already attributed.
  - Run the code.

If there is more than one unknown, you may end up with:
> TypeError: unsupported operand type(s) for -: 'Mul' and 'NoneType'

A quick fix for this exception: Don't end up with more than one unknown.

In a common function call, the variables (and potential unknowns) are: _M0 = find_root(F, ***_F***, **{'H' : ***_H***, 'M0': ***_M0***, 'Ps': ***_Ps***, 'F0': ***_F0***})

#### If you encounter any issue when running the code, please notify me so I can try to patch it.
