# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/NtSpreadInfo.proto

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
  name='tbclient/FrsPage/NtSpreadInfo.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n#tbclient/FrsPage/NtSpreadInfo.proto\x12\x10tbclient.FrsPage\"\xa9\x01\n\x0cNtSpreadInfo\x12\x10\n\x08link_url\x18\x07 \x01(\t\x12\x0c\n\x04pics\x18\x06 \x03(\t\x12\x10\n\x08position\x18\x08 \x01(\r\x12\x14\n\x0cpublish_date\x18\t \x01(\t\x12\x0c\n\x04tips\x18\x03 \x01(\t\x12\r\n\x05title\x18\x05 \x01(\t\x12\x0c\n\x04type\x18\x04 \x01(\t\x12\x13\n\x0buser_avatar\x18\x02 \x01(\t\x12\x11\n\tuser_name\x18\x01 \x01(\t')
)




_NTSPREADINFO = _descriptor.Descriptor(
  name='NtSpreadInfo',
  full_name='tbclient.FrsPage.NtSpreadInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_url', full_name='tbclient.FrsPage.NtSpreadInfo.link_url', index=0,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pics', full_name='tbclient.FrsPage.NtSpreadInfo.pics', index=1,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='position', full_name='tbclient.FrsPage.NtSpreadInfo.position', index=2,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='publish_date', full_name='tbclient.FrsPage.NtSpreadInfo.publish_date', index=3,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tips', full_name='tbclient.FrsPage.NtSpreadInfo.tips', index=4,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.FrsPage.NtSpreadInfo.title', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tbclient.FrsPage.NtSpreadInfo.type', index=6,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_avatar', full_name='tbclient.FrsPage.NtSpreadInfo.user_avatar', index=7,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.FrsPage.NtSpreadInfo.user_name', index=8,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=58,
  serialized_end=227,
)

DESCRIPTOR.message_types_by_name['NtSpreadInfo'] = _NTSPREADINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NtSpreadInfo = _reflection.GeneratedProtocolMessageType('NtSpreadInfo', (_message.Message,), dict(
  DESCRIPTOR = _NTSPREADINFO,
  __module__ = 'tbclient.FrsPage.NtSpreadInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.NtSpreadInfo)
  ))
_sym_db.RegisterMessage(NtSpreadInfo)


# @@protoc_insertion_point(module_scope)
