# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/PostTopic.proto

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
  name='tbclient/FrsPage/PostTopic.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n tbclient/FrsPage/PostTopic.proto\x12\x10tbclient.FrsPage\"7\n\tPostTopic\x12\x15\n\rcontent_topic\x18\x02 \x01(\t\x12\x13\n\x0btitle_topic\x18\x01 \x01(\t')
)




_POSTTOPIC = _descriptor.Descriptor(
  name='PostTopic',
  full_name='tbclient.FrsPage.PostTopic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content_topic', full_name='tbclient.FrsPage.PostTopic.content_topic', index=0,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title_topic', full_name='tbclient.FrsPage.PostTopic.title_topic', index=1,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_end=109,
)

DESCRIPTOR.message_types_by_name['PostTopic'] = _POSTTOPIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PostTopic = _reflection.GeneratedProtocolMessageType('PostTopic', (_message.Message,), dict(
  DESCRIPTOR = _POSTTOPIC,
  __module__ = 'tbclient.FrsPage.PostTopic_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.PostTopic)
  ))
_sym_db.RegisterMessage(PostTopic)


# @@protoc_insertion_point(module_scope)