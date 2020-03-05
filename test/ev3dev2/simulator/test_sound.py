import sys
import unittest

from unittest.mock import patch, MagicMock

clientSocketModuleMock = MagicMock()
sys.modules['ev3dev2simulator.connection.ClientSocket'] = clientSocketModuleMock
# you cannot import ClientSocket, since that sets up a connection

clientSocketMock = MagicMock()
clientSocketModuleMock.get_client_socket = lambda: clientSocketMock

from ev3dev2.sound import Sound


class SoundTest(unittest.TestCase):
    def test_beep(self):
        spkr = Sound()
        spkr.beep(play_type=0)
        print(clientSocketMock.method_calls)
        spkr.beep(play_type=1)
        print(clientSocketMock.method_calls)

    # def test_play_tone(self):
    #     spkr = Sound()
    #     spkr.play_tone(500, duration=0.3, volume=50, play_type=1)
    #     spkr.play_tone(1500, duration=0.3, volume=50, play_type=0)
    #
    # def test_tone(self):
    #     spkr = Sound()
    #     spkr.tone([
    #         (392, 350, 100), (392, 350), (392,), ()
    #     ])
    #     print(clientSocketMock.method_calls)
    #
    # def test_play_note(self):
    #     spkr = Sound()
    #     spkr.play_note("C4", 0.5)
    #     spkr.play_note("D4", 0.3)
    #     spkr.play_note("E4", 0.01)
    #
    #
    # def test_play_song(self):
    #     spkr = Sound()
    #     spkr.play_song((
    #         ('G4', 'h'),  # meas 1
    #         ('D5', 'h'),
    #         ('C5', 'e3'),  # meas 2
    #         ('B4', 'e3'),
    #         ('A4', 'e3'),
    #         ('G5', 'h'),
    #         ('D5', 'q'),
    #     ), tempo=150)
    #
    # def test_play_file(self):
    #     spkr = Sound()
    #     spkr.play_file('inputFiles/bark.wav', play_type=0)
    #
    #     # Test for invalid path files
    #     with self.assertRaises(ValueError) as cm:
    #         spkr.play_file('file/that/does/not/exist.wav', play_type=0)
    #
    #     self.assertEqual(cm.exception.args[0], 'file/that/does/not/exist.wav does not exist')
    #
    #     # Test for wrong extensions
    #     with self.assertRaises(ValueError) as cm:
    #         spkr.play_file('inputFiles/bark', play_type=0)
    #
    #     self.assertEqual(cm.exception.args[0], 'invalid sound file (inputFiles/bark), only .wav files are supported')
    #
    # def test_speak(self):
    #     spkr = Sound()
    #     spkr.speak("test test test test test", volume=100, play_type=1)
    #     spkr.play_note("C4", 2)
    #     spkr.speak("kekeroni", volume=100, play_type=0)


if __name__ == '__main__':
    unittest.main()
