# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/DealWindow.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import DisplayWindowInfo_pb2 as tbclient_dot_DisplayWindowInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/DealWindow.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/DealWindow.proto\x12\x08tbclient\x1a tbclient/DisplayWindowInfo.proto\"F\n\nDealWindow\x12)\n\x04list\x18\x01 \x03(\x0b\x32\x1b.tbclient.DisplayWindowInfo\x12\r\n\x05total\x18\x02 \x01(\x04')
  ,
  dependencies=[tbclient_dot_DisplayWindowInfo__pb2.DESCRIPTOR,])




_DEALWINDOW = _descriptor.Descriptor(
  name='DealWindow',
  full_name='tbclient.DealWindow',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='tbclient.DealWindow.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total', full_name='tbclient.DealWindow.total', index=1,
      number=2, type=4, cpp_type=4, label=1,
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
  serialized_start=73,
  serialized_end=143,
)

_DEALWINDOW.fields_by_name['list'].message_type = tbclient_dot_DisplayWindowInfo__pb2._DISPLAYWINDOWINFO
DESCRIPTOR.message_types_by_name['DealWindow'] = _DEALWINDOW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DealWindow = _reflection.GeneratedProtocolMessageType('DealWindow', (_message.Message,), dict(
  DESCRIPTOR = _DEALWINDOW,
  __module__ = 'tbclient.DealWindow_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.DealWindow)
  ))
_sym_db.RegisterMessage(DealWindow)


# @@protoc_insertion_point(module_scope)
