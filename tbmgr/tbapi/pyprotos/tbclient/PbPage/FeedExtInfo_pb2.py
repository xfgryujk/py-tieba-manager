# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PbPage/FeedExtInfo.proto

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
  name='tbclient/PbPage/FeedExtInfo.proto',
  package='tbclient.PbPage',
  syntax='proto2',
  serialized_pb=_b('\n!tbclient/PbPage/FeedExtInfo.proto\x12\x0ftbclient.PbPage\"1\n\x0b\x46\x65\x65\x64\x45xtInfo\x12\x10\n\x08\x66\x65\x65\x64_bar\x18\x02 \x03(\t\x12\x10\n\x08\x66\x65\x65\x64_tab\x18\x01 \x03(\t')
)




_FEEDEXTINFO = _descriptor.Descriptor(
  name='FeedExtInfo',
  full_name='tbclient.PbPage.FeedExtInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='feed_bar', full_name='tbclient.PbPage.FeedExtInfo.feed_bar', index=0,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feed_tab', full_name='tbclient.PbPage.FeedExtInfo.feed_tab', index=1,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
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
  serialized_end=103,
)

DESCRIPTOR.message_types_by_name['FeedExtInfo'] = _FEEDEXTINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FeedExtInfo = _reflection.GeneratedProtocolMessageType('FeedExtInfo', (_message.Message,), dict(
  DESCRIPTOR = _FEEDEXTINFO,
  __module__ = 'tbclient.PbPage.FeedExtInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PbPage.FeedExtInfo)
  ))
_sym_db.RegisterMessage(FeedExtInfo)


# @@protoc_insertion_point(module_scope)
