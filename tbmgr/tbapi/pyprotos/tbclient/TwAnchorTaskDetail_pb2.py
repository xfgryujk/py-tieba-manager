# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/TwAnchorTaskDetail.proto

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
  name='tbclient/TwAnchorTaskDetail.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n!tbclient/TwAnchorTaskDetail.proto\x12\x08tbclient\"&\n\x12TwAnchorTaskDetail\x12\x10\n\x08\x64\x65scribe\x18\x01 \x01(\t')
)




_TWANCHORTASKDETAIL = _descriptor.Descriptor(
  name='TwAnchorTaskDetail',
  full_name='tbclient.TwAnchorTaskDetail',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='describe', full_name='tbclient.TwAnchorTaskDetail.describe', index=0,
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
  serialized_start=47,
  serialized_end=85,
)

DESCRIPTOR.message_types_by_name['TwAnchorTaskDetail'] = _TWANCHORTASKDETAIL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TwAnchorTaskDetail = _reflection.GeneratedProtocolMessageType('TwAnchorTaskDetail', (_message.Message,), dict(
  DESCRIPTOR = _TWANCHORTASKDETAIL,
  __module__ = 'tbclient.TwAnchorTaskDetail_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.TwAnchorTaskDetail)
  ))
_sym_db.RegisterMessage(TwAnchorTaskDetail)


# @@protoc_insertion_point(module_scope)
