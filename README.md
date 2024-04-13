## UART Data Exchange Firmware

Welcome to the **UART Data Exchange Firmware** repository! This firmware facilitates seamless bidirectional communication between a personal computer (PC) and a microcontroller unit (MCU) using UART (Universal Asynchronous Receiver-Transmitter) communication. Whether you're a seasoned developer or just diving into the world of embedded systems, this firmware has you covered.

### Overview

1. **Python Script (PC_side_code.py)**
   - This Python script establishes communication with the Arduino Uno by transmitting text data character by character.
   - It also provides real-time feedback on data transmission and reception speeds, measured in bits per second.

2. **Arduino Sketch (MCU_side_code.ino)**
   - The MCU_Receiver sketch runs on the Arduino Uno.
   - It receives data from the PC via the serial port and efficiently stores it in the onboard EEPROM (Electrically Erasable Programmable Read-Only Memory).
   - It sends back the stored data to the PC.

### Contents

#### 1. PC_side_code
- **Description**: This directory contains the PC-side code responsible for initiating data transmission and displaying received data on the console.
- **Main File**: `PC_side_code.py`

#### 2. MCU_side_code
- **Description**: Here lies the MCU firmware code, written in Embedded C/C++.
- **Main File**: `MCU_side_code.ino`

### Requirements

To get started, ensure you have the following:

1. **Python 3.x**: Make sure Python is installed on your PC.
2. **Arduino Uno or Compatible Board**: You'll need an Arduino Uno or a similar development board.
3. **USB Cable**: Use a USB cable to connect the Arduino Uno to your PC.
4. **USB to UART Converter**: If your PC lacks a native UART interface, grab a USB to UART converter.

### Usage Instructions

1. **Hardware Setup**:
   - Connect the Arduino Uno to your PC via USB.
   - Upload the `MCU_side_code.ino` sketch to the Arduino Uno.

2. **Software Execution**:
   - Run the `PC_side_codde.py` script on your PC.
   - Ensure that the correct COM port for the Arduino Uno is specified in the script.

### Note

The provided Arduino code intentionally avoids using built-in functions or external libraries such as `EEPROM.h`. Instead, it implements all EEPROM read and write operations directly. Feel free to explore and modify the code to suit your specific project needs.
