# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PicTextItem.proto

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
  name='tbclient/PicTextItem.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/PicTextItem.proto\x12\x08tbclient\"D\n\x0bPicTextItem\x12\x10\n\x08item_pic\x18\x01 \x01(\t\x12\x11\n\titem_text\x18\x03 \x01(\t\x12\x10\n\x08item_url\x18\x02 \x01(\t')
)




_PICTEXTITEM = _descriptor.Descriptor(
  name='PicTextItem',
  full_name='tbclient.PicTextItem',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_pic', full_name='tbclient.PicTextItem.item_pic', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_text', full_name='tbclient.PicTextItem.item_text', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='item_url', full_name='tbclient.PicTextItem.item_url', index=2,
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
  serialized_start=40,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['PicTextItem'] = _PICTEXTITEM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PicTextItem = _reflection.GeneratedProtocolMessageType('PicTextItem', (_message.Message,), dict(
  DESCRIPTOR = _PICTEXTITEM,
  __module__ = 'tbclient.PicTextItem_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PicTextItem)
  ))
_sym_db.RegisterMessage(PicTextItem)


# @@protoc_insertion_point(module_scope)
