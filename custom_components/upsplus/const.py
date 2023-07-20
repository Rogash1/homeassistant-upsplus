"""All constants for the integration"""
DOMAIN = "upsplus"
DEVICE_ADDR = 0x17
DEVICE_BUS = 1

UPS_ID = "5t89t8th-7g45-jf93-c8534c97ejf9"

BUTTONS = [
    {
        "name": "Cancel shutdown",
        "entry_id": "cancel_shutdown",
        "address": 0x18,
        "value": 0x00
    },
    {
        "name": "Cancel restart",
        "entry_id": "cancel_restart",
        "address": 0x1A,
        "value": 0x00
    },
    {
        "name": "Restore factory settings",
        "entry_id": "restore_factory_settings",
        "address": 0x1B,
        "value": 0x01
    },
    {
        "name": "Enter OTA",
        "entry_id": "enter_ota",
        "address": 0x32,
        "value": 0x7F
    },
]

SENSOR_LIST = {
    "supply_voltage": {
        "subfix": "voltage",
        "name": "UPS supply voltage",
        "unit_of_measurement": "V",
        "multiplier": 1,
        "class": "voltage",
        "prefix": "supply"
    },
    "supply_current": {
        "subfix": "current",
        "name": "UPS supply current",
        "unit_of_measurement": "A",
        "class": "current",
        "prefix": "supply"
    },
    "supply_power": {
        "subfix": "power",
        "name": "UPS supply power",
        "unit_of_measurement": "W",
        "class": "power",
        "prefix": "supply"
    },
    "battery_voltage": {
        "subfix": "voltage",
        "name": "UPS battery voltage",
        "unit_of_measurement": "V",
        "multiplier": 1,
        "class": "voltage",
        "prefix": "battery"
    },
    "battery_current": {
        "subfix": "current",
        "name": "UPS battery current input",
        "unit_of_measurement": "A",
        "multiplier": -0.001,
        "class": "current",
        "prefix": "battery"
    },
    "battery_power": {
        "subfix": "power",
        "name": "UPS battery power input",
        "unit_of_measurement": "W",
        "class": "power",
        "prefix": "battery"
    }
}

# The registermap of the UPS can be found in the product wiki
# https://wiki.52pi.com/index.php?title=EP-0136#Register_Mapping
SENSOR_LIST_SMBUS = {
    "processor_voltage": {
        "name": "UPS processor voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x01,0x02]
    },
    "pi_report_voltage": {
        "name": "UPS pi report voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x03,0x04]
    },
    "input_report_voltage": {
        "name": "UPS input report voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x05,0x06]
    },
    "type_c_voltage": {
        "name": "UPS Type C voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x07,0x08]
    },
    "micro_usb_voltage": {
        "name": "UPS Micro USB voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x09,0x0A]
    },
    "battery_temperature": {
        "name": "UPS battery temperature",
        "unit_of_measurement": "°C",
        "class": "temperature",
        "index": [0x0B,0x0C]
    },
    "battery_full_voltage": {
        "name": "UPS battery full voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x0D,0x0E]
    },
    "battery_empty_voltage": {
        "name": "UPS battery empty voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x0F,0x10]
    },
    "battery_protection_voltage": {
        "name": "UPS battery protection voltage",
        "unit_of_measurement": "V",
        "class": "voltage",
        "index": [0x11,0x12]
    },
    "battery_capacity": {
        "name": "UPS battery capacity",
        "unit_of_measurement": "%",
        "class": "battery",
        "index": [0x13,0x14]
    },
    "sampling_period": {
        "name": "UPS sampling period",
        "unit_of_measurement": "min",
        "class": "duration",
        "index": [0x15,0x16]
    },
    "shutdown_timer": {
        "name": "UPS shutdown countdown",
        "unit_of_measurement": "s",
        "class": "duration",
        "index": [0x18]
    },
    "restart_timer": {
        "name": "UPS restart countdown",
        "unit_of_measurement": "s",
        "class": "duration",
        "index": [0x1A]
    },
    "all_running_time": {
        "name": "UPS accumulated running time",
        "unit_of_measurement": "s",
        "class": "duration",
        "index": [0x1C,0x1D,0x1E,0x1F]
    },
    "all_charged_time": {
        "name": "UPS accumulated charged time",
        "unit_of_measurement": "s",
        "class": "duration",
        "index": [0x20,0x21,0x22,0x23]
    },
    "running_time": {
        "name": "UPS running time",
        "unit_of_measurement": "s",
        "class": "duration",
        "index": [0x24,0x25,0x26,0x27]
    }
}
