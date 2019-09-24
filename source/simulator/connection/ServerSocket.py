import json
import socket
import threading
import time
from typing import Any

from ev3dev2.connection.DataRequest import DataRequest
from ev3dev2.connection.DriveCommand import DriveCommand
from ev3dev2.connection.StopCommand import StopCommand
from simulator.connection.MessageHandler import MessageHandler


class ServerSocket(threading.Thread):

    def __init__(self, robot_state):
        threading.Thread.__init__(self)
        self.message_handler = MessageHandler(robot_state)
        self.robot_state = robot_state

        self.first_run = True


    def run(self):
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind(('localhost', 6840))
        server.listen(5)

        while True:
            print('Listening for connections...')
            (client, address) = server.accept()

            print('Connection accepted')
            if not self.first_run:
                self.robot_state.should_reset = True

            self.first_run = False
            time.sleep(1)

            try:
                while True:

                    data = client.recv(128)
                    if data:

                        val = self._handle(data)
                        if val:
                            client.send(val)

                    else:
                        break

            except socket.error:
                pass

            print('Closing connection...')
            client.close()


    def _handle(self, data: bytes) -> Any:
        jsn = data.decode()
        jsn = jsn.replace('#', '')

        obj_dict = json.loads(jsn)

        tpe = obj_dict['type']
        if tpe == 'DriveCommand':
            return self._handle_drive_command(obj_dict)

        if tpe == 'StopCommand':
            return self._handle_stop_command(obj_dict)

        elif tpe == 'DataRequest':
            return self._handle_data_request(obj_dict)


    def _handle_drive_command(self, d: dict) -> Any:
        command = DriveCommand(d['address'], d['ppf'], d['frames'], d['frames_coast'])
        self.message_handler.handle_drive_command(command)

        return None


    def _handle_stop_command(self, d: dict) -> Any:
        command = StopCommand(d['address'], d['ppf'], d['frames'])
        self.message_handler.handle_stop_command(command)

        return None


    def _handle_data_request(self, d: dict) -> Any:
        request = DataRequest(d['address'])
        val = self.message_handler.handle_data_request(request)

        return self._serialize(val)


    def _serialize(self, val):
        d = {'value': val}

        jsn = json.dumps(d)
        return str.encode(jsn)