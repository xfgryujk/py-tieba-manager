# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FollowRelation.proto

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
  name='tbclient/FollowRelation.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1dtbclient/FollowRelation.proto\x12\x08tbclient\"Z\n\x0e\x46ollowRelation\x12\x12\n\nhas_follow\x18\x04 \x01(\x08\x12\x10\n\x08portrait\x18\x03 \x01(\t\x12\x0f\n\x07user_id\x18\x01 \x01(\x04\x12\x11\n\tuser_name\x18\x02 \x01(\t')
)




_FOLLOWRELATION = _descriptor.Descriptor(
  name='FollowRelation',
  full_name='tbclient.FollowRelation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='has_follow', full_name='tbclient.FollowRelation.has_follow', index=0,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.FollowRelation.portrait', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.FollowRelation.user_id', index=2,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.FollowRelation.user_name', index=3,
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
  serialized_start=43,
  serialized_end=133,
)

DESCRIPTOR.message_types_by_name['FollowRelation'] = _FOLLOWRELATION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FollowRelation = _reflection.GeneratedProtocolMessageType('FollowRelation', (_message.Message,), dict(
  DESCRIPTOR = _FOLLOWRELATION,
  __module__ = 'tbclient.FollowRelation_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FollowRelation)
  ))
_sym_db.RegisterMessage(FollowRelation)


# @@protoc_insertion_point(module_scope)
