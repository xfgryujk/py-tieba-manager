# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/TbreadDispatch.proto

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
  name='tbclient/TbreadDispatch.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1dtbclient/TbreadDispatch.proto\x12\x08tbclient\"M\n\x0eTbreadDispatch\x12\x11\n\tfloor_num\x18\x01 \x01(\t\x12\x12\n\nproduct_id\x18\x03 \x01(\t\x12\x14\n\x0cproduct_type\x18\x02 \x01(\t')
)




_TBREADDISPATCH = _descriptor.Descriptor(
  name='TbreadDispatch',
  full_name='tbclient.TbreadDispatch',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='floor_num', full_name='tbclient.TbreadDispatch.floor_num', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_id', full_name='tbclient.TbreadDispatch.product_id', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='product_type', full_name='tbclient.TbreadDispatch.product_type', index=2,
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
  serialized_start=43,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['TbreadDispatch'] = _TBREADDISPATCH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TbreadDispatch = _reflection.GeneratedProtocolMessageType('TbreadDispatch', (_message.Message,), dict(
  DESCRIPTOR = _TBREADDISPATCH,
  __module__ = 'tbclient.TbreadDispatch_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.TbreadDispatch)
  ))
_sym_db.RegisterMessage(TbreadDispatch)


# @@protoc_insertion_point(module_scope)