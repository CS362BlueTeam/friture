#Test file for audioBackend
import pytest
from friture import audiobackend as ab
import sounddevice

#This exception isn't handled and crashes the program when there are no audio devices present
def test_noAudioDevices(monkeypatch):
    monkeypatch.setattr("sounddevice.query_devices", lambda: [None])
    abe = ab.AudioBackend()



def test_outputStreamOpen():
    abe = ab.AudioBackend()
    stream = abe.open_stream(abe.device)
    assert stream != None

def test_init():
    abe = ab.AudioBackend()
    abe.__init__()
    assert abe.device != None

def test_getInputDevices():
    abe = ab.AudioBackend()
    input_devices = abe.get_input_devices()
    assert input_devices != [None]

def test_getOutputDevices():
    abe = ab.AudioBackend()
    output_devices = abe.get_output_devices()
    assert output_devices != [None]

def test_restart():
    abe = ab.AudioBackend()
    abe.restart()

def test_pause():
    abe = ab.AudioBackend()
    abe.pause()

def test_getStreamTime(monkeypatch):
    abe = ab.AudioBackend()
    time = abe.get_stream_time()
    assert time != None
    monkeypatch.setattr("friture.audiobackend.__AudioBackend.get_stream_time", lambda: [None])
    with pytest.raises(Exception):
        time = abe.get_stream_time()

def test_setDuoInput():
    abe = ab.AudioBackend()
    abe.set_duo_input()
    assert abe.duo_input == True

def test_setSingleInput():
    abe = ab.AudioBackend()
    abe.set_single_input()
    assert abe.duo_input == False
