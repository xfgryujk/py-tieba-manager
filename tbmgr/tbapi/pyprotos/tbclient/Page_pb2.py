# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/Page.proto

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
  name='tbclient/Page.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x13tbclient/Page.proto\x12\x08tbclient\"\xf9\x01\n\x04Page\x12\x13\n\x0b\x63ur_good_id\x18\x08 \x01(\x05\x12\x14\n\x0c\x63urrent_page\x18\x03 \x01(\x05\x12\x10\n\x08has_more\x18\x06 \x01(\x05\x12\x10\n\x08has_prev\x18\x07 \x01(\x05\x12\x16\n\x0elz_total_floor\x18\r \x01(\x05\x12\x0e\n\x06offset\x18\x02 \x01(\x05\x12\x11\n\tpage_size\x18\x01 \x01(\x05\x12\x0c\n\x04pnum\x18\n \x01(\x05\x12\x0f\n\x07req_num\x18\t \x01(\x05\x12\x0c\n\x04tnum\x18\x0b \x01(\x05\x12\x13\n\x0btotal_count\x18\x04 \x01(\x05\x12\x11\n\ttotal_num\x18\x0c \x01(\x05\x12\x12\n\ntotal_page\x18\x05 \x01(\x05')
)




_PAGE = _descriptor.Descriptor(
  name='Page',
  full_name='tbclient.Page',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='cur_good_id', full_name='tbclient.Page.cur_good_id', index=0,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='current_page', full_name='tbclient.Page.current_page', index=1,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_more', full_name='tbclient.Page.has_more', index=2,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_prev', full_name='tbclient.Page.has_prev', index=3,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lz_total_floor', full_name='tbclient.Page.lz_total_floor', index=4,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='offset', full_name='tbclient.Page.offset', index=5,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page_size', full_name='tbclient.Page.page_size', index=6,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pnum', full_name='tbclient.Page.pnum', index=7,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='req_num', full_name='tbclient.Page.req_num', index=8,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tnum', full_name='tbclient.Page.tnum', index=9,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='tbclient.Page.total_count', index=10,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_num', full_name='tbclient.Page.total_num', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_page', full_name='tbclient.Page.total_page', index=12,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_end=283,
)

DESCRIPTOR.message_types_by_name['Page'] = _PAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Page = _reflection.GeneratedProtocolMessageType('Page', (_message.Message,), dict(
  DESCRIPTOR = _PAGE,
  __module__ = 'tbclient.Page_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.Page)
  ))
_sym_db.RegisterMessage(Page)


# @@protoc_insertion_point(module_scope)
