# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ForumDynamic.proto

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
  name='tbclient/ForumDynamic.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1btbclient/ForumDynamic.proto\x12\x08tbclient\"\xbb\x01\n\x0c\x46orumDynamic\x12\x0e\n\x06\x61vatar\x18\x03 \x01(\t\x12\x10\n\x08\x66orum_id\x18\x01 \x01(\x03\x12\x12\n\nforum_name\x18\x02 \x01(\t\x12\x0f\n\x07is_like\x18\x05 \x01(\r\x12\x14\n\x0cmember_count\x18\x06 \x01(\r\x12\x0e\n\x06slogan\x18\x04 \x01(\t\x12\x14\n\x0cthread_count\x18\x07 \x01(\r\x12\r\n\x05title\x18\x08 \x01(\t\x12\x19\n\x11user_thread_count\x18\t \x01(\r')
)




_FORUMDYNAMIC = _descriptor.Descriptor(
  name='ForumDynamic',
  full_name='tbclient.ForumDynamic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar', full_name='tbclient.ForumDynamic.avatar', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='tbclient.ForumDynamic.forum_id', index=1,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forum_name', full_name='tbclient.ForumDynamic.forum_name', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_like', full_name='tbclient.ForumDynamic.is_like', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_count', full_name='tbclient.ForumDynamic.member_count', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='slogan', full_name='tbclient.ForumDynamic.slogan', index=5,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_count', full_name='tbclient.ForumDynamic.thread_count', index=6,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.ForumDynamic.title', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_thread_count', full_name='tbclient.ForumDynamic.user_thread_count', index=8,
      number=9, type=13, cpp_type=3, label=1,
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
  serialized_start=42,
  serialized_end=229,
)

DESCRIPTOR.message_types_by_name['ForumDynamic'] = _FORUMDYNAMIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ForumDynamic = _reflection.GeneratedProtocolMessageType('ForumDynamic', (_message.Message,), dict(
  DESCRIPTOR = _FORUMDYNAMIC,
  __module__ = 'tbclient.ForumDynamic_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ForumDynamic)
  ))
_sym_db.RegisterMessage(ForumDynamic)


# @@protoc_insertion_point(module_scope)
