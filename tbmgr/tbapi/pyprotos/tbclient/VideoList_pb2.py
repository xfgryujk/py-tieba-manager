# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/VideoList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import ChannelPage_pb2 as tbclient_dot_ChannelPage__pb2
from tbclient import ChannelVideoInfo_pb2 as tbclient_dot_ChannelVideoInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/VideoList.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x18tbclient/VideoList.proto\x12\x08tbclient\x1a\x1atbclient/ChannelPage.proto\x1a\x1ftbclient/ChannelVideoInfo.proto\"Z\n\tVideoList\x12(\n\x04list\x18\x01 \x03(\x0b\x32\x1a.tbclient.ChannelVideoInfo\x12#\n\x04page\x18\x02 \x01(\x0b\x32\x15.tbclient.ChannelPage')
  ,
  dependencies=[tbclient_dot_ChannelPage__pb2.DESCRIPTOR,tbclient_dot_ChannelVideoInfo__pb2.DESCRIPTOR,])




_VIDEOLIST = _descriptor.Descriptor(
  name='VideoList',
  full_name='tbclient.VideoList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='tbclient.VideoList.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='page', full_name='tbclient.VideoList.page', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_start=99,
  serialized_end=189,
)

_VIDEOLIST.fields_by_name['list'].message_type = tbclient_dot_ChannelVideoInfo__pb2._CHANNELVIDEOINFO
_VIDEOLIST.fields_by_name['page'].message_type = tbclient_dot_ChannelPage__pb2._CHANNELPAGE
DESCRIPTOR.message_types_by_name['VideoList'] = _VIDEOLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VideoList = _reflection.GeneratedProtocolMessageType('VideoList', (_message.Message,), dict(
  DESCRIPTOR = _VIDEOLIST,
  __module__ = 'tbclient.VideoList_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.VideoList)
  ))
_sym_db.RegisterMessage(VideoList)


# @@protoc_insertion_point(module_scope)
