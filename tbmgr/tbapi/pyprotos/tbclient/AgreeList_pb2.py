# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/AgreeList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import Post_pb2 as tbclient_dot_Post__pb2
from tbclient import ThreadInfo_pb2 as tbclient_dot_ThreadInfo__pb2
from tbclient import User_pb2 as tbclient_dot_User__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/AgreeList.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x18tbclient/AgreeList.proto\x12\x08tbclient\x1a\x13tbclient/Post.proto\x1a\x19tbclient/ThreadInfo.proto\x1a\x13tbclient/User.proto\"\xb2\x01\n\tAgreeList\x12\x1f\n\x07\x61greeer\x18\x08 \x01(\x0b\x32\x0e.tbclient.User\x12\n\n\x02id\x18\x07 \x01(\x04\x12\x0e\n\x06is_del\x18\x05 \x01(\x05\x12!\n\tpost_info\x18\t \x01(\x0b\x32\x0e.tbclient.Post\x12)\n\x0bthread_info\x18\x01 \x01(\x0b\x32\x14.tbclient.ThreadInfo\x12\x0c\n\x04time\x18\x04 \x01(\r\x12\x0c\n\x04type\x18\x06 \x01(\x05')
  ,
  dependencies=[tbclient_dot_Post__pb2.DESCRIPTOR,tbclient_dot_ThreadInfo__pb2.DESCRIPTOR,tbclient_dot_User__pb2.DESCRIPTOR,])




_AGREELIST = _descriptor.Descriptor(
  name='AgreeList',
  full_name='tbclient.AgreeList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='agreeer', full_name='tbclient.AgreeList.agreeer', index=0,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.AgreeList.id', index=1,
      number=7, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_del', full_name='tbclient.AgreeList.is_del', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='post_info', full_name='tbclient.AgreeList.post_info', index=3,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_info', full_name='tbclient.AgreeList.thread_info', index=4,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='tbclient.AgreeList.time', index=5,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tbclient.AgreeList.type', index=6,
      number=6, type=5, cpp_type=1, label=1,
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
  serialized_start=108,
  serialized_end=286,
)

_AGREELIST.fields_by_name['agreeer'].message_type = tbclient_dot_User__pb2._USER
_AGREELIST.fields_by_name['post_info'].message_type = tbclient_dot_Post__pb2._POST
_AGREELIST.fields_by_name['thread_info'].message_type = tbclient_dot_ThreadInfo__pb2._THREADINFO
DESCRIPTOR.message_types_by_name['AgreeList'] = _AGREELIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AgreeList = _reflection.GeneratedProtocolMessageType('AgreeList', (_message.Message,), dict(
  DESCRIPTOR = _AGREELIST,
  __module__ = 'tbclient.AgreeList_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.AgreeList)
  ))
_sym_db.RegisterMessage(AgreeList)


# @@protoc_insertion_point(module_scope)