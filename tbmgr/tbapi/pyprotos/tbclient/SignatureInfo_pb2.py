# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/SignatureInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import Avatar_pb2 as tbclient_dot_Avatar__pb2
from tbclient import Equipment_pb2 as tbclient_dot_Equipment__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/SignatureInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1ctbclient/SignatureInfo.proto\x12\x08tbclient\x1a\x15tbclient/Avatar.proto\x1a\x18tbclient/Equipment.proto\"\xac\x01\n\rSignatureInfo\x12 \n\x06\x61vatar\x18\x05 \x01(\x0b\x32\x10.tbclient.Avatar\x12&\n\tequipment\x18\x01 \x01(\x0b\x32\x13.tbclient.Equipment\x12\x0f\n\x07game_id\x18\x02 \x01(\t\x12\x11\n\tgame_name\x18\x03 \x01(\t\x12\x0e\n\x06player\x18\x04 \x01(\t\x12\r\n\x05power\x18\x06 \x01(\t\x12\x0e\n\x06server\x18\x07 \x01(\t')
  ,
  dependencies=[tbclient_dot_Avatar__pb2.DESCRIPTOR,tbclient_dot_Equipment__pb2.DESCRIPTOR,])




_SIGNATUREINFO = _descriptor.Descriptor(
  name='SignatureInfo',
  full_name='tbclient.SignatureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='avatar', full_name='tbclient.SignatureInfo.avatar', index=0,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='equipment', full_name='tbclient.SignatureInfo.equipment', index=1,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_id', full_name='tbclient.SignatureInfo.game_id', index=2,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='game_name', full_name='tbclient.SignatureInfo.game_name', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='player', full_name='tbclient.SignatureInfo.player', index=4,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='power', full_name='tbclient.SignatureInfo.power', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='server', full_name='tbclient.SignatureInfo.server', index=6,
      number=7, type=9, cpp_type=9, label=1,
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
  serialized_start=92,
  serialized_end=264,
)

_SIGNATUREINFO.fields_by_name['avatar'].message_type = tbclient_dot_Avatar__pb2._AVATAR
_SIGNATUREINFO.fields_by_name['equipment'].message_type = tbclient_dot_Equipment__pb2._EQUIPMENT
DESCRIPTOR.message_types_by_name['SignatureInfo'] = _SIGNATUREINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SignatureInfo = _reflection.GeneratedProtocolMessageType('SignatureInfo', (_message.Message,), dict(
  DESCRIPTOR = _SIGNATUREINFO,
  __module__ = 'tbclient.SignatureInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.SignatureInfo)
  ))
_sym_db.RegisterMessage(SignatureInfo)


# @@protoc_insertion_point(module_scope)
