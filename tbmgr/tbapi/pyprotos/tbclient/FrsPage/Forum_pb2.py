# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/Forum.proto

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
  name='tbclient/FrsPage/Forum.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1ctbclient/FrsPage/Forum.proto\x12\x10tbclient.FrsPage\"2\n\x05\x46orum\x12\x10\n\x08\x66orum_id\x18\x01 \x01(\x03\x12\x17\n\x0flevel1_dir_name\x18\x02 \x01(\t')
)




_FORUM = _descriptor.Descriptor(
  name='Forum',
  full_name='tbclient.FrsPage.Forum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='tbclient.FrsPage.Forum.forum_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='level1_dir_name', full_name='tbclient.FrsPage.Forum.level1_dir_name', index=1,
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
  serialized_start=50,
  serialized_end=100,
)

DESCRIPTOR.message_types_by_name['Forum'] = _FORUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Forum = _reflection.GeneratedProtocolMessageType('Forum', (_message.Message,), dict(
  DESCRIPTOR = _FORUM,
  __module__ = 'tbclient.FrsPage.Forum_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.Forum)
  ))
_sym_db.RegisterMessage(Forum)


# @@protoc_insertion_point(module_scope)
