import smbus
import time

# MPU6050 Registers
MPU6050_ADDR = 0x68
PWR_MGMT_1   = 0x6B
ACCEL_XOUT_H = 0x3B

bus = smbus2.SMBus(1)

def read_word(reg):
    high = bus.read_byte_data(MPU6050_ADDR, reg)
    low = bus.read_byte_data(MPU6050_ADDR, reg + 1)
    value = (high << 8) + low
    if value >= 0x8000:
        value = -((65535 - value) + 1)
    return value

# Wake up the MPU6050
bus.write_byte_data(MPU6050_ADDR, PWR_MGMT_1, 0)

print("Reading MPU6050 values...\n")

while True:
    # Accelerometer
    ax = read_word(ACCEL_XOUT_H)
    ay = read_word(ACCEL_XOUT_H + 2)
    az = read_word(ACCEL_XOUT_H + 4)

    # Temperature
    temp_raw = read_word(ACCEL_XOUT_H + 6)
    temp_c = (temp_raw / 340.0) + 36.53

    # Gyroscope
    gx = read_word(ACCEL_XOUT_H + 8)
    gy = read_word(ACCEL_XOUT_H + 10)
    gz = read_word(ACCEL_XOUT_H + 12)

    print("Accelerometer:")
    print(f"  AX = {ax}")
    print(f"  AY = {ay}")
    print(f"  AZ = {az}")

    print("Gyroscope:")
    print(f"  GX = {gx}")
    print(f"  GY = {gy}")
    print(f"  GZ = {gz}")

    print(f"Temperature: {temp_c:.2f} °C")
    print("-" * 40)

    time.sleep(0.5)
