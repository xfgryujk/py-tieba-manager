# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ThemeSkinPropMain.proto

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
  name='tbclient/ThemeSkinPropMain.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n tbclient/ThemeSkinPropMain.proto\x12\x08tbclient\"\xc3\x02\n\x11ThemeSkinPropMain\x12\x14\n\x0c\x61\x63tivity_url\x18\n \x01(\t\x12\x1e\n\x16\x64\x61ily_privilege_status\x18\r \x01(\r\x12\x10\n\x08\x65nd_time\x18\x0e \x01(\x03\x12\x13\n\x0b\x65xample_url\x18\x03 \x01(\t\x12\x17\n\x0f\x66ree_user_level\x18\t \x01(\r\x12\x13\n\x0bis_finished\x18\x0b \x01(\x05\x12\x13\n\x0bpackage_key\x18\x0c \x01(\t\x12\x14\n\x0cpackage_size\x18\x07 \x01(\t\x12\x13\n\x0bpackage_url\x18\x06 \x01(\t\x12\x12\n\npermission\x18\x04 \x01(\t\x12\x10\n\x08props_id\x18\x01 \x01(\x05\x12\x17\n\x0fprops_state_img\x18\x05 \x01(\t\x12\x15\n\rprops_version\x18\x08 \x01(\x05\x12\r\n\x05title\x18\x02 \x01(\t')
)




_THEMESKINPROPMAIN = _descriptor.Descriptor(
  name='ThemeSkinPropMain',
  full_name='tbclient.ThemeSkinPropMain',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_url', full_name='tbclient.ThemeSkinPropMain.activity_url', index=0,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='daily_privilege_status', full_name='tbclient.ThemeSkinPropMain.daily_privilege_status', index=1,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end_time', full_name='tbclient.ThemeSkinPropMain.end_time', index=2,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='example_url', full_name='tbclient.ThemeSkinPropMain.example_url', index=3,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='free_user_level', full_name='tbclient.ThemeSkinPropMain.free_user_level', index=4,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_finished', full_name='tbclient.ThemeSkinPropMain.is_finished', index=5,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_key', full_name='tbclient.ThemeSkinPropMain.package_key', index=6,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_size', full_name='tbclient.ThemeSkinPropMain.package_size', index=7,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='package_url', full_name='tbclient.ThemeSkinPropMain.package_url', index=8,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='permission', full_name='tbclient.ThemeSkinPropMain.permission', index=9,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='props_id', full_name='tbclient.ThemeSkinPropMain.props_id', index=10,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='props_state_img', full_name='tbclient.ThemeSkinPropMain.props_state_img', index=11,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='props_version', full_name='tbclient.ThemeSkinPropMain.props_version', index=12,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.ThemeSkinPropMain.title', index=13,
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
  serialized_start=47,
  serialized_end=370,
)

DESCRIPTOR.message_types_by_name['ThemeSkinPropMain'] = _THEMESKINPROPMAIN
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ThemeSkinPropMain = _reflection.GeneratedProtocolMessageType('ThemeSkinPropMain', (_message.Message,), dict(
  DESCRIPTOR = _THEMESKINPROPMAIN,
  __module__ = 'tbclient.ThemeSkinPropMain_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ThemeSkinPropMain)
  ))
_sym_db.RegisterMessage(ThemeSkinPropMain)


# @@protoc_insertion_point(module_scope)
