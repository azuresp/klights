from RFM69 import Radio, FREQ_915MHZ
import datetime
import time
import random

node_id = 1
network_id = 100
recipient_id = 2

with Radio(FREQ_915MHZ, node_id, network_id, isHighPower=True, verbose=True) as radio:
    print ("Starting loop...")
    
    rx_counter = 0
    tx_counter = 6

    while True:
        

        # Every 5 seconds send a message
        if tx_counter > 5:
            tx_counter=0


            r = random.randrange(255).to_bytes(1,byteorder='big')[0]
            g = random.randrange(255).to_bytes(1,byteorder='big')[0]
            b = random.randrange(255).to_bytes(1,byteorder='big')[0]

            ba = list([r,g,b])


            # Send
            print ("Sending")
            if radio.send(2, ba, attempts=3, waitTime=100):
                print ("Acknowledgement received")
            else:
                print ("No Acknowledgement")


        print("Listening...", len(radio.packets), radio.mode_name)
        delay = 0.5
        rx_counter += delay
        tx_counter += delay
        time.sleep(delay)
        