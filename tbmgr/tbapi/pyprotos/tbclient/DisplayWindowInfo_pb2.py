# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/DisplayWindowInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import DealMedia_pb2 as tbclient_dot_DealMedia__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/DisplayWindowInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n tbclient/DisplayWindowInfo.proto\x12\x08tbclient\x1a\x18tbclient/DealMedia.proto\"\xbf\x01\n\x11\x44isplayWindowInfo\x12 \n\x03img\x18\x04 \x01(\x0b\x32\x13.tbclient.DealMedia\x12\r\n\x05intro\x18\x03 \x01(\t\x12\x12\n\nis_display\x18\x08 \x01(\x05\x12\x12\n\nproduct_id\x18\x01 \x01(\x03\x12\r\n\x05sales\x18\t \x01(\x04\x12\x10\n\x08ship_fee\x18\x07 \x01(\x04\x12\r\n\x05stock\x18\x06 \x01(\x04\x12\r\n\x05title\x18\x02 \x01(\t\x12\x12\n\nunit_price\x18\x05 \x01(\x04')
  ,
  dependencies=[tbclient_dot_DealMedia__pb2.DESCRIPTOR,])




_DISPLAYWINDOWINFO = _descriptor.Descriptor(
  name='DisplayWindowInfo',
  full_name='tbclient.DisplayWindowInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='img', full_name='tbclient.DisplayWindowInfo.img', index=0,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intro', full_name='tbclient.DisplayWindowInfo.intro', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_display', full_name='tbclient.DisplayWindowInfo.is_display', index=2,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='tbclient.DisplayWindowInfo.product_id', index=3,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sales', full_name='tbclient.DisplayWindowInfo.sales', index=4,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ship_fee', full_name='tbclient.DisplayWindowInfo.ship_fee', index=5,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stock', full_name='tbclient.DisplayWindowInfo.stock', index=6,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.DisplayWindowInfo.title', index=7,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='unit_price', full_name='tbclient.DisplayWindowInfo.unit_price', index=8,
      number=5, type=4, cpp_type=4, label=1,
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
  serialized_end=264,
)

_DISPLAYWINDOWINFO.fields_by_name['img'].message_type = tbclient_dot_DealMedia__pb2._DEALMEDIA
DESCRIPTOR.message_types_by_name['DisplayWindowInfo'] = _DISPLAYWINDOWINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DisplayWindowInfo = _reflection.GeneratedProtocolMessageType('DisplayWindowInfo', (_message.Message,), dict(
  DESCRIPTOR = _DISPLAYWINDOWINFO,
  __module__ = 'tbclient.DisplayWindowInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.DisplayWindowInfo)
  ))
_sym_db.RegisterMessage(DisplayWindowInfo)


# @@protoc_insertion_point(module_scope)
