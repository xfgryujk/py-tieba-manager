# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ScoreInfo.proto

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
  name='tbclient/ScoreInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x18tbclient/ScoreInfo.proto\x12\x08tbclient\"+\n\tScoreInfo\x12\x0f\n\x07\x65ndtime\x18\x02 \x01(\x05\x12\r\n\x05score\x18\x01 \x01(\x05')
)




_SCOREINFO = _descriptor.Descriptor(
  name='ScoreInfo',
  full_name='tbclient.ScoreInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='endtime', full_name='tbclient.ScoreInfo.endtime', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='tbclient.ScoreInfo.score', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=38,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['ScoreInfo'] = _SCOREINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ScoreInfo = _reflection.GeneratedProtocolMessageType('ScoreInfo', (_message.Message,), dict(
  DESCRIPTOR = _SCOREINFO,
  __module__ = 'tbclient.ScoreInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ScoreInfo)
  ))
_sym_db.RegisterMessage(ScoreInfo)


# @@protoc_insertion_point(module_scope)