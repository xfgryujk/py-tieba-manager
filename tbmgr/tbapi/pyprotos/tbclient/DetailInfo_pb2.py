# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/DetailInfo.proto

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
  name='tbclient/DetailInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/DetailInfo.proto\x12\x08tbclient\"\'\n\nDetailInfo\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t')
)




_DETAILINFO = _descriptor.Descriptor(
  name='DetailInfo',
  full_name='tbclient.DetailInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='tbclient.DetailInfo.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.DetailInfo.url', index=1,
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
  serialized_start=39,
  serialized_end=78,
)

DESCRIPTOR.message_types_by_name['DetailInfo'] = _DETAILINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DetailInfo = _reflection.GeneratedProtocolMessageType('DetailInfo', (_message.Message,), dict(
  DESCRIPTOR = _DETAILINFO,
  __module__ = 'tbclient.DetailInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.DetailInfo)
  ))
_sym_db.RegisterMessage(DetailInfo)


# @@protoc_insertion_point(module_scope)
