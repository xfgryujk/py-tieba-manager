# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/TopNotice.proto

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
  name='tbclient/FrsPage/TopNotice.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n tbclient/FrsPage/TopNotice.proto\x12\x10tbclient.FrsPage\"J\n\tTopNotice\x12\x0e\n\x06\x61uthor\x18\x03 \x01(\t\x12\n\n\x02id\x18\x04 \x01(\x05\x12\r\n\x05title\x18\x01 \x01(\t\x12\x12\n\ntitle_link\x18\x02 \x01(\t')
)




_TOPNOTICE = _descriptor.Descriptor(
  name='TopNotice',
  full_name='tbclient.FrsPage.TopNotice',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='author', full_name='tbclient.FrsPage.TopNotice.author', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.FrsPage.TopNotice.id', index=1,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.FrsPage.TopNotice.title', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_link', full_name='tbclient.FrsPage.TopNotice.title_link', index=3,
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
  serialized_start=54,
  serialized_end=128,
)

DESCRIPTOR.message_types_by_name['TopNotice'] = _TOPNOTICE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TopNotice = _reflection.GeneratedProtocolMessageType('TopNotice', (_message.Message,), dict(
  DESCRIPTOR = _TOPNOTICE,
  __module__ = 'tbclient.FrsPage.TopNotice_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.TopNotice)
  ))
_sym_db.RegisterMessage(TopNotice)


# @@protoc_insertion_point(module_scope)
