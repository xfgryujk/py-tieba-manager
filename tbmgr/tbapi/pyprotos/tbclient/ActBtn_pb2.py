# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ActBtn.proto

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
  name='tbclient/ActBtn.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x15tbclient/ActBtn.proto\x12\x08tbclient\"1\n\x06\x41\x63tBtn\x12\x0c\n\x04text\x18\x03 \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\r\x12\x0b\n\x03url\x18\x02 \x01(\t')
)




_ACTBTN = _descriptor.Descriptor(
  name='ActBtn',
  full_name='tbclient.ActBtn',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='tbclient.ActBtn.text', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tbclient.ActBtn.type', index=1,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.ActBtn.url', index=2,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=35,
  serialized_end=84,
)

DESCRIPTOR.message_types_by_name['ActBtn'] = _ACTBTN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActBtn = _reflection.GeneratedProtocolMessageType('ActBtn', (_message.Message,), dict(
  DESCRIPTOR = _ACTBTN,
  __module__ = 'tbclient.ActBtn_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ActBtn)
  ))
_sym_db.RegisterMessage(ActBtn)


# @@protoc_insertion_point(module_scope)
