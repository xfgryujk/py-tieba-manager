# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/EsportStatic.proto

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
  name='tbclient/EsportStatic.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1btbclient/EsportStatic.proto\x12\x08tbclient\"(\n\x0c\x45sportStatic\x12\x0b\n\x03img\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t')
)




_ESPORTSTATIC = _descriptor.Descriptor(
  name='EsportStatic',
  full_name='tbclient.EsportStatic',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='img', full_name='tbclient.EsportStatic.img', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.EsportStatic.url', index=1,
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
  serialized_start=41,
  serialized_end=81,
)

DESCRIPTOR.message_types_by_name['EsportStatic'] = _ESPORTSTATIC
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EsportStatic = _reflection.GeneratedProtocolMessageType('EsportStatic', (_message.Message,), dict(
  DESCRIPTOR = _ESPORTSTATIC,
  __module__ = 'tbclient.EsportStatic_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.EsportStatic)
  ))
_sym_db.RegisterMessage(EsportStatic)


# @@protoc_insertion_point(module_scope)