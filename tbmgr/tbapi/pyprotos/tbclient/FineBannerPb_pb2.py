# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FineBannerPb.proto

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
  name='tbclient/FineBannerPb.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1btbclient/FineBannerPb.proto\x12\x08tbclient\"N\n\x0c\x46ineBannerPb\x12\x0c\n\x04\x66tid\x18\x01 \x01(\x03\x12\x10\n\x08link_url\x18\x04 \x01(\t\x12\x0f\n\x07pic_url\x18\x03 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t')
)




_FINEBANNERPB = _descriptor.Descriptor(
  name='FineBannerPb',
  full_name='tbclient.FineBannerPb',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ftid', full_name='tbclient.FineBannerPb.ftid', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_url', full_name='tbclient.FineBannerPb.link_url', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pic_url', full_name='tbclient.FineBannerPb.pic_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.FineBannerPb.title', index=3,
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
  serialized_start=41,
  serialized_end=119,
)

DESCRIPTOR.message_types_by_name['FineBannerPb'] = _FINEBANNERPB
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FineBannerPb = _reflection.GeneratedProtocolMessageType('FineBannerPb', (_message.Message,), dict(
  DESCRIPTOR = _FINEBANNERPB,
  __module__ = 'tbclient.FineBannerPb_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FineBannerPb)
  ))
_sym_db.RegisterMessage(FineBannerPb)


# @@protoc_insertion_point(module_scope)
