# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/VipCloseAd.proto

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
  name='tbclient/VipCloseAd.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/VipCloseAd.proto\x12\x08tbclient\"E\n\nVipCloseAd\x12\x13\n\x0b\x66orum_close\x18\x03 \x03(\x05\x12\x0f\n\x07is_open\x18\x01 \x01(\x05\x12\x11\n\tvip_close\x18\x02 \x01(\x05')
)




_VIPCLOSEAD = _descriptor.Descriptor(
  name='VipCloseAd',
  full_name='tbclient.VipCloseAd',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='forum_close', full_name='tbclient.VipCloseAd.forum_close', index=0,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_open', full_name='tbclient.VipCloseAd.is_open', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vip_close', full_name='tbclient.VipCloseAd.vip_close', index=2,
      number=2, type=5, cpp_type=1, label=1,
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
  serialized_start=39,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['VipCloseAd'] = _VIPCLOSEAD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VipCloseAd = _reflection.GeneratedProtocolMessageType('VipCloseAd', (_message.Message,), dict(
  DESCRIPTOR = _VIPCLOSEAD,
  __module__ = 'tbclient.VipCloseAd_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.VipCloseAd)
  ))
_sym_db.RegisterMessage(VipCloseAd)


# @@protoc_insertion_point(module_scope)