"""All functions for reading data from the UPS"""
import smbus2
from ina219 import INA219
from .const import DEVICE_BUS, DEVICE_ADDR

class UPSManager:
    """Setup UPS for all sensors"""
    _instance = None

    def __new__(cls):
        """Only create instance if it doesn't already exist"""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        """initiate UPS operation"""
        self.ina_supply = INA219(0.00725, busnum=DEVICE_BUS, address=0x40)
        self.ina_supply.configure()
        self.ina_battery = INA219(0.005, busnum=DEVICE_BUS, address=0x45)
        self.ina_battery.configure()
        self.bus = smbus2.SMBus(DEVICE_BUS)
        self.sw_version = read_buff(self.bus,0x28,0x29)
        self.serial_number = read_buff(self.bus,0xF0,0xF1,0xF2,0xF3,0xF4,0xF5,0xF6,0xF7,0XF8,0xF9,0xFA,0xFB)

def read_buff(bus, index1, *args):
    """Function to read the SMBus and add all specified indexes"""
    result = bus.read_byte_data(DEVICE_ADDR, index1)
    i = 0
    for index in args:
        i += 1
        result = result | bus.read_byte_data(DEVICE_ADDR, index) << (8 * i)
    return result
