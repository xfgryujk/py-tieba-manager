# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/BawuRoleInfoPub.proto

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
  name='tbclient/BawuRoleInfoPub.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1etbclient/BawuRoleInfoPub.proto\x12\x08tbclient\"\xa5\x01\n\x0f\x42\x61wuRoleInfoPub\x12\x10\n\x08\x66orum_id\x18\x01 \x01(\x04\x12\x12\n\nlevel_name\x18\x07 \x01(\t\x12\x10\n\x08portrait\x18\x05 \x01(\t\x12\x0f\n\x07role_id\x18\x03 \x01(\x05\x12\x11\n\trole_name\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x02 \x01(\x03\x12\x12\n\nuser_level\x18\x06 \x01(\x05\x12\x11\n\tuser_name\x18\x08 \x01(\t')
)




_BAWUROLEINFOPUB = _descriptor.Descriptor(
  name='BawuRoleInfoPub',
  full_name='tbclient.BawuRoleInfoPub',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='tbclient.BawuRoleInfoPub.forum_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level_name', full_name='tbclient.BawuRoleInfoPub.level_name', index=1,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.BawuRoleInfoPub.portrait', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_id', full_name='tbclient.BawuRoleInfoPub.role_id', index=3,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='role_name', full_name='tbclient.BawuRoleInfoPub.role_name', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.BawuRoleInfoPub.user_id', index=5,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_level', full_name='tbclient.BawuRoleInfoPub.user_level', index=6,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.BawuRoleInfoPub.user_name', index=7,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=45,
  serialized_end=210,
)

DESCRIPTOR.message_types_by_name['BawuRoleInfoPub'] = _BAWUROLEINFOPUB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BawuRoleInfoPub = _reflection.GeneratedProtocolMessageType('BawuRoleInfoPub', (_message.Message,), dict(
  DESCRIPTOR = _BAWUROLEINFOPUB,
  __module__ = 'tbclient.BawuRoleInfoPub_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.BawuRoleInfoPub)
  ))
_sym_db.RegisterMessage(BawuRoleInfoPub)


# @@protoc_insertion_point(module_scope)
