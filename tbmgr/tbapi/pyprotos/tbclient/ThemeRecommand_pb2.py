# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ThemeRecommand.proto

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
  name='tbclient/ThemeRecommand.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1dtbclient/ThemeRecommand.proto\x12\x08tbclient\"Y\n\x0eThemeRecommand\x12\x13\n\x0b\x62utton_text\x18\x04 \x01(\t\x12\x12\n\nbutton_url\x18\x03 \x01(\t\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x10\n\x08tip_text\x18\x02 \x01(\t')
)




_THEMERECOMMAND = _descriptor.Descriptor(
  name='ThemeRecommand',
  full_name='tbclient.ThemeRecommand',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='button_text', full_name='tbclient.ThemeRecommand.button_text', index=0,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_url', full_name='tbclient.ThemeRecommand.button_url', index=1,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='icon', full_name='tbclient.ThemeRecommand.icon', index=2,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tip_text', full_name='tbclient.ThemeRecommand.tip_text', index=3,
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
  serialized_start=43,
  serialized_end=132,
)

DESCRIPTOR.message_types_by_name['ThemeRecommand'] = _THEMERECOMMAND
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThemeRecommand = _reflection.GeneratedProtocolMessageType('ThemeRecommand', (_message.Message,), dict(
  DESCRIPTOR = _THEMERECOMMAND,
  __module__ = 'tbclient.ThemeRecommand_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ThemeRecommand)
  ))
_sym_db.RegisterMessage(ThemeRecommand)


# @@protoc_insertion_point(module_scope)
