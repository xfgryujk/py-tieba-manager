# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/GameInfo.proto

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
  name='tbclient/GameInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/GameInfo.proto\x12\x08tbclient\"\xde\x05\n\x08GameInfo\x12\x11\n\t_abstract\x18\x1a \x01(\t\x12\x14\n\x0c\x61ndr_pk_name\x18\x10 \x01(\t\x12\x0e\n\x06\x61pp_id\x18\x1c \x01(\r\x12\x10\n\x08\x61pple_id\x18\n \x01(\t\x12\x11\n\tbundle_id\x18\x0b \x01(\t\x12\x13\n\x0b\x63\x61tegory_id\x18\x15 \x01(\r\x12\x15\n\rcategory_name\x18\x16 \x01(\t\x12\x19\n\x11\x63\x61tegory_name_sim\x18# \x01(\t\x12\x15\n\rday_downloads\x18\x11 \x01(\r\x12\x10\n\x08\x64\x65\x61\x64line\x18\x18 \x01(\x04\x12\x12\n\neditor_rec\x18\x19 \x01(\t\x12\x11\n\tgame_desc\x18  \x01(\t\x12\x18\n\x10game_details_url\x18\x1b \x01(\t\x12\x0f\n\x07game_id\x18\x01 \x01(\t\x12\x11\n\tgame_link\x18\x08 \x01(\t\x12\x11\n\tgame_name\x18\x02 \x01(\t\x12\x10\n\x08game_pic\x18\r \x03(\t\x12\x11\n\tgame_type\x18\x03 \x01(\r\x12\x11\n\ticon_pic1\x18\x1d \x01(\t\x12\x11\n\ticon_pic2\x18\x1e \x01(\t\x12\x11\n\ticon_pic3\x18\x1f \x01(\t\x12\x10\n\x08icon_url\x18\x04 \x01(\t\x12\x11\n\tintroduce\x18\x0e \x01(\t\x12\x17\n\x0flaunchComponent\x18\" \x01(\t\x12\x18\n\x10launch_component\x18\x0f \x01(\t\x12\x0c\n\x04mark\x18\t \x01(\r\x12\x14\n\x0cpackage_link\x18\x06 \x01(\t\x12\x14\n\x0cpackage_size\x18\x07 \x01(\t\x12\x12\n\nplayer_num\x18\x05 \x01(\r\x12\x12\n\nschema_url\x18\x0c \x01(\t\x12\r\n\x05score\x18$ \x01(\r\x12\x12\n\nsecret_key\x18\x12 \x01(\t\x12\x0c\n\x04star\x18\x14 \x01(\r\x12\x17\n\x0fsubscript_color\x18! \x01(\t\x12\x19\n\x11superscript_color\x18\x13 \x01(\t\x12\x0f\n\x07version\x18\x17 \x01(\t')
)




_GAMEINFO = _descriptor.Descriptor(
  name='GameInfo',
  full_name='tbclient.GameInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_abstract', full_name='tbclient.GameInfo._abstract', index=0,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='andr_pk_name', full_name='tbclient.GameInfo.andr_pk_name', index=1,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_id', full_name='tbclient.GameInfo.app_id', index=2,
      number=28, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apple_id', full_name='tbclient.GameInfo.apple_id', index=3,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bundle_id', full_name='tbclient.GameInfo.bundle_id', index=4,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_id', full_name='tbclient.GameInfo.category_id', index=5,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_name', full_name='tbclient.GameInfo.category_name', index=6,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='category_name_sim', full_name='tbclient.GameInfo.category_name_sim', index=7,
      number=35, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='day_downloads', full_name='tbclient.GameInfo.day_downloads', index=8,
      number=17, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deadline', full_name='tbclient.GameInfo.deadline', index=9,
      number=24, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='editor_rec', full_name='tbclient.GameInfo.editor_rec', index=10,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_desc', full_name='tbclient.GameInfo.game_desc', index=11,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_details_url', full_name='tbclient.GameInfo.game_details_url', index=12,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='tbclient.GameInfo.game_id', index=13,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_link', full_name='tbclient.GameInfo.game_link', index=14,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_name', full_name='tbclient.GameInfo.game_name', index=15,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_pic', full_name='tbclient.GameInfo.game_pic', index=16,
      number=13, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_type', full_name='tbclient.GameInfo.game_type', index=17,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_pic1', full_name='tbclient.GameInfo.icon_pic1', index=18,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_pic2', full_name='tbclient.GameInfo.icon_pic2', index=19,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_pic3', full_name='tbclient.GameInfo.icon_pic3', index=20,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_url', full_name='tbclient.GameInfo.icon_url', index=21,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='introduce', full_name='tbclient.GameInfo.introduce', index=22,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='launchComponent', full_name='tbclient.GameInfo.launchComponent', index=23,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='launch_component', full_name='tbclient.GameInfo.launch_component', index=24,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mark', full_name='tbclient.GameInfo.mark', index=25,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_link', full_name='tbclient.GameInfo.package_link', index=26,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_size', full_name='tbclient.GameInfo.package_size', index=27,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player_num', full_name='tbclient.GameInfo.player_num', index=28,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='schema_url', full_name='tbclient.GameInfo.schema_url', index=29,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='tbclient.GameInfo.score', index=30,
      number=36, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='secret_key', full_name='tbclient.GameInfo.secret_key', index=31,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='star', full_name='tbclient.GameInfo.star', index=32,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscript_color', full_name='tbclient.GameInfo.subscript_color', index=33,
      number=33, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='superscript_color', full_name='tbclient.GameInfo.superscript_color', index=34,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='version', full_name='tbclient.GameInfo.version', index=35,
      number=23, type=9, cpp_type=9, label=1,
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
  serialized_start=38,
  serialized_end=772,
)

DESCRIPTOR.message_types_by_name['GameInfo'] = _GAMEINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameInfo = _reflection.GeneratedProtocolMessageType('GameInfo', (_message.Message,), dict(
  DESCRIPTOR = _GAMEINFO,
  __module__ = 'tbclient.GameInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.GameInfo)
  ))
_sym_db.RegisterMessage(GameInfo)


# @@protoc_insertion_point(module_scope)