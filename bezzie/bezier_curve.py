# -*- coding: utf-8 -*-
def _eval(control_points, t):
    if len(control_points) > 1:
        new_points = []
        for i in range(len(control_points)-1):
            x0 = control_points[i][0]
            x1 = control_points[i+1][0]
            y0 = control_points[i][1]
            y1 = control_points[i+1][1]
            xt = x0 + t * (x1 - x0)
            yt = y0 + t * (y1 - y0)
            new_points.append([xt, yt])
        return _eval(new_points, t)

    else:
        return control_points

def bezier_curve(control_points, t):
    '''Construct and evaluate a two-dimensional, n-order Bezier curve from n+1
    control points and t value from 0. - 1. that represents a fraction between the
    endpoints.

    ::
        >> control_points = [[0, 0],[50, 100],[100, 0]]
        >> bezier_curve(control_points, 0.25)
        [[75.0, 112.5]]

    Returns an interpolated point at t.
    '''
    point = _eval(control_points, t)
    return point[0]
