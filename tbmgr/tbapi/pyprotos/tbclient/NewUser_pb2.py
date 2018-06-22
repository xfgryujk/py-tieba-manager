# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/NewUser.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import GameAttr_pb2 as tbclient_dot_GameAttr__pb2
from tbclient import Global_pb2 as tbclient_dot_Global__pb2
from tbclient import MparrProps_pb2 as tbclient_dot_MparrProps__pb2
from tbclient import NoticeMask_pb2 as tbclient_dot_NoticeMask__pb2
from tbclient import ParrProps_pb2 as tbclient_dot_ParrProps__pb2
from tbclient import ParrScores_pb2 as tbclient_dot_ParrScores__pb2
from tbclient import Props_pb2 as tbclient_dot_Props__pb2
from tbclient import Rpgoldicon_pb2 as tbclient_dot_Rpgoldicon__pb2
from tbclient import TbmallMonthIcon_pb2 as tbclient_dot_TbmallMonthIcon__pb2
from tbclient import WapRn_pb2 as tbclient_dot_WapRn__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/NewUser.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x16tbclient/NewUser.proto\x12\x08tbclient\x1a\x17tbclient/GameAttr.proto\x1a\x15tbclient/Global.proto\x1a\x19tbclient/MparrProps.proto\x1a\x19tbclient/NoticeMask.proto\x1a\x18tbclient/ParrProps.proto\x1a\x19tbclient/ParrScores.proto\x1a\x14tbclient/Props.proto\x1a\x19tbclient/Rpgoldicon.proto\x1a\x1etbclient/TbmallMonthIcon.proto\x1a\x14tbclient/WapRn.proto\"\xb1\x07\n\x07NewUser\x12!\n\x08\x61ppraise\x18\x16 \x03(\x0b\x32\x0f.tbclient.Props\x12\r\n\x05\x62g_id\x18\x11 \x01(\t\x12\x11\n\tbillboard\x18\x14 \x01(\t\x12\x0c\n\x04\x63\x61rd\x18\x07 \x01(\t\x12\x11\n\tcdn_error\x18\x1e \x01(\t\x12\x11\n\tfree_flag\x18$ \x01(\t\x12%\n\tgame_attr\x18! \x01(\x0b\x32\x12.tbclient.GameAttr\x12 \n\x06global\x18# \x01(\x0b\x32\x10.tbclient.Global\x12\x13\n\x0bis_coreuser\x18  \x01(\t\x12\x13\n\x0bis_doudizhu\x18\x1d \x01(\t\x12\x16\n\x0eis_group_owner\x18\x0c \x01(\x05\x12\x16\n\x0eis_hardworking\x18\x13 \x01(\x05\x12\x16\n\x0eis_interestman\x18\" \x01(\t\x12\x11\n\tis_member\x18\x18 \x01(\x05\x12\x11\n\tis_passer\x18\x19 \x01(\x05\x12\x15\n\ris_qun_spring\x18\x1a \x01(\x05\x12\x13\n\x0bis_shengyou\x18\x12 \x01(\x05\x12\x12\n\nis_tenyear\x18\x0b \x01(\x05\x12*\n\x0cm_parr_props\x18\t \x01(\x0b\x32\x14.tbclient.MparrProps\x12\x14\n\x0cmeizhi_level\x18\x05 \x01(\x05\x12)\n\x0bnotice_mask\x18\x1b \x03(\x0b\x32\x14.tbclient.NoticeMask\x12\r\n\x05paper\x18\x10 \x01(\t\x12\'\n\nparr_props\x18\x08 \x01(\x0b\x32\x13.tbclient.ParrProps\x12)\n\x0bparr_scores\x18\r \x01(\x0b\x32\x14.tbclient.ParrScores\x12\x15\n\rportrait_time\x18\x15 \x01(\t\x12(\n\nrpgoldicon\x18\x1c \x03(\x0b\x32\x14.tbclient.Rpgoldicon\x12\x10\n\x08superboy\x18\x06 \x01(\x05\x12\x34\n\x11tbmall_month_icon\x18\x1f \x03(\x0b\x32\x19.tbclient.TbmallMonthIcon\x12#\n\x1btbscore_repeate_finish_time\x18\x17 \x01(\t\x12\x0f\n\x07use_sig\x18\x0f \x01(\x05\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x10\n\x08user_sex\x18\x03 \x01(\x05\x12\x13\n\x0buser_status\x18\x04 \x01(\x05\x12\x11\n\tuser_type\x18\x0e \x01(\x05\x12\x1f\n\x06wap_rn\x18\n \x01(\x0b\x32\x0f.tbclient.WapRn')
  ,
  dependencies=[tbclient_dot_GameAttr__pb2.DESCRIPTOR,tbclient_dot_Global__pb2.DESCRIPTOR,tbclient_dot_MparrProps__pb2.DESCRIPTOR,tbclient_dot_NoticeMask__pb2.DESCRIPTOR,tbclient_dot_ParrProps__pb2.DESCRIPTOR,tbclient_dot_ParrScores__pb2.DESCRIPTOR,tbclient_dot_Props__pb2.DESCRIPTOR,tbclient_dot_Rpgoldicon__pb2.DESCRIPTOR,tbclient_dot_TbmallMonthIcon__pb2.DESCRIPTOR,tbclient_dot_WapRn__pb2.DESCRIPTOR,])




