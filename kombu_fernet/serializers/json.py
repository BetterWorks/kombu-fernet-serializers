# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

import anyjson as _json

from . import fernet_encode, fernet_decode, force_text

MIMETYPE = 'application/x-fernet-json'

register_args = (
    fernet_encode(_json.dumps),
    fernet_decode(force_text(_json.loads)),
    MIMETYPE,
    'utf-8',
)
