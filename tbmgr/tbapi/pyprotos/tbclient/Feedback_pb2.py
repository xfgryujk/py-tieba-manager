# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/Feedback.proto

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
  name='tbclient/Feedback.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x17tbclient/Feedback.proto\x12\x08tbclient\"4\n\x08\x46\x65\x65\x64\x62\x61\x63k\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t')
)




_FEEDBACK = _descriptor.Descriptor(
  name='Feedback',
  full_name='tbclient.Feedback',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='icon', full_name='tbclient.Feedback.icon', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.Feedback.title', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.Feedback.url', index=2,
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
  serialized_start=37,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['Feedback'] = _FEEDBACK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Feedback = _reflection.GeneratedProtocolMessageType('Feedback', (_message.Message,), dict(
  DESCRIPTOR = _FEEDBACK,
  __module__ = 'tbclient.Feedback_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.Feedback)
  ))
_sym_db.RegisterMessage(Feedback)


# @@protoc_insertion_point(module_scope)