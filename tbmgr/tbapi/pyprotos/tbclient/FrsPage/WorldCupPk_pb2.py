# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/WorldCupPk.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/FrsPage/WorldCupPk.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n!tbclient/FrsPage/WorldCupPk.proto\x12\x10tbclient.FrsPage\"Q\n\nWorldCupPk\x12\x11\n\tprize_url\x18\x03 \x01(\t\x12\x11\n\tsum_bonus\x18\x02 \x01(\t\x12\x10\n\x08sum_game\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x04 \x01(\t')
)




_WORLDCUPPK = _descriptor.Descriptor(
  name='WorldCupPk',
  full_name='tbclient.FrsPage.WorldCupPk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='prize_url', full_name='tbclient.FrsPage.WorldCupPk.prize_url', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum_bonus', full_name='tbclient.FrsPage.WorldCupPk.sum_bonus', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sum_game', full_name='tbclient.FrsPage.WorldCupPk.sum_game', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.FrsPage.WorldCupPk.url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=55,
  serialized_end=136,
)

DESCRIPTOR.message_types_by_name['WorldCupPk'] = _WORLDCUPPK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

WorldCupPk = _reflection.GeneratedProtocolMessageType('WorldCupPk', (_message.Message,), dict(
  DESCRIPTOR = _WORLDCUPPK,
  __module__ = 'tbclient.FrsPage.WorldCupPk_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.WorldCupPk)
  ))
_sym_db.RegisterMessage(WorldCupPk)


# @@protoc_insertion_point(module_scope)