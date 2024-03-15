def voyager(days):
    start_dist = 24042369103
    velocity = 16.9995
    seconds = days*24*60*60
    distance = start_dist+velocity*seconds
    lightspeed = 299792.458
    return 2*distance/lightspeed
