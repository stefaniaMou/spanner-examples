import Device

device = Device.Particle('340055000f51353532343635', '034a7e5d14e8d1af0be253f67c69a28e1312e262')

def test():
    device.ota("/home/vagrant/spanner/BuildFactory/code/repositories/mike/b_AAyeIJlNz5BVEKLNSWjJ1rw3/mike_binary.bin")

if __name__ == "__main__":
    test()
