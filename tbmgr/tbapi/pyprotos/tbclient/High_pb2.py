# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/High.proto

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
  name='tbclient/High.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x13tbclient/High.proto\x12\x08tbclient\"\xbd\x01\n\x04High\x12\x10\n\x08\x61lbum_id\x18\x01 \x01(\x04\x12\x13\n\x0b\x63reate_time\x18\x05 \x01(\r\x12\x0b\n\x03hid\x18\x02 \x01(\x04\x12\x0f\n\x07num_cai\x18\x07 \x01(\r\x12\x0f\n\x07num_zan\x18\x06 \x01(\r\x12\x0f\n\x07pic_url\x18\x04 \x01(\t\x12\x10\n\x08portrait\x18\n \x01(\t\x12\x0c\n\x04type\x18\t \x01(\r\x12\x0b\n\x03uid\x18\x03 \x01(\x04\x12\x11\n\tuser_name\x18\x0b \x01(\t\x12\x0e\n\x06weight\x18\x08 \x01(\r')
)




_HIGH = _descriptor.Descriptor(
  name='High',
  full_name='tbclient.High',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='album_id', full_name='tbclient.High.album_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='create_time', full_name='tbclient.High.create_time', index=1,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hid', full_name='tbclient.High.hid', index=2,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_cai', full_name='tbclient.High.num_cai', index=3,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_zan', full_name='tbclient.High.num_zan', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pic_url', full_name='tbclient.High.pic_url', index=5,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.High.portrait', index=6,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tbclient.High.type', index=7,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='uid', full_name='tbclient.High.uid', index=8,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.High.user_name', index=9,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='tbclient.High.weight', index=10,
      number=8, type=13, cpp_type=3, label=1,
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
  serialized_start=34,
  serialized_end=223,
)

DESCRIPTOR.message_types_by_name['High'] = _HIGH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

High = _reflection.GeneratedProtocolMessageType('High', (_message.Message,), dict(
  DESCRIPTOR = _HIGH,
  __module__ = 'tbclient.High_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.High)
  ))
_sym_db.RegisterMessage(High)


# @@protoc_insertion_point(module_scope)
