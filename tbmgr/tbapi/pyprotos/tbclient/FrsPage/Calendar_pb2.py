# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/Calendar.proto

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
  name='tbclient/FrsPage/Calendar.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1ftbclient/FrsPage/Calendar.proto\x12\x10tbclient.FrsPage\"+\n\x08\x43\x61lendar\x12\x0c\n\x04rank\x18\x03 \x01(\x05\x12\x11\n\tsign_type\x18\x04 \x01(\x05')
)




_CALENDAR = _descriptor.Descriptor(
  name='Calendar',
  full_name='tbclient.FrsPage.Calendar',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='rank', full_name='tbclient.FrsPage.Calendar.rank', index=0,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign_type', full_name='tbclient.FrsPage.Calendar.sign_type', index=1,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=53,
  serialized_end=96,
)

DESCRIPTOR.message_types_by_name['Calendar'] = _CALENDAR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Calendar = _reflection.GeneratedProtocolMessageType('Calendar', (_message.Message,), dict(
  DESCRIPTOR = _CALENDAR,
  __module__ = 'tbclient.FrsPage.Calendar_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.Calendar)
  ))
_sym_db.RegisterMessage(Calendar)


# @@protoc_insertion_point(module_scope)
