# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/HeadSdk.proto

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
  name='tbclient/FrsPage/HeadSdk.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1etbclient/FrsPage/HeadSdk.proto\x12\x10tbclient.FrsPage\"g\n\x07HeadSdk\x12\x10\n\x08head_pic\x18\x01 \x01(\t\x12\x11\n\thead_text\x18\x02 \x01(\t\x12\x11\n\thead_type\x18\x05 \x01(\x05\x12\x10\n\x08sdk_name\x18\x03 \x01(\t\x12\x12\n\nsdk_params\x18\x04 \x01(\t')
)




_HEADSDK = _descriptor.Descriptor(
  name='HeadSdk',
  full_name='tbclient.FrsPage.HeadSdk',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='head_pic', full_name='tbclient.FrsPage.HeadSdk.head_pic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_text', full_name='tbclient.FrsPage.HeadSdk.head_text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='head_type', full_name='tbclient.FrsPage.HeadSdk.head_type', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sdk_name', full_name='tbclient.FrsPage.HeadSdk.sdk_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sdk_params', full_name='tbclient.FrsPage.HeadSdk.sdk_params', index=4,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=52,
  serialized_end=155,
)

DESCRIPTOR.message_types_by_name['HeadSdk'] = _HEADSDK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeadSdk = _reflection.GeneratedProtocolMessageType('HeadSdk', (_message.Message,), dict(
  DESCRIPTOR = _HEADSDK,
  __module__ = 'tbclient.FrsPage.HeadSdk_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.HeadSdk)
  ))
_sym_db.RegisterMessage(HeadSdk)


# @@protoc_insertion_point(module_scope)
