#!/usr/bin/env python3

import rospy
import serial

from biospherical_par_sensor.msg import par


class SerialConnection:
    def __init__(self, device, baud=9600):
        self.device = device
        self.baud = baud
        self.open()

    def open(self):
        self.port = serial.Serial(self.device, self.baud, timeout=0.1)

    def send(self, data):
        pass
        # disabled for now since this was copied from elseware and we don't
        # need to write for now
        # self.port.write(data.encode('utf-8'))
        #return self.recv()

    def recv(self):
        data = self.port.readline().decode('utf-8')
        if len(data):
            return data
        return None

rospy.init_node('par_sensor')

serial_port = rospy.get_param('~serial_port', '/dev/ttyS0')
baud_rate = rospy.get_param('~baud_rate', 9600)

connection = SerialConnection(serial_port, baud_rate)

publisher = rospy.Publisher("data", par, queue_size=10)

while not rospy.is_shutdown():
    data = connection.recv()
    parts = data.split()
    if len(parts) == 3:
        par_message = par()
        par_message.irradiance = float(parts[0].rstrip(', '))
        par_message.temperature = float(parts[1].rstrip(', '))
        par_message.line_voltage = float(parts[2].rstrip(', '))
        publisher.publish(par_message)
