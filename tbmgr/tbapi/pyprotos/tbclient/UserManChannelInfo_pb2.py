# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/UserManChannelInfo.proto

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
  name='tbclient/UserManChannelInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n!tbclient/UserManChannelInfo.proto\x12\x08tbclient\"A\n\x12UserManChannelInfo\x12\x16\n\x0e\x66ollow_channel\x18\x02 \x01(\r\x12\x13\n\x0bman_channel\x18\x01 \x01(\r')
)




_USERMANCHANNELINFO = _descriptor.Descriptor(
  name='UserManChannelInfo',
  full_name='tbclient.UserManChannelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='follow_channel', full_name='tbclient.UserManChannelInfo.follow_channel', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='man_channel', full_name='tbclient.UserManChannelInfo.man_channel', index=1,
      number=1, type=13, cpp_type=3, label=1,
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
  serialized_start=47,
  serialized_end=112,
)

DESCRIPTOR.message_types_by_name['UserManChannelInfo'] = _USERMANCHANNELINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserManChannelInfo = _reflection.GeneratedProtocolMessageType('UserManChannelInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERMANCHANNELINFO,
  __module__ = 'tbclient.UserManChannelInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.UserManChannelInfo)
  ))
_sym_db.RegisterMessage(UserManChannelInfo)


# @@protoc_insertion_point(module_scope)
