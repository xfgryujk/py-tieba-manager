# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/BawuTeam.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import BawuRoleDes_pb2 as tbclient_dot_BawuRoleDes__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/BawuTeam.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/BawuTeam.proto\x12\x08tbclient\x1a\x1atbclient/BawuRoleDes.proto\"L\n\x08\x42\x61wuTeam\x12-\n\x0e\x62\x61wu_team_list\x18\x02 \x03(\x0b\x32\x15.tbclient.BawuRoleDes\x12\x11\n\ttotal_num\x18\x01 \x01(\x05')
  ,
  dependencies=[tbclient_dot_BawuRoleDes__pb2.DESCRIPTOR,])




_BAWUTEAM = _descriptor.Descriptor(
  name='BawuTeam',
  full_name='tbclient.BawuTeam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bawu_team_list', full_name='tbclient.BawuTeam.bawu_team_list', index=0,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='total_num', full_name='tbclient.BawuTeam.total_num', index=1,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=65,
  serialized_end=141,
)

_BAWUTEAM.fields_by_name['bawu_team_list'].message_type = tbclient_dot_BawuRoleDes__pb2._BAWUROLEDES
DESCRIPTOR.message_types_by_name['BawuTeam'] = _BAWUTEAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BawuTeam = _reflection.GeneratedProtocolMessageType('BawuTeam', (_message.Message,), dict(
  DESCRIPTOR = _BAWUTEAM,
  __module__ = 'tbclient.BawuTeam_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.BawuTeam)
  ))
_sym_db.RegisterMessage(BawuTeam)


# @@protoc_insertion_point(module_scope)