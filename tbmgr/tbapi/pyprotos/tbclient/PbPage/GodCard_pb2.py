# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PbPage/GodCard.proto

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
  name='tbclient/PbPage/GodCard.proto',
  package='tbclient.PbPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1dtbclient/PbPage/GodCard.proto\x12\x0ftbclient.PbPage\"\x9b\x01\n\x07GodCard\x12\x13\n\x0b\x62utton_text\x18\x06 \x01(\t\x12\x12\n\nbutton_url\x18\x07 \x01(\t\x12\x0f\n\x07pic_url\x18\x05 \x01(\t\x12\x10\n\x08portrait\x18\x02 \x01(\t\x12\x12\n\nshow_floor\x18\x08 \x01(\r\x12\x0c\n\x04text\x18\x04 \x01(\t\x12\x0f\n\x07time_ex\x18\x03 \x01(\t\x12\x11\n\tuser_name\x18\x01 \x01(\t')
)




_GODCARD = _descriptor.Descriptor(
  name='GodCard',
  full_name='tbclient.PbPage.GodCard',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='button_text', full_name='tbclient.PbPage.GodCard.button_text', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='button_url', full_name='tbclient.PbPage.GodCard.button_url', index=1,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pic_url', full_name='tbclient.PbPage.GodCard.pic_url', index=2,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.PbPage.GodCard.portrait', index=3,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='show_floor', full_name='tbclient.PbPage.GodCard.show_floor', index=4,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='tbclient.PbPage.GodCard.text', index=5,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_ex', full_name='tbclient.PbPage.GodCard.time_ex', index=6,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_name', full_name='tbclient.PbPage.GodCard.user_name', index=7,
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
  serialized_start=51,
  serialized_end=206,
)

DESCRIPTOR.message_types_by_name['GodCard'] = _GODCARD
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

GodCard = _reflection.GeneratedProtocolMessageType('GodCard', (_message.Message,), dict(
  DESCRIPTOR = _GODCARD,
  __module__ = 'tbclient.PbPage.GodCard_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PbPage.GodCard)
  ))
_sym_db.RegisterMessage(GodCard)


# @@protoc_insertion_point(module_scope)
