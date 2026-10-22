# DS18B20 Temperature Sensors — 1-Wire on Raspberry Pi

Reads **four DS18B20 digital temperature sensors** on a single **1-Wire** bus and logs the readings every second to the console and a rotating log file. Built for monitoring a cellar.

## About the DS18B20

- Accuracy ±0.5 °C over most of the range, up to **12-bit** resolution
- Many sensors can share **one data pin**; each has a unique factory-programmed **64-bit ID**
- Works with 3.0–5.0 V systems

## How It Works

1. The Linux 1-Wire driver exposes each sensor at `/sys/bus/w1/devices/28-<id>/w1_slave`.
2. The script reads that file, waits for a valid CRC (`YES`) and parses `t=<millidegrees>`.
3. Temperatures T1–T4 are logged with timestamps through a logger that writes to both the console and a rotating file.

## Wiring

| DS18B20 pin | Raspberry Pi |
|-------------|--------------|
| VDD | 3.3 V |
| DQ (data) | GPIO 4 |
| GND | GND |

Add a **4.7 kΩ pull-up resistor** between DQ and 3.3 V.

## Usage

```bash
# Enable the 1-Wire interface
echo "dtoverlay=w1-gpio" | sudo tee -a /boot/config.txt
sudo reboot

ls /sys/bus/w1/devices/            # find your sensor IDs (28-xxxxxxxxxxxx)
# then set them in src/cave_temp-sensors_projects.py (path_temp1 … path_temp4)

sudo python3 src/cave_temp-sensors_projects.py
```

The log is written to `logs/sensorsTemp.log` by default. Set the `TEMP_SENSORS_LOG_FILE` environment variable to use a different path.

## Sample Log

```
2019-01-22 03:00:04,869 — main-temp-sensor — DEBUG — … — Temperature1: 24.375[°C]
2019-01-22 03:00:05,744 — main-temp-sensor — DEBUG — … — Temperature2: 23.312[°C]
2019-01-22 03:00:06,625 — main-temp-sensor — DEBUG — … — Temperature3: 24.125[°C]
2019-01-22 03:00:07,504 — main-temp-sensor — DEBUG — … — Temperature4: 23.187[°C]
```

A full run is in [`logs/sensorsTemp.log`](logs/sensorsTemp.log).

## Repository Structure

```
.
├── src/
│   ├── cave_temp-sensors_projects.py   # Reads the 4 sensors
│   └── lib_python_logging.py           # Console + rotating file logger
├── logs/                               # Sample log
└── requirements.txt
```

## Tech Stack

Python 3 · 1-Wire (w1-gpio) · DS18B20 · Linux sysfs · logging · Raspberry Pi

## Author

**Akram M'Tir**, [@amtir](https://github.com/amtir)
