# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/UserMap.proto

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
  name='tbclient/UserMap.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x16tbclient/UserMap.proto\x12\x08tbclient\"0\n\x07UserMap\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t')
)




_USERMAP = _descriptor.Descriptor(
  name='UserMap',
  full_name='tbclient.UserMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.UserMap.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tbclient.UserMap.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.UserMap.url', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=36,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['UserMap'] = _USERMAP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserMap = _reflection.GeneratedProtocolMessageType('UserMap', (_message.Message,), dict(
  DESCRIPTOR = _USERMAP,
  __module__ = 'tbclient.UserMap_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.UserMap)
  ))
_sym_db.RegisterMessage(UserMap)


# @@protoc_insertion_point(module_scope)
