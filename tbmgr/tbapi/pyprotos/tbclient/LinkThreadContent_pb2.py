# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/LinkThreadContent.proto

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
  name='tbclient/LinkThreadContent.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n tbclient/LinkThreadContent.proto\x12\x08tbclient\"\xa0\x01\n\x11LinkThreadContent\x12\x15\n\rlink_abstract\x18\x03 \x01(\t\x12\x19\n\x11link_head_big_pic\x18\x06 \x01(\t\x12\x15\n\rlink_head_pic\x18\x04 \x01(\t\x12\x1b\n\x13link_head_small_pic\x18\x05 \x01(\t\x12\x12\n\nlink_title\x18\x02 \x01(\t\x12\x11\n\tlink_type\x18\x01 \x01(\x05')
)




_LINKTHREADCONTENT = _descriptor.Descriptor(
  name='LinkThreadContent',
  full_name='tbclient.LinkThreadContent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='link_abstract', full_name='tbclient.LinkThreadContent.link_abstract', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_head_big_pic', full_name='tbclient.LinkThreadContent.link_head_big_pic', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_head_pic', full_name='tbclient.LinkThreadContent.link_head_pic', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_head_small_pic', full_name='tbclient.LinkThreadContent.link_head_small_pic', index=3,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_title', full_name='tbclient.LinkThreadContent.link_title', index=4,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_type', full_name='tbclient.LinkThreadContent.link_type', index=5,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=47,
  serialized_end=207,
)

DESCRIPTOR.message_types_by_name['LinkThreadContent'] = _LINKTHREADCONTENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

LinkThreadContent = _reflection.GeneratedProtocolMessageType('LinkThreadContent', (_message.Message,), dict(
  DESCRIPTOR = _LINKTHREADCONTENT,
  __module__ = 'tbclient.LinkThreadContent_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.LinkThreadContent)
  ))
_sym_db.RegisterMessage(LinkThreadContent)


# @@protoc_insertion_point(module_scope)
