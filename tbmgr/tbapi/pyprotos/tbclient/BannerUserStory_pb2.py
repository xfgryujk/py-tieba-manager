# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/BannerUserStory.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import AlaLiveInfo_pb2 as tbclient_dot_AlaLiveInfo__pb2
from tbclient import UserStory_pb2 as tbclient_dot_UserStory__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/BannerUserStory.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1etbclient/BannerUserStory.proto\x12\x08tbclient\x1a\x1atbclient/AlaLiveInfo.proto\x1a\x18tbclient/UserStory.proto\"y\n\x0f\x42\x61nnerUserStory\x12\x0f\n\x07_switch\x18\x02 \x01(\r\x12,\n\rala_live_list\x18\x03 \x03(\x0b\x32\x15.tbclient.AlaLiveInfo\x12\'\n\nuser_story\x18\x01 \x03(\x0b\x32\x13.tbclient.UserStory')
  ,
  dependencies=[tbclient_dot_AlaLiveInfo__pb2.DESCRIPTOR,tbclient_dot_UserStory__pb2.DESCRIPTOR,])




_BANNERUSERSTORY = _descriptor.Descriptor(
  name='BannerUserStory',
  full_name='tbclient.BannerUserStory',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_switch', full_name='tbclient.BannerUserStory._switch', index=0,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ala_live_list', full_name='tbclient.BannerUserStory.ala_live_list', index=1,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_story', full_name='tbclient.BannerUserStory.user_story', index=2,
      number=1, type=11, cpp_type=10, label=3,
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
  serialized_start=98,
  serialized_end=219,
)

_BANNERUSERSTORY.fields_by_name['ala_live_list'].message_type = tbclient_dot_AlaLiveInfo__pb2._ALALIVEINFO
_BANNERUSERSTORY.fields_by_name['user_story'].message_type = tbclient_dot_UserStory__pb2._USERSTORY
DESCRIPTOR.message_types_by_name['BannerUserStory'] = _BANNERUSERSTORY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BannerUserStory = _reflection.GeneratedProtocolMessageType('BannerUserStory', (_message.Message,), dict(
  DESCRIPTOR = _BANNERUSERSTORY,
  __module__ = 'tbclient.BannerUserStory_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.BannerUserStory)
  ))
_sym_db.RegisterMessage(BannerUserStory)


# @@protoc_insertion_point(module_scope)
