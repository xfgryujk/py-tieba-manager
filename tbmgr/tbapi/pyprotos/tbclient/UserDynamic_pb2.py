# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/UserDynamic.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import User_pb2 as tbclient_dot_User__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/UserDynamic.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/UserDynamic.proto\x12\x08tbclient\x1a\x13tbclient/User.proto\":\n\x0bUserDynamic\x12+\n\x13\x63oncerned_user_list\x18\x01 \x03(\x0b\x32\x0e.tbclient.User')
  ,
  dependencies=[tbclient_dot_User__pb2.DESCRIPTOR,])




_USERDYNAMIC = _descriptor.Descriptor(
  name='UserDynamic',
  full_name='tbclient.UserDynamic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='concerned_user_list', full_name='tbclient.UserDynamic.concerned_user_list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=119,
)

_USERDYNAMIC.fields_by_name['concerned_user_list'].message_type = tbclient_dot_User__pb2._USER
DESCRIPTOR.message_types_by_name['UserDynamic'] = _USERDYNAMIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserDynamic = _reflection.GeneratedProtocolMessageType('UserDynamic', (_message.Message,), dict(
  DESCRIPTOR = _USERDYNAMIC,
  __module__ = 'tbclient.UserDynamic_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.UserDynamic)
  ))
_sym_db.RegisterMessage(UserDynamic)


# @@protoc_insertion_point(module_scope)