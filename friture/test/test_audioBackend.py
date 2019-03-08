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

def test_handleNewData():
    abe = ab.AudioBackend()
    abe.handle_new_data("",[None],[None],True)
    abe.handle_new_data("",[None],[None],False)

def test_getters():
    abe = ab.AudioBackend()
    count = abe.get_device_outputchannels_count(abe.device)
    assert count != None
    count = abe.get_current_device_nchannels()
    assert count != None
    count = abe.get_current_second_channel()
    assert count != None
    count = abe.get_current_first_channel()
    assert count != None
    device = abe.get_readable_current_device()
    assert device != None

def test_currentChannels():
    abe = ab.AudioBackend()
    channels = abe.get_readable_current_channels()
    assert channels != None
    abe.device['max_input_channels'] = 2
    channels = abe.get_readable_current_channels()
    assert channels == ['L', 'R']

def test_outputSupported():
    abe = ab.AudioBackend()
    assert abe.is_output_format_supported(abe.device, None) == False

def test_selectInputDevice():
    abe = ab.AudioBackend()
    data = abe.select_input_device(0)
    assert data != None
    with pytest.raises(Exception):
        abe.select_input_device(99999)