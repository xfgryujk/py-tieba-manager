# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ZhiBoInfoTW.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import HotTWThreadInfo_pb2 as tbclient_dot_HotTWThreadInfo__pb2
from tbclient import LabelInfo_pb2 as tbclient_dot_LabelInfo__pb2
from tbclient import LiveCoverStatus_pb2 as tbclient_dot_LiveCoverStatus__pb2
from tbclient import NoticeInfo_pb2 as tbclient_dot_NoticeInfo__pb2
from tbclient import User_pb2 as tbclient_dot_User__pb2
from tbclient import Zan_pb2 as tbclient_dot_Zan__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/ZhiBoInfoTW.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/ZhiBoInfoTW.proto\x12\x08tbclient\x1a\x1etbclient/HotTWThreadInfo.proto\x1a\x18tbclient/LabelInfo.proto\x1a\x1etbclient/LiveCoverStatus.proto\x1a\x19tbclient/NoticeInfo.proto\x1a\x13tbclient/User.proto\x1a\x12tbclient/Zan.proto\"\xd7\x04\n\x0bZhiBoInfoTW\x12\x0f\n\x07\x63ontent\x18\x0b \x01(\t\x12\x19\n\x11\x63opythread_remind\x18\x14 \x01(\r\x12\x10\n\x08\x66ield_ex\x18\x16 \x01(\t\x12\x10\n\x08\x66orum_id\x18\x08 \x01(\x04\x12\x12\n\nforum_name\x18\x07 \x01(\t\x12\x10\n\x08\x66req_num\x18\x13 \x01(\r\x12.\n\x0bhot_tw_info\x18\r \x02(\x0b\x32\x19.tbclient.HotTWThreadInfo\x12\x16\n\x0eis_copytwzhibo\x18\x15 \x01(\r\x12\x13\n\x0bis_headline\x18\x11 \x01(\x05\x12&\n\tlabelInfo\x18\x0e \x03(\x0b\x32\x13.tbclient.LabelInfo\x12\x1a\n\x12last_modified_time\x18\t \x01(\x04\x12\x15\n\rlivecover_src\x18\x02 \x01(\t\x12\x1b\n\x13livecover_src_bsize\x18\x03 \x01(\t\x12\x1c\n\x14livecover_src_status\x18\x0f \x01(\t\x12\x33\n\x10livecover_status\x18\x12 \x02(\x0b\x32\x19.tbclient.LiveCoverStatus\x12)\n\x0bnotice_info\x18\x10 \x02(\x0b\x32\x14.tbclient.NoticeInfo\x12\x10\n\x08post_num\x18\x04 \x01(\r\x12\x11\n\treply_num\x18\x05 \x01(\r\x12\x11\n\tthread_id\x18\x01 \x01(\x04\x12\r\n\x05title\x18\n \x01(\t\x12\x1c\n\x04user\x18\x0c \x02(\x0b\x32\x0e.tbclient.User\x12\x1a\n\x03zan\x18\x06 \x02(\x0b\x32\r.tbclient.Zan')
  ,
  dependencies=[tbclient_dot_HotTWThreadInfo__pb2.DESCRIPTOR,tbclient_dot_LabelInfo__pb2.DESCRIPTOR,tbclient_dot_LiveCoverStatus__pb2.DESCRIPTOR,tbclient_dot_NoticeInfo__pb2.DESCRIPTOR,tbclient_dot_User__pb2.DESCRIPTOR,tbclient_dot_Zan__pb2.DESCRIPTOR,])




_ZHIBOINFOTW = _descriptor.Descriptor(
  name='ZhiBoInfoTW',
  full_name='tbclient.ZhiBoInfoTW',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='tbclient.ZhiBoInfoTW.content', index=0,
      number=11, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='copythread_remind', full_name='tbclient.ZhiBoInfoTW.copythread_remind', index=1,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field_ex', full_name='tbclient.ZhiBoInfoTW.field_ex', index=2,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forum_id', full_name='tbclient.ZhiBoInfoTW.forum_id', index=3,
      number=8, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='forum_name', full_name='tbclient.ZhiBoInfoTW.forum_name', index=4,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='freq_num', full_name='tbclient.ZhiBoInfoTW.freq_num', index=5,
      number=19, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hot_tw_info', full_name='tbclient.ZhiBoInfoTW.hot_tw_info', index=6,
      number=13, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_copytwzhibo', full_name='tbclient.ZhiBoInfoTW.is_copytwzhibo', index=7,
      number=21, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_headline', full_name='tbclient.ZhiBoInfoTW.is_headline', index=8,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='labelInfo', full_name='tbclient.ZhiBoInfoTW.labelInfo', index=9,
      number=14, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_modified_time', full_name='tbclient.ZhiBoInfoTW.last_modified_time', index=10,
      number=9, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='livecover_src', full_name='tbclient.ZhiBoInfoTW.livecover_src', index=11,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='livecover_src_bsize', full_name='tbclient.ZhiBoInfoTW.livecover_src_bsize', index=12,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='livecover_src_status', full_name='tbclient.ZhiBoInfoTW.livecover_src_status', index=13,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='livecover_status', full_name='tbclient.ZhiBoInfoTW.livecover_status', index=14,
      number=18, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='notice_info', full_name='tbclient.ZhiBoInfoTW.notice_info', index=15,
      number=16, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='post_num', full_name='tbclient.ZhiBoInfoTW.post_num', index=16,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='reply_num', full_name='tbclient.ZhiBoInfoTW.reply_num', index=17,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='tbclient.ZhiBoInfoTW.thread_id', index=18,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.ZhiBoInfoTW.title', index=19,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user', full_name='tbclient.ZhiBoInfoTW.user', index=20,
      number=12, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zan', full_name='tbclient.ZhiBoInfoTW.zan', index=21,
      number=6, type=11, cpp_type=10, label=2,
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
  serialized_end=798,
)

_ZHIBOINFOTW.fields_by_name['hot_tw_info'].message_type = tbclient_dot_HotTWThreadInfo__pb2._HOTTWTHREADINFO
_ZHIBOINFOTW.fields_by_name['labelInfo'].message_type = tbclient_dot_LabelInfo__pb2._LABELINFO
_ZHIBOINFOTW.fields_by_name['livecover_status'].message_type = tbclient_dot_LiveCoverStatus__pb2._LIVECOVERSTATUS
_ZHIBOINFOTW.fields_by_name['notice_info'].message_type = tbclient_dot_NoticeInfo__pb2._NOTICEINFO
_ZHIBOINFOTW.fields_by_name['user'].message_type = tbclient_dot_User__pb2._USER
_ZHIBOINFOTW.fields_by_name['zan'].message_type = tbclient_dot_Zan__pb2._ZAN
DESCRIPTOR.message_types_by_name['ZhiBoInfoTW'] = _ZHIBOINFOTW
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ZhiBoInfoTW = _reflection.GeneratedProtocolMessageType('ZhiBoInfoTW', (_message.Message,), dict(
  DESCRIPTOR = _ZHIBOINFOTW,
  __module__ = 'tbclient.ZhiBoInfoTW_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ZhiBoInfoTW)
  ))
_sym_db.RegisterMessage(ZhiBoInfoTW)


# @@protoc_insertion_point(module_scope)
