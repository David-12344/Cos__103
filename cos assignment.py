print('equation for speed')
#speed = distance/time
distance = float(input('enter distance: '))
time = float(input('enter time: '))
speed = distance/time
print ('the value of speed is =', speed, 'm/s')

print('equation for velocity')
#velocity = displacement/time
displacement = float(input('enter displacement: '))
time = float(input('enter time: '))
velocity = displacement/time
print('the value of velocity is =', velocity, 'm/s')

print('equation for efficiency')
#efficiency = ma/vr*100
ma = float(input('enter mechanical advantage: '))
vr = float(input('enter velocity ratio: '))
efficiency = ma/vr*100
print('the efficiency of the machine is = ', efficiency, '%')

print('equation for mechanical advantage')
#ma = l/e
l = float(input('enter the weight of the load: '))
e = float(input('enter the effort exerted: '))
ma = l/e
print('the mechanical advantage is = ', ma, 'newton(N)')

print('equation for frequency')
#frequency = 1/T
T = float(input('enter the period of travel: '))
frequency = 1/T
print('the period of travel is = ', frequency, 'hertz(Hz)')
