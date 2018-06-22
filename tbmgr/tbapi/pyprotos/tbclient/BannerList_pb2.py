# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/BannerList.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import App_pb2 as tbclient_dot_App__pb2
from tbclient import FeedForumInfo_pb2 as tbclient_dot_FeedForumInfo__pb2
from tbclient import RecomTopicInfo_pb2 as tbclient_dot_RecomTopicInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/BannerList.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/BannerList.proto\x12\x08tbclient\x1a\x12tbclient/App.proto\x1a\x1ctbclient/FeedForumInfo.proto\x1a\x1dtbclient/RecomTopicInfo.proto\"\x93\x01\n\nBannerList\x12\x1a\n\x03\x61pp\x18\x01 \x03(\x0b\x32\r.tbclient.App\x12\x0f\n\x07\x61pplist\x18\x04 \x01(\t\x12+\n\nfeed_forum\x18\x02 \x03(\x0b\x32\x17.tbclient.FeedForumInfo\x12+\n\thot_topic\x18\x03 \x01(\x0b\x32\x18.tbclient.RecomTopicInfo')
  ,
  dependencies=[tbclient_dot_App__pb2.DESCRIPTOR,tbclient_dot_FeedForumInfo__pb2.DESCRIPTOR,tbclient_dot_RecomTopicInfo__pb2.DESCRIPTOR,])




_BANNERLIST = _descriptor.Descriptor(
  name='BannerList',
  full_name='tbclient.BannerList',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='app', full_name='tbclient.BannerList.app', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='applist', full_name='tbclient.BannerList.applist', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='feed_forum', full_name='tbclient.BannerList.feed_forum', index=2,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hot_topic', full_name='tbclient.BannerList.hot_topic', index=3,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=121,
  serialized_end=268,
)

_BANNERLIST.fields_by_name['app'].message_type = tbclient_dot_App__pb2._APP
_BANNERLIST.fields_by_name['feed_forum'].message_type = tbclient_dot_FeedForumInfo__pb2._FEEDFORUMINFO
_BANNERLIST.fields_by_name['hot_topic'].message_type = tbclient_dot_RecomTopicInfo__pb2._RECOMTOPICINFO
DESCRIPTOR.message_types_by_name['BannerList'] = _BANNERLIST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BannerList = _reflection.GeneratedProtocolMessageType('BannerList', (_message.Message,), dict(
  DESCRIPTOR = _BANNERLIST,
  __module__ = 'tbclient.BannerList_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.BannerList)
  ))
_sym_db.RegisterMessage(BannerList)


# @@protoc_insertion_point(module_scope)
