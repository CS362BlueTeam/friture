#Test file for audioBackend
import pytest
import friture.audiobackend as ab
import sounddevice

def test_creation():
    abe = ab.AudioBackend()
    assert abe != None

def test_outputStreamOpen():
    abe = ab.AudioBackend()
    stream = abe.open_stream(abe.device)
    assert stream != None

def test_init():
    abe = ab.AudioBackend()
    abe.device = None
    assert abe.device == None
    abe.__init__()
    assert abe.device != None

def test_getInputDevices(monkeypatch):
    abe = ab.AudioBackend()
    monkeypatch.setattr("friture.audiobackend.__AudioBackend.get_input_devices", lambda x: [])
    input_devices = abe.get_input_devices()
    assert input_devices == []