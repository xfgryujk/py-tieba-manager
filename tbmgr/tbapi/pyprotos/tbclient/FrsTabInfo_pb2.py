# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsTabInfo.proto

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
  name='tbclient/FrsTabInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/FrsTabInfo.proto\x12\x08tbclient\"Q\n\nFrsTabInfo\x12\x0e\n\x06tab_id\x18\x01 \x01(\x05\x12\x10\n\x08tab_name\x18\x03 \x01(\t\x12\x10\n\x08tab_type\x18\x02 \x01(\x05\x12\x0f\n\x07tab_url\x18\x04 \x01(\t')
)




_FRSTABINFO = _descriptor.Descriptor(
  name='FrsTabInfo',
  full_name='tbclient.FrsTabInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='tab_id', full_name='tbclient.FrsTabInfo.tab_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tab_name', full_name='tbclient.FrsTabInfo.tab_name', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tab_type', full_name='tbclient.FrsTabInfo.tab_type', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tab_url', full_name='tbclient.FrsTabInfo.tab_url', index=3,
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
  serialized_start=39,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['FrsTabInfo'] = _FRSTABINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FrsTabInfo = _reflection.GeneratedProtocolMessageType('FrsTabInfo', (_message.Message,), dict(
  DESCRIPTOR = _FRSTABINFO,
  __module__ = 'tbclient.FrsTabInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsTabInfo)
  ))
_sym_db.RegisterMessage(FrsTabInfo)


# @@protoc_insertion_point(module_scope)