_NEWUSER = _descriptor.Descriptor(
  name='NewUser',
  full_name='tbclient.NewUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='appraise', full_name='tbclient.NewUser.appraise', index=0,
      number=22, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bg_id', full_name='tbclient.NewUser.bg_id', index=1,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='billboard', full_name='tbclient.NewUser.billboard', index=2,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card', full_name='tbclient.NewUser.card', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cdn_error', full_name='tbclient.NewUser.cdn_error', index=4,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_flag', full_name='tbclient.NewUser.free_flag', index=5,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_attr', full_name='tbclient.NewUser.game_attr', index=6,
      number=33, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='global', full_name='tbclient.NewUser.global', index=7,
      number=35, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_coreuser', full_name='tbclient.NewUser.is_coreuser', index=8,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_doudizhu', full_name='tbclient.NewUser.is_doudizhu', index=9,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_group_owner', full_name='tbclient.NewUser.is_group_owner', index=10,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_hardworking', full_name='tbclient.NewUser.is_hardworking', index=11,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_interestman', full_name='tbclient.NewUser.is_interestman', index=12,
      number=34, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_member', full_name='tbclient.NewUser.is_member', index=13,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_passer', full_name='tbclient.NewUser.is_passer', index=14,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_qun_spring', full_name='tbclient.NewUser.is_qun_spring', index=15,
      number=26, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_shengyou', full_name='tbclient.NewUser.is_shengyou', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_tenyear', full_name='tbclient.NewUser.is_tenyear', index=17,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='m_parr_props', full_name='tbclient.NewUser.m_parr_props', index=18,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='meizhi_level', full_name='tbclient.NewUser.meizhi_level', index=19,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notice_mask', full_name='tbclient.NewUser.notice_mask', index=20,
      number=27, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='paper', full_name='tbclient.NewUser.paper', index=21,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parr_props', full_name='tbclient.NewUser.parr_props', index=22,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='parr_scores', full_name='tbclient.NewUser.parr_scores', index=23,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait_time', full_name='tbclient.NewUser.portrait_time', index=24,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rpgoldicon', full_name='tbclient.NewUser.rpgoldicon', index=25,
      number=28, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='superboy', full_name='tbclient.NewUser.superboy', index=26,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tbmall_month_icon', full_name='tbclient.NewUser.tbmall_month_icon', index=27,
      number=31, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tbscore_repeate_finish_time', full_name='tbclient.NewUser.tbscore_repeate_finish_time', index=28,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='use_sig', full_name='tbclient.NewUser.use_sig', index=29,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.NewUser.user_id', index=30,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.NewUser.user_name', index=31,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_sex', full_name='tbclient.NewUser.user_sex', index=32,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_status', full_name='tbclient.NewUser.user_status', index=33,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_type', full_name='tbclient.NewUser.user_type', index=34,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='wap_rn', full_name='tbclient.NewUser.wap_rn', index=35,
      number=10, type=11, cpp_type=10, label=1,
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
  serialized_start=295,
  serialized_end=1240,
)

_NEWUSER.fields_by_name['appraise'].message_type = tbclient_dot_Props__pb2._PROPS
_NEWUSER.fields_by_name['game_attr'].message_type = tbclient_dot_GameAttr__pb2._GAMEATTR
_NEWUSER.fields_by_name['global'].message_type = tbclient_dot_Global__pb2._GLOBAL
_NEWUSER.fields_by_name['m_parr_props'].message_type = tbclient_dot_MparrProps__pb2._MPARRPROPS
_NEWUSER.fields_by_name['notice_mask'].message_type = tbclient_dot_NoticeMask__pb2._NOTICEMASK
_NEWUSER.fields_by_name['parr_props'].message_type = tbclient_dot_ParrProps__pb2._PARRPROPS
_NEWUSER.fields_by_name['parr_scores'].message_type = tbclient_dot_ParrScores__pb2._PARRSCORES
_NEWUSER.fields_by_name['rpgoldicon'].message_type = tbclient_dot_Rpgoldicon__pb2._RPGOLDICON
_NEWUSER.fields_by_name['tbmall_month_icon'].message_type = tbclient_dot_TbmallMonthIcon__pb2._TBMALLMONTHICON
_NEWUSER.fields_by_name['wap_rn'].message_type = tbclient_dot_WapRn__pb2._WAPRN
DESCRIPTOR.message_types_by_name['NewUser'] = _NEWUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

NewUser = _reflection.GeneratedProtocolMessageType('NewUser', (_message.Message,), dict(
  DESCRIPTOR = _NEWUSER,
  __module__ = 'tbclient.NewUser_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.NewUser)
  ))
_sym_db.RegisterMessage(NewUser)


# @@protoc_insertion_point(module_scope)
