# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import anyjson as _json

from . import fernet_decode, fernet_encode

MIMETYPE = 'application/x-fernet-json'

register_args = (
    fernet_encode(_json.dumps),
    fernet_decode(_json.loads),
    MIMETYPE,
    'utf-8',
)
