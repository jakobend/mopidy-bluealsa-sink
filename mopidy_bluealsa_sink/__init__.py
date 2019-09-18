"""
mopidy-bluealsa-sink
"""

from mopidy import ext

__version__ = "0.0.1"

class Extension(ext.Extension):
    dist_name = "Mopidy-BlueALSA-Sink"
    ext_name = "bluealsa-sink"
    version = __version__

    def setup(self, registry):
        from mopidy_bluealsa_sink.backend import BlueAlsaSinkBackend
        registry.add("backend", BlueAlsaSinkBackend)
