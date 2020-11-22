import os
from time import sleep


class OnboardLeds:

    red_pwr = '/sys/class/leds/led1/brightness'
    green_act = '/sys/class/leds/led0/brightness'

    def __init__(self, color):
        self.color = color
        if self.color == 'red':
            self.color = OnboardLeds.red_pwr
        else:
            self.color = OnboardLeds.green_act
        
    def on(self):
        if self.color == OnboardLeds.red_pwr:
            self.state = '0'
        else:
            self.state = '1'
            
        return self._toggle()

    def off(self):
        if self.color == OnboardLeds.red_pwr:
            self.state = '1'
        else:
            self.state = '0'
            
        return self._toggle()
        
    def _toggle(self):
        return os.system('echo {} | sudo tee {} > /dev/null 2>&1'.format(self.state, self.color))

    def flash(self, flashes, duration=None, rest=None):
        for i in range(flashes):
            self.on()
            if duration is not None:
                sleep(duration)
            else:
                sleep(.2)
            self.off()
            if rest is not None:
                sleep(rest)
            else:
                sleep(.1)
                

red = OnboardLeds('red')
green = OnboardLeds('green')

#red.flash(3, rest=.3, duration=.3)
red.off()
green.off()
