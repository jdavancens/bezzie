# Bezzie 
Bezzie is a set of tools for creating paths in two dimensions consisting of Bezier curves of arbitrary order.
## Install
* Download the source code
* run:
```
sudo python setup.py install
```
## Example
```
>>> from bezzie import *
>>> b0 = BezierCurve((0, 0), (100, 100), (200, 0))
>>> b2 = BezierCurve((200, 0), (300, -100), (400, 0))
>>> p = Path(b0, b1)
>>> x0 = 150
>>> x1 = 275
>>> p(x0)
75
>>> p(x1)
-80
