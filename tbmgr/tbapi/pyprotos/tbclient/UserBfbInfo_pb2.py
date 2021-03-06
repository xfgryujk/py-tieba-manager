# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/UserBfbInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import AndroidBfbSdk_pb2 as tbclient_dot_AndroidBfbSdk__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/UserBfbInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/UserBfbInfo.proto\x12\x08tbclient\x1a\x1ctbclient/AndroidBfbSdk.proto\"\x8c\x01\n\x0bUserBfbInfo\x12\x17\n\x0f\x61\x63tivity_status\x18\x01 \x01(\x05\x12\x30\n\x0f\x61ndroid_bfb_sdk\x18\x05 \x01(\x0b\x32\x17.tbclient.AndroidBfbSdk\x12\x0f\n\x07\x62\x66\x62_url\x18\x02 \x01(\t\x12\x11\n\tmaste_url\x18\x03 \x01(\t\x12\x0e\n\x06res_no\x18\x04 \x01(\x05')
  ,
  dependencies=[tbclient_dot_AndroidBfbSdk__pb2.DESCRIPTOR,])




_USERBFBINFO = _descriptor.Descriptor(
  name='UserBfbInfo',
  full_name='tbclient.UserBfbInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_status', full_name='tbclient.UserBfbInfo.activity_status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='android_bfb_sdk', full_name='tbclient.UserBfbInfo.android_bfb_sdk', index=1,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bfb_url', full_name='tbclient.UserBfbInfo.bfb_url', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='maste_url', full_name='tbclient.UserBfbInfo.maste_url', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='res_no', full_name='tbclient.UserBfbInfo.res_no', index=4,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=71,
  serialized_end=211,
)

_USERBFBINFO.fields_by_name['android_bfb_sdk'].message_type = tbclient_dot_AndroidBfbSdk__pb2._ANDROIDBFBSDK
DESCRIPTOR.message_types_by_name['UserBfbInfo'] = _USERBFBINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

UserBfbInfo = _reflection.GeneratedProtocolMessageType('UserBfbInfo', (_message.Message,), dict(
  DESCRIPTOR = _USERBFBINFO,
  __module__ = 'tbclient.UserBfbInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.UserBfbInfo)
  ))
_sym_db.RegisterMessage(UserBfbInfo)


# @@protoc_insertion_point(module_scope)
