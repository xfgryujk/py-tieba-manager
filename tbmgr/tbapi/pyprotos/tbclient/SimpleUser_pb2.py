# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/SimpleUser.proto

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
  name='tbclient/SimpleUser.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/SimpleUser.proto\x12\x08tbclient\"\xeb\x01\n\nSimpleUser\x12\x12\n\nagree_type\x18\t \x01(\x05\x12\x11\n\tahead_url\x18\n \x01(\t\x12\x11\n\tblock_msg\x18\x0b \x01(\t\x12\x17\n\x0fincomplete_user\x18\x07 \x01(\r\x12\x10\n\x08portrait\x18\x08 \x01(\t\x12\x13\n\x0bsecureemail\x18\x03 \x01(\t\x12\x13\n\x0bsecuremobil\x18\x04 \x01(\t\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x11\n\tuser_name\x18\x05 \x01(\t\x12\x15\n\ruser_nickname\x18\x06 \x01(\t\x12\x13\n\x0buser_status\x18\x02 \x01(\x05')
)




_SIMPLEUSER = _descriptor.Descriptor(
  name='SimpleUser',
  full_name='tbclient.SimpleUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agree_type', full_name='tbclient.SimpleUser.agree_type', index=0,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ahead_url', full_name='tbclient.SimpleUser.ahead_url', index=1,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_msg', full_name='tbclient.SimpleUser.block_msg', index=2,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='incomplete_user', full_name='tbclient.SimpleUser.incomplete_user', index=3,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.SimpleUser.portrait', index=4,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secureemail', full_name='tbclient.SimpleUser.secureemail', index=5,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='securemobil', full_name='tbclient.SimpleUser.securemobil', index=6,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.SimpleUser.user_id', index=7,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.SimpleUser.user_name', index=8,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_nickname', full_name='tbclient.SimpleUser.user_nickname', index=9,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_status', full_name='tbclient.SimpleUser.user_status', index=10,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=40,
  serialized_end=275,
)

DESCRIPTOR.message_types_by_name['SimpleUser'] = _SIMPLEUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SimpleUser = _reflection.GeneratedProtocolMessageType('SimpleUser', (_message.Message,), dict(
  DESCRIPTOR = _SIMPLEUSER,
  __module__ = 'tbclient.SimpleUser_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.SimpleUser)
  ))
_sym_db.RegisterMessage(SimpleUser)


# @@protoc_insertion_point(module_scope)