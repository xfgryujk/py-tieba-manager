# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/UserPics.proto

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
  name='tbclient/UserPics.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/UserPics.proto\x12\x08tbclient\"&\n\x08UserPics\x12\x0b\n\x03\x62ig\x18\x01 \x01(\t\x12\r\n\x05small\x18\x02 \x01(\t')
)




_USERPICS = _descriptor.Descriptor(
  name='UserPics',
  full_name='tbclient.UserPics',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='big', full_name='tbclient.UserPics.big', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='small', full_name='tbclient.UserPics.small', index=1,
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
  serialized_start=37,
  serialized_end=75,
)

DESCRIPTOR.message_types_by_name['UserPics'] = _USERPICS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserPics = _reflection.GeneratedProtocolMessageType('UserPics', (_message.Message,), dict(
  DESCRIPTOR = _USERPICS,
  __module__ = 'tbclient.UserPics_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.UserPics)
  ))
_sym_db.RegisterMessage(UserPics)


# @@protoc_insertion_point(module_scope)
