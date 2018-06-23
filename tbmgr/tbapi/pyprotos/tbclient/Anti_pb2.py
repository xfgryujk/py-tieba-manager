# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/Anti.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import BlockPopInfo_pb2 as tbclient_dot_BlockPopInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/Anti.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x13tbclient/Anti.proto\x12\x08tbclient\x1a\x1btbclient/BlockPopInfo.proto\"\xdd\x03\n\x04\x41nti\x12.\n\x0e\x62lock_pop_info\x18\x16 \x01(\x0b\x32\x16.tbclient.BlockPopInfo\x12\x12\n\nblock_stat\x18\x06 \x01(\x05\x12\x13\n\x0b\x64\x61ys_tofree\x18\t \x01(\x05\x12\x13\n\x0b\x66orbid_flag\x18\x04 \x01(\x05\x12\x13\n\x0b\x66orbid_info\x18\x05 \x01(\t\x12\x12\n\nhas_chance\x18\n \x01(\x05\x12\x11\n\thide_stat\x18\x07 \x01(\x05\x12\x12\n\nifaddition\x18\r \x01(\x05\x12\x0e\n\x06ifpost\x18\x02 \x01(\x05\x12\x0f\n\x07ifposta\x18\x03 \x01(\x05\x12\x0f\n\x07ifvoice\x18\x0b \x01(\x05\x12\x12\n\nifxiaoying\x18\x12 \x01(\t\x12\x12\n\nneed_vcode\x18\x0e \x01(\x05\x12\x14\n\x0cpoll_message\x18\x13 \x01(\t\x12\x0b\n\x03tbs\x18\x01 \x01(\t\x12\x11\n\tuser_mute\x18\x11 \x01(\t\x12\x11\n\tvcode_md5\x18\x0f \x01(\t\x12\x15\n\rvcode_pic_url\x18\x10 \x01(\t\x12\x12\n\nvcode_stat\x18\x08 \x01(\x05\x12\x1b\n\x13video_local_message\x18\x15 \x01(\t\x12\x15\n\rvideo_message\x18\x14 \x01(\t\x12\x15\n\rvoice_message\x18\x0c \x01(\t')
  ,
  dependencies=[tbclient_dot_BlockPopInfo__pb2.DESCRIPTOR,])




_ANTI = _descriptor.Descriptor(
  name='Anti',
  full_name='tbclient.Anti',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='block_pop_info', full_name='tbclient.Anti.block_pop_info', index=0,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='block_stat', full_name='tbclient.Anti.block_stat', index=1,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='days_tofree', full_name='tbclient.Anti.days_tofree', index=2,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forbid_flag', full_name='tbclient.Anti.forbid_flag', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forbid_info', full_name='tbclient.Anti.forbid_info', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='has_chance', full_name='tbclient.Anti.has_chance', index=5,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hide_stat', full_name='tbclient.Anti.hide_stat', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ifaddition', full_name='tbclient.Anti.ifaddition', index=7,
      number=13, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ifpost', full_name='tbclient.Anti.ifpost', index=8,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ifposta', full_name='tbclient.Anti.ifposta', index=9,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ifvoice', full_name='tbclient.Anti.ifvoice', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ifxiaoying', full_name='tbclient.Anti.ifxiaoying', index=11,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_vcode', full_name='tbclient.Anti.need_vcode', index=12,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='poll_message', full_name='tbclient.Anti.poll_message', index=13,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tbs', full_name='tbclient.Anti.tbs', index=14,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_mute', full_name='tbclient.Anti.user_mute', index=15,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vcode_md5', full_name='tbclient.Anti.vcode_md5', index=16,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vcode_pic_url', full_name='tbclient.Anti.vcode_pic_url', index=17,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vcode_stat', full_name='tbclient.Anti.vcode_stat', index=18,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_local_message', full_name='tbclient.Anti.video_local_message', index=19,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_message', full_name='tbclient.Anti.video_message', index=20,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voice_message', full_name='tbclient.Anti.voice_message', index=21,
      number=12, type=9, cpp_type=9, label=1,
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
  serialized_start=63,
  serialized_end=540,
)

_ANTI.fields_by_name['block_pop_info'].message_type = tbclient_dot_BlockPopInfo__pb2._BLOCKPOPINFO
DESCRIPTOR.message_types_by_name['Anti'] = _ANTI
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Anti = _reflection.GeneratedProtocolMessageType('Anti', (_message.Message,), dict(
  DESCRIPTOR = _ANTI,
  __module__ = 'tbclient.Anti_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.Anti)
  ))
_sym_db.RegisterMessage(Anti)


# @@protoc_insertion_point(module_scope)