# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ActHot.proto

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
  name='tbclient/ActHot.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x15tbclient/ActHot.proto\x12\x08tbclient\"n\n\x06\x41\x63tHot\x12\x13\n\x0b\x61uthor_name\x18\x04 \x01(\t\x12\r\n\x05\x62size\x18\x01 \x01(\t\x12\x0f\n\x07img_des\x18\x05 \x01(\t\x12\x0f\n\x07img_src\x18\x02 \x01(\t\x12\x10\n\x08img_type\x18\x06 \x01(\x05\x12\x0c\n\x04link\x18\x03 \x01(\t')
)




_ACTHOT = _descriptor.Descriptor(
  name='ActHot',
  full_name='tbclient.ActHot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='author_name', full_name='tbclient.ActHot.author_name', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bsize', full_name='tbclient.ActHot.bsize', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_des', full_name='tbclient.ActHot.img_des', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_src', full_name='tbclient.ActHot.img_src', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_type', full_name='tbclient.ActHot.img_type', index=4,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='tbclient.ActHot.link', index=5,
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
  serialized_start=35,
  serialized_end=145,
)

DESCRIPTOR.message_types_by_name['ActHot'] = _ACTHOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActHot = _reflection.GeneratedProtocolMessageType('ActHot', (_message.Message,), dict(
  DESCRIPTOR = _ACTHOT,
  __module__ = 'tbclient.ActHot_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ActHot)
  ))
_sym_db.RegisterMessage(ActHot)


# @@protoc_insertion_point(module_scope)
