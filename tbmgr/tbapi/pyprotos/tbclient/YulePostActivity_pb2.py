# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/YulePostActivity.proto

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
  name='tbclient/YulePostActivity.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1ftbclient/YulePostActivity.proto\x12\x08tbclient\"\x97\x01\n\x10YulePostActivity\x12\x17\n\x0f\x61\x63tivity_banner\x18\x03 \x01(\t\x12\x17\n\x0f\x61\x63tivity_button\x18\x06 \x01(\t\x12\x15\n\ractivity_desc\x18\x05 \x01(\t\x12\x14\n\x0c\x61\x63tivity_url\x18\x04 \x01(\t\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x03\x12\x12\n\nstart_time\x18\x01 \x01(\x03')
)




_YULEPOSTACTIVITY = _descriptor.Descriptor(
  name='YulePostActivity',
  full_name='tbclient.YulePostActivity',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_banner', full_name='tbclient.YulePostActivity.activity_banner', index=0,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_button', full_name='tbclient.YulePostActivity.activity_button', index=1,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_desc', full_name='tbclient.YulePostActivity.activity_desc', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='activity_url', full_name='tbclient.YulePostActivity.activity_url', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='tbclient.YulePostActivity.end_time', index=4,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='start_time', full_name='tbclient.YulePostActivity.start_time', index=5,
      number=1, type=3, cpp_type=2, label=1,
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
  serialized_start=46,
  serialized_end=197,
)

DESCRIPTOR.message_types_by_name['YulePostActivity'] = _YULEPOSTACTIVITY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

YulePostActivity = _reflection.GeneratedProtocolMessageType('YulePostActivity', (_message.Message,), dict(
  DESCRIPTOR = _YULEPOSTACTIVITY,
  __module__ = 'tbclient.YulePostActivity_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.YulePostActivity)
  ))
_sym_db.RegisterMessage(YulePostActivity)


# @@protoc_insertion_point(module_scope)