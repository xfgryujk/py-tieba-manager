# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PbFloor/DataRes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import Anti_pb2 as tbclient_dot_Anti__pb2
from tbclient import Page_pb2 as tbclient_dot_Page__pb2
from tbclient import Post_pb2 as tbclient_dot_Post__pb2
from tbclient import SimpleForum_pb2 as tbclient_dot_SimpleForum__pb2
from tbclient import SubPostList_pb2 as tbclient_dot_SubPostList__pb2
from tbclient import ThreadInfo_pb2 as tbclient_dot_ThreadInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/PbFloor/DataRes.proto',
  package='tbclient.PbFloor',
  syntax='proto2',
  serialized_pb=_b('\n\x1etbclient/PbFloor/DataRes.proto\x12\x10tbclient.PbFloor\x1a\x13tbclient/Anti.proto\x1a\x13tbclient/Page.proto\x1a\x13tbclient/Post.proto\x1a\x1atbclient/SimpleForum.proto\x1a\x1atbclient/SubPostList.proto\x1a\x19tbclient/ThreadInfo.proto\"\xf1\x01\n\x07\x44\x61taRes\x12\x1c\n\x04\x61nti\x18\x02 \x01(\x0b\x32\x0e.tbclient.Anti\x12$\n\x05\x66orum\x18\x06 \x01(\x0b\x32\x15.tbclient.SimpleForum\x12\x1c\n\x04page\x18\x01 \x01(\x0b\x32\x0e.tbclient.Page\x12\x1c\n\x04post\x18\x03 \x01(\x0b\x32\x0e.tbclient.Post\x12\x13\n\x0bserver_time\x18\x07 \x01(\x05\x12+\n\x0csubpost_list\x18\x04 \x03(\x0b\x32\x15.tbclient.SubPostList\x12$\n\x06thread\x18\x05 \x01(\x0b\x32\x14.tbclient.ThreadInfo')
  ,
  dependencies=[tbclient_dot_Anti__pb2.DESCRIPTOR,tbclient_dot_Page__pb2.DESCRIPTOR,tbclient_dot_Post__pb2.DESCRIPTOR,tbclient_dot_SimpleForum__pb2.DESCRIPTOR,tbclient_dot_SubPostList__pb2.DESCRIPTOR,tbclient_dot_ThreadInfo__pb2.DESCRIPTOR,])




_DATARES = _descriptor.Descriptor(
  name='DataRes',
  full_name='tbclient.PbFloor.DataRes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='anti', full_name='tbclient.PbFloor.DataRes.anti', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forum', full_name='tbclient.PbFloor.DataRes.forum', index=1,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='tbclient.PbFloor.DataRes.page', index=2,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='post', full_name='tbclient.PbFloor.DataRes.post', index=3,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server_time', full_name='tbclient.PbFloor.DataRes.server_time', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subpost_list', full_name='tbclient.PbFloor.DataRes.subpost_list', index=5,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread', full_name='tbclient.PbFloor.DataRes.thread', index=6,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=199,
  serialized_end=440,
)

_DATARES.fields_by_name['anti'].message_type = tbclient_dot_Anti__pb2._ANTI
_DATARES.fields_by_name['forum'].message_type = tbclient_dot_SimpleForum__pb2._SIMPLEFORUM
_DATARES.fields_by_name['page'].message_type = tbclient_dot_Page__pb2._PAGE
_DATARES.fields_by_name['post'].message_type = tbclient_dot_Post__pb2._POST
_DATARES.fields_by_name['subpost_list'].message_type = tbclient_dot_SubPostList__pb2._SUBPOSTLIST
_DATARES.fields_by_name['thread'].message_type = tbclient_dot_ThreadInfo__pb2._THREADINFO
DESCRIPTOR.message_types_by_name['DataRes'] = _DATARES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataRes = _reflection.GeneratedProtocolMessageType('DataRes', (_message.Message,), dict(
  DESCRIPTOR = _DATARES,
  __module__ = 'tbclient.PbFloor.DataRes_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PbFloor.DataRes)
  ))
_sym_db.RegisterMessage(DataRes)


# @@protoc_insertion_point(module_scope)
