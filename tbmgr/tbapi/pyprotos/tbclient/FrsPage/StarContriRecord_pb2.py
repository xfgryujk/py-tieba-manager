# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/StarContriRecord.proto

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
  name='tbclient/FrsPage/StarContriRecord.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\'tbclient/FrsPage/StarContriRecord.proto\x12\x10tbclient.FrsPage\"M\n\x10StarContriRecord\x12\x15\n\rrecord_notice\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x11\n\tuser_name\x18\x02 \x01(\t')
)




_STARCONTRIRECORD = _descriptor.Descriptor(
  name='StarContriRecord',
  full_name='tbclient.FrsPage.StarContriRecord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_notice', full_name='tbclient.FrsPage.StarContriRecord.record_notice', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.FrsPage.StarContriRecord.user_id', index=1,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.FrsPage.StarContriRecord.user_name', index=2,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=61,
  serialized_end=138,
)

DESCRIPTOR.message_types_by_name['StarContriRecord'] = _STARCONTRIRECORD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StarContriRecord = _reflection.GeneratedProtocolMessageType('StarContriRecord', (_message.Message,), dict(
  DESCRIPTOR = _STARCONTRIRECORD,
  __module__ = 'tbclient.FrsPage.StarContriRecord_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.StarContriRecord)
  ))
_sym_db.RegisterMessage(StarContriRecord)


# @@protoc_insertion_point(module_scope)