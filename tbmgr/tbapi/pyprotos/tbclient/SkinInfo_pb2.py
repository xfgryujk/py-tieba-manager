# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/SkinInfo.proto

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
  name='tbclient/SkinInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/SkinInfo.proto\x12\x08tbclient\"\\\n\x08SkinInfo\x12\x12\n\nmonitor_id\x18\x05 \x01(\t\x12\x0e\n\x06obj_id\x18\x04 \x01(\t\x12\x0c\n\x04skin\x18\x01 \x01(\t\x12\x11\n\tskin_size\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t')
)




_SKININFO = _descriptor.Descriptor(
  name='SkinInfo',
  full_name='tbclient.SkinInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='monitor_id', full_name='tbclient.SkinInfo.monitor_id', index=0,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='obj_id', full_name='tbclient.SkinInfo.obj_id', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skin', full_name='tbclient.SkinInfo.skin', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skin_size', full_name='tbclient.SkinInfo.skin_size', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.SkinInfo.url', index=4,
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
  serialized_start=37,
  serialized_end=129,
)

DESCRIPTOR.message_types_by_name['SkinInfo'] = _SKININFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SkinInfo = _reflection.GeneratedProtocolMessageType('SkinInfo', (_message.Message,), dict(
  DESCRIPTOR = _SKININFO,
  __module__ = 'tbclient.SkinInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.SkinInfo)
  ))
_sym_db.RegisterMessage(SkinInfo)


# @@protoc_insertion_point(module_scope)