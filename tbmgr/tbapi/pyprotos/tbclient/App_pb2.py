# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/App.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import GoodsInfo_pb2 as tbclient_dot_GoodsInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/App.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x12tbclient/App.proto\x12\x08tbclient\x1a\x18tbclient/GoodsInfo.proto\"\xb1\x04\n\x03\x41pp\x12\x0e\n\x06\x61\x62test\x18\x18 \x01(\t\x12\r\n\x05\x61\x64_id\x18\x0c \x01(\t\x12\x10\n\x08\x61pk_name\x18\x13 \x01(\t\x12\x0f\n\x07\x61pk_url\x18\x12 \x01(\t\x12\x10\n\x08\x61pp_desc\x18\x06 \x01(\t\x12\x10\n\x08\x61pp_name\x18\x05 \x01(\t\x12\x10\n\x08\x61pp_time\x18\n \x01(\x05\x12\x0c\n\x04\x63pid\x18\x17 \x01(\x05\x12\x10\n\x08\x64\x65\x65p_url\x18  \x01(\t\x12\x10\n\x08\x65xt_info\x18\x1d \x01(\t\x12\x12\n\nfirst_name\x18\x15 \x01(\t\x12\'\n\ngoods_info\x18\x1e \x03(\x0b\x32\x13.tbclient.GoodsInfo\x12\x11\n\ticon_link\x18\x04 \x01(\t\x12\x10\n\x08icon_url\x18\x03 \x01(\t\x12\n\n\x02id\x18\r \x01(\t\x12\x0f\n\x07img_url\x18\t \x01(\t\x12\x0f\n\x07ios_url\x18\x11 \x01(\t\x12\x10\n\x08loc_code\x18\x1f \x01(\t\x12\x0c\n\x04name\x18\x0e \x01(\t\x12\x0e\n\x06p_name\x18\x07 \x01(\t\x12\r\n\x05p_url\x18\x08 \x01(\t\x12\x0f\n\x07plan_id\x18\x19 \x01(\x05\x12\x0b\n\x03pos\x18\x02 \x01(\x05\x12\x10\n\x08pos_name\x18\x14 \x01(\t\x12\r\n\x05price\x18\x1b \x01(\t\x12\x13\n\x0bsecond_name\x18\x16 \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0b\n\x03url\x18\x10 \x01(\t\x12\x10\n\x08url_type\x18\x0f \x01(\x05\x12\x0f\n\x07user_id\x18\x1a \x01(\t\x12\x0e\n\x06verify\x18\x1c \x01(\t\x12\x0f\n\x07web_url\x18\x0b \x01(\t')
  ,
  dependencies=[tbclient_dot_GoodsInfo__pb2.DESCRIPTOR,])




_APP = _descriptor.Descriptor(
  name='App',
  full_name='tbclient.App',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='abtest', full_name='tbclient.App.abtest', index=0,
      number=24, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ad_id', full_name='tbclient.App.ad_id', index=1,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apk_name', full_name='tbclient.App.apk_name', index=2,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apk_url', full_name='tbclient.App.apk_url', index=3,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_desc', full_name='tbclient.App.app_desc', index=4,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_name', full_name='tbclient.App.app_name', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='app_time', full_name='tbclient.App.app_time', index=6,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cpid', full_name='tbclient.App.cpid', index=7,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='deep_url', full_name='tbclient.App.deep_url', index=8,
      number=32, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ext_info', full_name='tbclient.App.ext_info', index=9,
      number=29, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='first_name', full_name='tbclient.App.first_name', index=10,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='goods_info', full_name='tbclient.App.goods_info', index=11,
      number=30, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_link', full_name='tbclient.App.icon_link', index=12,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon_url', full_name='tbclient.App.icon_url', index=13,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.App.id', index=14,
      number=13, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_url', full_name='tbclient.App.img_url', index=15,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ios_url', full_name='tbclient.App.ios_url', index=16,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loc_code', full_name='tbclient.App.loc_code', index=17,
      number=31, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='tbclient.App.name', index=18,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_name', full_name='tbclient.App.p_name', index=19,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='p_url', full_name='tbclient.App.p_url', index=20,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='plan_id', full_name='tbclient.App.plan_id', index=21,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos', full_name='tbclient.App.pos', index=22,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pos_name', full_name='tbclient.App.pos_name', index=23,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='price', full_name='tbclient.App.price', index=24,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='second_name', full_name='tbclient.App.second_name', index=25,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tbclient.App.type', index=26,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.App.url', index=27,
      number=16, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url_type', full_name='tbclient.App.url_type', index=28,
      number=15, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.App.user_id', index=29,
      number=26, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='verify', full_name='tbclient.App.verify', index=30,
      number=28, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='web_url', full_name='tbclient.App.web_url', index=31,
      number=11, type=9, cpp_type=9, label=1,
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
  serialized_start=59,
  serialized_end=620,
)

_APP.fields_by_name['goods_info'].message_type = tbclient_dot_GoodsInfo__pb2._GOODSINFO
DESCRIPTOR.message_types_by_name['App'] = _APP
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

App = _reflection.GeneratedProtocolMessageType('App', (_message.Message,), dict(
  DESCRIPTOR = _APP,
  __module__ = 'tbclient.App_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.App)
  ))
_sym_db.RegisterMessage(App)


# @@protoc_insertion_point(module_scope)
