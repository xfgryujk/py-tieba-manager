# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PushStatus.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import PushType_pb2 as tbclient_dot_PushType__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/PushStatus.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/PushStatus.proto\x12\x08tbclient\x1a\x17tbclient/PushType.proto\"?\n\nPushStatus\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12!\n\x05types\x18\x02 \x03(\x0b\x32\x12.tbclient.PushType')
  ,
  dependencies=[tbclient_dot_PushType__pb2.DESCRIPTOR,])




_PUSHSTATUS = _descriptor.Descriptor(
  name='PushStatus',
  full_name='tbclient.PushStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status', full_name='tbclient.PushStatus.status', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='types', full_name='tbclient.PushStatus.types', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=64,
  serialized_end=127,
)

_PUSHSTATUS.fields_by_name['types'].message_type = tbclient_dot_PushType__pb2._PUSHTYPE
DESCRIPTOR.message_types_by_name['PushStatus'] = _PUSHSTATUS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PushStatus = _reflection.GeneratedProtocolMessageType('PushStatus', (_message.Message,), dict(
  DESCRIPTOR = _PUSHSTATUS,
  __module__ = 'tbclient.PushStatus_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PushStatus)
  ))
_sym_db.RegisterMessage(PushStatus)


# @@protoc_insertion_point(module_scope)