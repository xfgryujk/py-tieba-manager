# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/Abstract.proto

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
  name='tbclient/Abstract.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/Abstract.proto\x12\x08tbclient\"u\n\x08\x41\x62stract\x12\x13\n\x0b\x64uring_time\x18\x06 \x01(\t\x12\x0c\n\x04link\x18\x03 \x01(\t\x12\x0b\n\x03src\x18\x04 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\n\n\x02un\x18\x05 \x01(\t\x12\x11\n\tvoice_md5\x18\x07 \x01(\t')
)




_ABSTRACT = _descriptor.Descriptor(
  name='Abstract',
  full_name='tbclient.Abstract',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='during_time', full_name='tbclient.Abstract.during_time', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='link', full_name='tbclient.Abstract.link', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='src', full_name='tbclient.Abstract.src', index=2,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='tbclient.Abstract.text', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='tbclient.Abstract.type', index=4,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='un', full_name='tbclient.Abstract.un', index=5,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='voice_md5', full_name='tbclient.Abstract.voice_md5', index=6,
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
  serialized_start=37,
  serialized_end=154,
)

DESCRIPTOR.message_types_by_name['Abstract'] = _ABSTRACT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Abstract = _reflection.GeneratedProtocolMessageType('Abstract', (_message.Message,), dict(
  DESCRIPTOR = _ABSTRACT,
  __module__ = 'tbclient.Abstract_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.Abstract)
  ))
_sym_db.RegisterMessage(Abstract)


# @@protoc_insertion_point(module_scope)
