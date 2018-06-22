# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/GoodsInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import AdCloseInfo_pb2 as tbclient_dot_AdCloseInfo__pb2
from tbclient import ThreadPicList_pb2 as tbclient_dot_ThreadPicList__pb2
from tbclient import VideoInfo_pb2 as tbclient_dot_VideoInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/GoodsInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x18tbclient/GoodsInfo.proto\x12\x08tbclient\x1a\x1atbclient/AdCloseInfo.proto\x1a\x1ctbclient/ThreadPicList.proto\x1a\x18tbclient/VideoInfo.proto\"\x9d\x05\n\tGoodsInfo\x12\x11\n\tad_source\x18\x18 \x01(\t\x12\x12\n\nbrand_icon\x18\x1b \x01(\t\x12\x15\n\rbrand_icon_wh\x18\x1c \x01(\t\x12\x13\n\x0b\x62utton_text\x18\r \x01(\t\x12\x12\n\nbutton_url\x18\x17 \x01(\t\x12\x11\n\tcard_desc\x18\x0e \x01(\t\x12\x10\n\x08\x63\x61rd_tag\x18\x0f \x01(\t\x12)\n\nclose_info\x18\x1d \x01(\x0b\x32\x15.tbclient.AdCloseInfo\x12\x13\n\x0bgoods_style\x18\x07 \x01(\x05\x12\x0e\n\x06height\x18\x11 \x01(\x05\x12\n\n\x02id\x18\x01 \x01(\x05\x12\x15\n\rlabel_measure\x18\x12 \x01(\x05\x12\x12\n\nlabel_text\x18\n \x01(\t\x12\x15\n\rlabel_visible\x18\t \x01(\x05\x12\x11\n\tlego_card\x18\x14 \x01(\t\x12\x17\n\x0fpop_window_text\x18\x06 \x01(\t\x12\x12\n\nrank_level\x18\x0b \x01(\x05\x12\x10\n\x08tag_name\x18\x16 \x01(\t\x12\x14\n\x0ctag_name_url\x18\x19 \x01(\t\x12\x13\n\x0btag_name_wh\x18\x1a \x01(\t\x12\x16\n\x0ethread_content\x18\x13 \x01(\t\x12\x12\n\nthread_pic\x18\x05 \x01(\t\x12\x30\n\x0fthread_pic_list\x18\x08 \x03(\x0b\x32\x17.tbclient.ThreadPicList\x12\x14\n\x0cthread_title\x18\x04 \x01(\t\x12\x13\n\x0bthread_type\x18\x0c \x01(\t\x12\x11\n\tuser_name\x18\x02 \x01(\t\x12\x15\n\ruser_portrait\x18\x03 \x01(\t\x12\'\n\nvideo_info\x18\x15 \x01(\x0b\x32\x13.tbclient.VideoInfo\x12\r\n\x05width\x18\x10 \x01(\x05')
  ,
  dependencies=[tbclient_dot_AdCloseInfo__pb2.DESCRIPTOR,tbclient_dot_ThreadPicList__pb2.DESCRIPTOR,tbclient_dot_VideoInfo__pb2.DESCRIPTOR,])




_GOODSINFO = _descriptor.Descriptor(
  name='GoodsInfo',
  full_name='tbclient.GoodsInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='ad_source', full_name='tbclient.GoodsInfo.ad_source', index=0,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brand_icon', full_name='tbclient.GoodsInfo.brand_icon', index=1,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='brand_icon_wh', full_name='tbclient.GoodsInfo.brand_icon_wh', index=2,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_text', full_name='tbclient.GoodsInfo.button_text', index=3,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_url', full_name='tbclient.GoodsInfo.button_url', index=4,
      number=23, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_desc', full_name='tbclient.GoodsInfo.card_desc', index=5,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='card_tag', full_name='tbclient.GoodsInfo.card_tag', index=6,
      number=15, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='close_info', full_name='tbclient.GoodsInfo.close_info', index=7,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goods_style', full_name='tbclient.GoodsInfo.goods_style', index=8,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='tbclient.GoodsInfo.height', index=9,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.GoodsInfo.id', index=10,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_measure', full_name='tbclient.GoodsInfo.label_measure', index=11,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_text', full_name='tbclient.GoodsInfo.label_text', index=12,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='label_visible', full_name='tbclient.GoodsInfo.label_visible', index=13,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lego_card', full_name='tbclient.GoodsInfo.lego_card', index=14,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pop_window_text', full_name='tbclient.GoodsInfo.pop_window_text', index=15,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank_level', full_name='tbclient.GoodsInfo.rank_level', index=16,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name', full_name='tbclient.GoodsInfo.tag_name', index=17,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name_url', full_name='tbclient.GoodsInfo.tag_name_url', index=18,
      number=25, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tag_name_wh', full_name='tbclient.GoodsInfo.tag_name_wh', index=19,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_content', full_name='tbclient.GoodsInfo.thread_content', index=20,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_pic', full_name='tbclient.GoodsInfo.thread_pic', index=21,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_pic_list', full_name='tbclient.GoodsInfo.thread_pic_list', index=22,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_title', full_name='tbclient.GoodsInfo.thread_title', index=23,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_type', full_name='tbclient.GoodsInfo.thread_type', index=24,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.GoodsInfo.user_name', index=25,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_portrait', full_name='tbclient.GoodsInfo.user_portrait', index=26,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_info', full_name='tbclient.GoodsInfo.video_info', index=27,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='tbclient.GoodsInfo.width', index=28,
      number=16, type=5, cpp_type=1, label=1,
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
  serialized_start=123,
  serialized_end=792,
)

_GOODSINFO.fields_by_name['close_info'].message_type = tbclient_dot_AdCloseInfo__pb2._ADCLOSEINFO
_GOODSINFO.fields_by_name['thread_pic_list'].message_type = tbclient_dot_ThreadPicList__pb2._THREADPICLIST
_GOODSINFO.fields_by_name['video_info'].message_type = tbclient_dot_VideoInfo__pb2._VIDEOINFO
DESCRIPTOR.message_types_by_name['GoodsInfo'] = _GOODSINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GoodsInfo = _reflection.GeneratedProtocolMessageType('GoodsInfo', (_message.Message,), dict(
  DESCRIPTOR = _GOODSINFO,
  __module__ = 'tbclient.GoodsInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.GoodsInfo)
  ))
_sym_db.RegisterMessage(GoodsInfo)


# @@protoc_insertion_point(module_scope)
