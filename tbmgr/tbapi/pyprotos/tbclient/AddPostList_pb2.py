# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/AddPostList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import SubPostList_pb2 as tbclient_dot_SubPostList__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/AddPostList.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/AddPostList.proto\x12\x08tbclient\x1a\x1atbclient/SubPostList.proto\"p\n\x0b\x41\x64\x64PostList\x12,\n\radd_post_list\x18\x04 \x03(\x0b\x32\x15.tbclient.SubPostList\x12\x0b\n\x03pid\x18\x01 \x01(\x04\x12\x13\n\x0btotal_count\x18\x03 \x01(\r\x12\x11\n\ttotal_num\x18\x02 \x01(\r')
  ,
  dependencies=[tbclient_dot_SubPostList__pb2.DESCRIPTOR,])




_ADDPOSTLIST = _descriptor.Descriptor(
  name='AddPostList',
  full_name='tbclient.AddPostList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='add_post_list', full_name='tbclient.AddPostList.add_post_list', index=0,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='tbclient.AddPostList.pid', index=1,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_count', full_name='tbclient.AddPostList.total_count', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_num', full_name='tbclient.AddPostList.total_num', index=3,
      number=2, type=13, cpp_type=3, label=1,
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
  serialized_start=68,
  serialized_end=180,
)

_ADDPOSTLIST.fields_by_name['add_post_list'].message_type = tbclient_dot_SubPostList__pb2._SUBPOSTLIST
DESCRIPTOR.message_types_by_name['AddPostList'] = _ADDPOSTLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AddPostList = _reflection.GeneratedProtocolMessageType('AddPostList', (_message.Message,), dict(
  DESCRIPTOR = _ADDPOSTLIST,
  __module__ = 'tbclient.AddPostList_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.AddPostList)
  ))
_sym_db.RegisterMessage(AddPostList)


# @@protoc_insertion_point(module_scope)