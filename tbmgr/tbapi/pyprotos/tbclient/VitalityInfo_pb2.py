# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/VitalityInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import FrequentlyForumInfo_pb2 as tbclient_dot_FrequentlyForumInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/VitalityInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1btbclient/VitalityInfo.proto\x12\x08tbclient\x1a\"tbclient/FrequentlyForumInfo.proto\"L\n\x0cVitalityInfo\x12<\n\x15\x66requently_forum_info\x18\x01 \x01(\x0b\x32\x1d.tbclient.FrequentlyForumInfo')
  ,
  dependencies=[tbclient_dot_FrequentlyForumInfo__pb2.DESCRIPTOR,])




_VITALITYINFO = _descriptor.Descriptor(
  name='VitalityInfo',
  full_name='tbclient.VitalityInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frequently_forum_info', full_name='tbclient.VitalityInfo.frequently_forum_info', index=0,
      number=1, type=11, cpp_type=10, label=1,
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
  serialized_start=77,
  serialized_end=153,
)

_VITALITYINFO.fields_by_name['frequently_forum_info'].message_type = tbclient_dot_FrequentlyForumInfo__pb2._FREQUENTLYFORUMINFO
DESCRIPTOR.message_types_by_name['VitalityInfo'] = _VITALITYINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

VitalityInfo = _reflection.GeneratedProtocolMessageType('VitalityInfo', (_message.Message,), dict(
  DESCRIPTOR = _VITALITYINFO,
  __module__ = 'tbclient.VitalityInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.VitalityInfo)
  ))
_sym_db.RegisterMessage(VitalityInfo)


# @@protoc_insertion_point(module_scope)
