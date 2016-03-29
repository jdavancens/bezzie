# Bezzie 
Bezzie is a set of tools for creating paths in two dimensions consisting of Bezier curves of arbitrary order.
## Install
* Download the source code
* run:
```
sudo python setup.py install
```
## Example
Construct a path with two second-order (quadratic) Bezier curves.
```
>>> from bezzie import *
>>> b0 = BezierCurve((0, 0), (50, 100), (100, 0))
>>> b2 = BezierCurve((100, 0), (200, -100), (300, 0))
>>> p = Path(b0, b1)
>>> x = 225
>>> p(x0)
-46.875
