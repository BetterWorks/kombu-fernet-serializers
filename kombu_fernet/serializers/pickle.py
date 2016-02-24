# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from kombu.serialization import pickle, pickle_protocol, unpickle

from . import fernet_decode, fernet_encode


def pickle_dumps(obj, dumper=pickle.dumps):
    return dumper(obj, protocol=pickle_protocol)

MIMETYPE = 'application/x-fernet-python-serialize'

register_args = (
    fernet_encode(pickle_dumps),
    fernet_decode(unpickle),
    MIMETYPE,
    'utf-8',
)
