class remotecontrol:
    def __init__(self, device):
        self.device = device

    def turn_on(self):
        return self.device.turn_on()

    def turn_off(self):
        return self.device.turn_off()

    def channel_change(self):
        return self.device.channel_change()

# class Device:
#     def turn_on(self):
#         pass

#     def turn_off(self):
#         pass

#     def channel_change(self):
#         pass

class TV():
    def turn_on(self):
        return 'Turning on the Tv'
    
    def turn_off(self):
        return 'Turnimg off the Tv'
    
    def channel_change(self):
        return 'Changing channel of Tv'
    
class radio():
    def turn_on(self):
        return 'Turning on the Radio'
    
    def turn_off(self):
        return 'Turnimg off the Radio'
    
    def channel_change(self):
        return 'Changing channel of radio'
    
tv_instance = TV()
remote_tv = remotecontrol(tv_instance)
print(remote_tv.turn_on())


