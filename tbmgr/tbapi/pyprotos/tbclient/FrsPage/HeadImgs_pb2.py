# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/HeadImgs.proto

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
  name='tbclient/FrsPage/HeadImgs.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1ftbclient/FrsPage/HeadImgs.proto\x12\x10tbclient.FrsPage\"\x89\x01\n\x08HeadImgs\x12\x10\n\x08\x62tn_text\x18\x05 \x01(\t\x12\x0f\n\x07img_url\x18\x01 \x01(\t\x12\x0e\n\x06pc_url\x18\x02 \x01(\t\x12\x10\n\x08subtitle\x18\x04 \x01(\t\x12\x14\n\x0ctag_name_url\x18\x06 \x01(\t\x12\x13\n\x0btag_name_wh\x18\x07 \x01(\t\x12\r\n\x05title\x18\x03 \x01(\t')
)




_HEADIMGS = _descriptor.Descriptor(
  name='HeadImgs',
  full_name='tbclient.FrsPage.HeadImgs',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='btn_text', full_name='tbclient.FrsPage.HeadImgs.btn_text', index=0,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_url', full_name='tbclient.FrsPage.HeadImgs.img_url', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pc_url', full_name='tbclient.FrsPage.HeadImgs.pc_url', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subtitle', full_name='tbclient.FrsPage.HeadImgs.subtitle', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name_url', full_name='tbclient.FrsPage.HeadImgs.tag_name_url', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name_wh', full_name='tbclient.FrsPage.HeadImgs.tag_name_wh', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.FrsPage.HeadImgs.title', index=6,
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
  serialized_start=54,
  serialized_end=191,
)

DESCRIPTOR.message_types_by_name['HeadImgs'] = _HEADIMGS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

HeadImgs = _reflection.GeneratedProtocolMessageType('HeadImgs', (_message.Message,), dict(
  DESCRIPTOR = _HEADIMGS,
  __module__ = 'tbclient.FrsPage.HeadImgs_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.HeadImgs)
  ))
_sym_db.RegisterMessage(HeadImgs)


# @@protoc_insertion_point(module_scope)