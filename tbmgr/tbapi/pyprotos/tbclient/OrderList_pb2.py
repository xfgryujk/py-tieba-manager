# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/OrderList.proto

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
  name='tbclient/OrderList.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x18tbclient/OrderList.proto\x12\x08tbclient\"\xed\x01\n\tOrderList\x12\x15\n\ractivity_desc\x18\x0f \x01(\t\x12\x14\n\x0c\x61\x63tivity_url\x18\x10 \x01(\t\x12\x13\n\x0b\x62utton_name\x18\x11 \x01(\t\x12\x13\n\x0b\x63reate_time\x18\n \x01(\x03\x12\x13\n\x0b\x66inish_time\x18\x0b \x01(\x03\x12\r\n\x05money\x18\x13 \x01(\x03\x12\x10\n\x08order_id\x18\x01 \x01(\t\x12\x12\n\npreg_field\x18\x15 \x01(\t\x12\x10\n\x08scene_id\x18\x12 \x01(\r\x12\x0e\n\x06scores\x18\x14 \x01(\x03\x12\x0e\n\x06status\x18\x07 \x01(\x05\x12\r\n\x05title\x18\x0c \x01(\t')
)




_ORDERLIST = _descriptor.Descriptor(
  name='OrderList',
  full_name='tbclient.OrderList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_desc', full_name='tbclient.OrderList.activity_desc', index=0,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_url', full_name='tbclient.OrderList.activity_url', index=1,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_name', full_name='tbclient.OrderList.button_name', index=2,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='tbclient.OrderList.create_time', index=3,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='finish_time', full_name='tbclient.OrderList.finish_time', index=4,
      number=11, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='money', full_name='tbclient.OrderList.money', index=5,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='order_id', full_name='tbclient.OrderList.order_id', index=6,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='preg_field', full_name='tbclient.OrderList.preg_field', index=7,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scene_id', full_name='tbclient.OrderList.scene_id', index=8,
      number=18, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scores', full_name='tbclient.OrderList.scores', index=9,
      number=20, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='status', full_name='tbclient.OrderList.status', index=10,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.OrderList.title', index=11,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_end=276,
)

DESCRIPTOR.message_types_by_name['OrderList'] = _ORDERLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OrderList = _reflection.GeneratedProtocolMessageType('OrderList', (_message.Message,), dict(
  DESCRIPTOR = _ORDERLIST,
  __module__ = 'tbclient.OrderList_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.OrderList)
  ))
_sym_db.RegisterMessage(OrderList)


# @@protoc_insertion_point(module_scope)
