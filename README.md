# mopidy-bluealsa-sink

The goal of this project is to consolidate [mopidy](https://www.mopidy.com/)
with [BlueALSA](https://github.com/Arkq/bluez-alsa)
(formerly known as bluez-alsa) to allow seamless audio playback from Bluetooth
sources on a mopidy server.

The idea is to expose Bluetooth devices in the vicinity as library items. When
the frontend chooses to play one of these items, mopidy-bluealsa-sink will
connect to the device if needed and then route the ALSA stream provided by
BlueALSA to mopidy.

This should allow for easy integration into all current mopidy frontends and
removes the need for a separate BlueZ agent that accepts incoming A2DP
connections.

A further optional development goal would be to implement such an agent that
appends the appropriate library item to the queue when a device connects.
