# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PollOption.proto

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
  name='tbclient/PollOption.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x19tbclient/PollOption.proto\x12\x08tbclient\"B\n\nPollOption\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05image\x18\x04 \x01(\t\x12\x0b\n\x03num\x18\x02 \x01(\x03\x12\x0c\n\x04text\x18\x03 \x01(\t')
)




_POLLOPTION = _descriptor.Descriptor(
  name='PollOption',
  full_name='tbclient.PollOption',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.PollOption.id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='image', full_name='tbclient.PollOption.image', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num', full_name='tbclient.PollOption.num', index=2,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='tbclient.PollOption.text', index=3,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=39,
  serialized_end=105,
)

DESCRIPTOR.message_types_by_name['PollOption'] = _POLLOPTION
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PollOption = _reflection.GeneratedProtocolMessageType('PollOption', (_message.Message,), dict(
  DESCRIPTOR = _POLLOPTION,
  __module__ = 'tbclient.PollOption_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PollOption)
  ))
_sym_db.RegisterMessage(PollOption)


# @@protoc_insertion_point(module_scope)