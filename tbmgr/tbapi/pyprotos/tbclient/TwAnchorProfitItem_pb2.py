# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/TwAnchorProfitItem.proto

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
  name='tbclient/TwAnchorProfitItem.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n!tbclient/TwAnchorProfitItem.proto\x12\x08tbclient\"~\n\x12TwAnchorProfitItem\x12\x1e\n\x16\x61vailable_anchor_level\x18\x02 \x01(\r\x12\x15\n\ricon_lock_url\x18\x05 \x01(\t\x12\x17\n\x0ficon_unlock_url\x18\x04 \x01(\t\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x03 \x01(\t')
)




_TWANCHORPROFITITEM = _descriptor.Descriptor(
  name='TwAnchorProfitItem',
  full_name='tbclient.TwAnchorProfitItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='available_anchor_level', full_name='tbclient.TwAnchorProfitItem.available_anchor_level', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_lock_url', full_name='tbclient.TwAnchorProfitItem.icon_lock_url', index=1,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_unlock_url', full_name='tbclient.TwAnchorProfitItem.icon_unlock_url', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.TwAnchorProfitItem.id', index=3,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tbclient.TwAnchorProfitItem.name', index=4,
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
  serialized_start=47,
  serialized_end=173,
)

DESCRIPTOR.message_types_by_name['TwAnchorProfitItem'] = _TWANCHORPROFITITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TwAnchorProfitItem = _reflection.GeneratedProtocolMessageType('TwAnchorProfitItem', (_message.Message,), dict(
  DESCRIPTOR = _TWANCHORPROFITITEM,
  __module__ = 'tbclient.TwAnchorProfitItem_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.TwAnchorProfitItem)
  ))
_sym_db.RegisterMessage(TwAnchorProfitItem)


# @@protoc_insertion_point(module_scope)
