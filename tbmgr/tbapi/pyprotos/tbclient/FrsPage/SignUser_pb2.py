# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/SignUser.proto

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
  name='tbclient/FrsPage/SignUser.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1ftbclient/FrsPage/SignUser.proto\x12\x10tbclient.FrsPage\"\x82\x02\n\x08SignUser\x12\x12\n\nc_sign_num\x18\x08 \x01(\x05\x12\x15\n\rcont_sign_num\x18\x05 \x01(\x05\x12\x1b\n\x13\x63out_total_sign_num\x18\x06 \x01(\x05\x12\x14\n\x0chun_sign_num\x18\t \x01(\x05\x12\x17\n\x0fis_org_disabled\x18\x07 \x01(\x05\x12\x12\n\nis_sign_in\x18\x02 \x01(\x05\x12\x15\n\rmiss_sign_num\x18\x0b \x01(\x05\x12\x11\n\tsign_time\x18\x04 \x01(\x05\x12\x18\n\x10total_resign_num\x18\n \x01(\x05\x12\x0f\n\x07user_id\x18\x01 \x01(\x03\x12\x16\n\x0euser_sign_rank\x18\x03 \x01(\x05')
)




_SIGNUSER = _descriptor.Descriptor(
  name='SignUser',
  full_name='tbclient.FrsPage.SignUser',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='c_sign_num', full_name='tbclient.FrsPage.SignUser.c_sign_num', index=0,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cont_sign_num', full_name='tbclient.FrsPage.SignUser.cont_sign_num', index=1,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='cout_total_sign_num', full_name='tbclient.FrsPage.SignUser.cout_total_sign_num', index=2,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='hun_sign_num', full_name='tbclient.FrsPage.SignUser.hun_sign_num', index=3,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_org_disabled', full_name='tbclient.FrsPage.SignUser.is_org_disabled', index=4,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_sign_in', full_name='tbclient.FrsPage.SignUser.is_sign_in', index=5,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='miss_sign_num', full_name='tbclient.FrsPage.SignUser.miss_sign_num', index=6,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sign_time', full_name='tbclient.FrsPage.SignUser.sign_time', index=7,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_resign_num', full_name='tbclient.FrsPage.SignUser.total_resign_num', index=8,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.FrsPage.SignUser.user_id', index=9,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_sign_rank', full_name='tbclient.FrsPage.SignUser.user_sign_rank', index=10,
      number=3, type=5, cpp_type=1, label=1,
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
  serialized_start=54,
  serialized_end=312,
)

DESCRIPTOR.message_types_by_name['SignUser'] = _SIGNUSER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignUser = _reflection.GeneratedProtocolMessageType('SignUser', (_message.Message,), dict(
  DESCRIPTOR = _SIGNUSER,
  __module__ = 'tbclient.FrsPage.SignUser_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.SignUser)
  ))
_sym_db.RegisterMessage(SignUser)


# @@protoc_insertion_point(module_scope)