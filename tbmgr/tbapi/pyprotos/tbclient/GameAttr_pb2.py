# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/GameAttr.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import SignatureInfo_pb2 as tbclient_dot_SignatureInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/GameAttr.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/GameAttr.proto\x12\x08tbclient\x1a\x1ctbclient/SignatureInfo.proto\"]\n\x08GameAttr\x12\x0f\n\x07is_open\x18\x03 \x01(\t\x12/\n\x0esignature_info\x18\x02 \x02(\x0b\x32\x17.tbclient.SignatureInfo\x12\x0f\n\x07user_id\x18\x01 \x01(\t')
  ,
  dependencies=[tbclient_dot_SignatureInfo__pb2.DESCRIPTOR,])




_GAMEATTR = _descriptor.Descriptor(
  name='GameAttr',
  full_name='tbclient.GameAttr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_open', full_name='tbclient.GameAttr.is_open', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature_info', full_name='tbclient.GameAttr.signature_info', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_id', full_name='tbclient.GameAttr.user_id', index=2,
      number=1, type=9, cpp_type=9, label=1,
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
  serialized_start=67,
  serialized_end=160,
)

_GAMEATTR.fields_by_name['signature_info'].message_type = tbclient_dot_SignatureInfo__pb2._SIGNATUREINFO
DESCRIPTOR.message_types_by_name['GameAttr'] = _GAMEATTR
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GameAttr = _reflection.GeneratedProtocolMessageType('GameAttr', (_message.Message,), dict(
  DESCRIPTOR = _GAMEATTR,
  __module__ = 'tbclient.GameAttr_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.GameAttr)
  ))
_sym_db.RegisterMessage(GameAttr)


# @@protoc_insertion_point(module_scope)
