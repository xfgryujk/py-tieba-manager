# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ActPost.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import ActHot_pb2 as tbclient_dot_ActHot__pb2
from tbclient import LinkInfo_pb2 as tbclient_dot_LinkInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/ActPost.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x16tbclient/ActPost.proto\x12\x08tbclient\x1a\x15tbclient/ActHot.proto\x1a\x17tbclient/LinkInfo.proto\"f\n\x07\x41\x63tPost\x12!\n\x07\x61\x63t_hot\x18\x01 \x03(\x0b\x32\x10.tbclient.ActHot\x12%\n\tlink_info\x18\x03 \x03(\x0b\x32\x12.tbclient.LinkInfo\x12\x11\n\tlist_head\x18\x02 \x01(\t')
  ,
  dependencies=[tbclient_dot_ActHot__pb2.DESCRIPTOR,tbclient_dot_LinkInfo__pb2.DESCRIPTOR,])




_ACTPOST = _descriptor.Descriptor(
  name='ActPost',
  full_name='tbclient.ActPost',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='act_hot', full_name='tbclient.ActPost.act_hot', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link_info', full_name='tbclient.ActPost.link_info', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='list_head', full_name='tbclient.ActPost.list_head', index=2,
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
  serialized_start=84,
  serialized_end=186,
)

_ACTPOST.fields_by_name['act_hot'].message_type = tbclient_dot_ActHot__pb2._ACTHOT
_ACTPOST.fields_by_name['link_info'].message_type = tbclient_dot_LinkInfo__pb2._LINKINFO
DESCRIPTOR.message_types_by_name['ActPost'] = _ACTPOST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActPost = _reflection.GeneratedProtocolMessageType('ActPost', (_message.Message,), dict(
  DESCRIPTOR = _ACTPOST,
  __module__ = 'tbclient.ActPost_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ActPost)
  ))
_sym_db.RegisterMessage(ActPost)


# @@protoc_insertion_point(module_scope)