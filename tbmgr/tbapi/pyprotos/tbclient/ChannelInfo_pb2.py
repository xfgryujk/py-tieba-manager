# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ChannelInfo.proto

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
  name='tbclient/ChannelInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/ChannelInfo.proto\x12\x08tbclient\"\xbc\x02\n\x0b\x43hannelInfo\x12\x16\n\x0e\x63hannel_avatar\x18\x04 \x01(\t\x12\x15\n\rchannel_cover\x18\x03 \x01(\t\x12\x12\n\nchannel_id\x18\x01 \x01(\x04\x12\x14\n\x0c\x63hannel_name\x18\x02 \x01(\t\x12\x1b\n\x13\x63hannel_small_cover\x18\x0e \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x05 \x01(\t\x12\x12\n\nfans_count\x18\n \x01(\r\x12\x14\n\x0cis_subscribe\x18\x0c \x01(\r\x12\x10\n\x08portrait\x18\x08 \x01(\t\x12\x13\n\x0bpush_switch\x18\r \x01(\r\x12\x0f\n\x07user_id\x18\x06 \x01(\x04\x12\x11\n\tuser_name\x18\x07 \x01(\t\x12\x13\n\x0bvideo_count\x18\t \x01(\r\x12\x18\n\x10video_play_count\x18\x0b \x01(\r')
)




_CHANNELINFO = _descriptor.Descriptor(
  name='ChannelInfo',
  full_name='tbclient.ChannelInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='channel_avatar', full_name='tbclient.ChannelInfo.channel_avatar', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_cover', full_name='tbclient.ChannelInfo.channel_cover', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_id', full_name='tbclient.ChannelInfo.channel_id', index=2,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_name', full_name='tbclient.ChannelInfo.channel_name', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='channel_small_cover', full_name='tbclient.ChannelInfo.channel_small_cover', index=4,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='description', full_name='tbclient.ChannelInfo.description', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fans_count', full_name='tbclient.ChannelInfo.fans_count', index=6,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_subscribe', full_name='tbclient.ChannelInfo.is_subscribe', index=7,
      number=12, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.ChannelInfo.portrait', index=8,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='push_switch', full_name='tbclient.ChannelInfo.push_switch', index=9,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.ChannelInfo.user_id', index=10,
      number=6, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.ChannelInfo.user_name', index=11,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_count', full_name='tbclient.ChannelInfo.video_count', index=12,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_play_count', full_name='tbclient.ChannelInfo.video_play_count', index=13,
      number=11, type=13, cpp_type=3, label=1,
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
  serialized_start=41,
  serialized_end=357,
)

DESCRIPTOR.message_types_by_name['ChannelInfo'] = _CHANNELINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ChannelInfo = _reflection.GeneratedProtocolMessageType('ChannelInfo', (_message.Message,), dict(
  DESCRIPTOR = _CHANNELINFO,
  __module__ = 'tbclient.ChannelInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ChannelInfo)
  ))
_sym_db.RegisterMessage(ChannelInfo)


# @@protoc_insertion_point(module_scope)
