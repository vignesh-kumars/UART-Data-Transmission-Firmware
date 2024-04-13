import serial
import time

def send_data_via_serial(data, data_port='COM5', baud_rate=2400):
    info_serial = serial.Serial(data_port, baud_rate) 
    time.sleep(2)  

    transmit_time = time.time()
    for ch in data:
        info_serial.write(ch.encode())
        next_time = time.time()
        if next_time != transmit_time:
            print("SPEED FOR CHAR ", ch,"TRANSMITTED FROM PC TO MCU  :", (8.0 / (next_time - transmit_time))," BITS/SEC")
        transmit_time = next_time

    info_serial.write(b"0\n1005\n")
    info_serial.close()

def receive_data_via_serial(data_port='COM5', baud_rate=2400):
    info_serial= serial.Serial(data_port, baud_rate) 
    time.sleep(2)

    data_received = ''
    begin_time = time.time()
    while True:
        received_byte = info_serial.read()
        if not received_byte:
            continue
        char_received= received_byte.decode('utf-8', errors='replace')

        end_time = time.time()
        if char_received == '\n':
            break 
        data_received += char_received
        if end_time != begin_time:
            speed_of_data = 8.0 / (end_time - begin_time)
            print("SPEED FOR CHAR'{}' RECEIVED FROM MCU TO PC : {:.2f} bits/second".format(char_received, speed_of_data))
        begin_time = end_time

    info_serial.close()
    return  data_received.strip()

send_data_string = "Finance Minister Arun Jaitley Tuesday hit out at former RBI governor Raghuram Rajan for predicting that the next banking crisis would be triggered by MSME lending, saying postmortem is easier than taking action when it was required. Rajan, who had as the chief economist at IMF warned of impending financial crisis of 2008, in a note to a parliamentary committee warned against ambitious credit targets and loan waivers, saying that they could be the sources of next banking crisis. Government should focus on sources of the next crisis, not just the last one. In particular, government should refrain from setting ambitious credit targets or waiving loans. Credit targets are sometimes achieved by abandoning appropriate due diligence, creating the environment for future NPAs,Rajan said in the note.Both MUDRA loans as well as the Kisan Credit Card, while popular, have to be examined more closely for potential credit risk. Rajan, who was RBI governor for three years till September 2016, is currently.\n"

send_data_via_serial(send_data_string)

data_received = receive_data_via_serial()

print("DATA RECEIVED FROM MCU :\n",  data_received)
