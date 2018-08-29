import Device

device = Device.Particle('340055000f51353532343635', '034a7e5d14e8d1af0be253f67c69a28e1312e262')

def test():
    device.digitalRead("D0")

if __name__ == "__main__":
    test()
