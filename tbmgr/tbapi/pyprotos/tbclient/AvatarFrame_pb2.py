# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/AvatarFrame.proto

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
  name='tbclient/AvatarFrame.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/AvatarFrame.proto\x12\x08tbclient\"1\n\x0b\x41vatarFrame\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x05\x12\x10\n\x08props_id\x18\x01 \x01(\x05')
)




_AVATARFRAME = _descriptor.Descriptor(
  name='AvatarFrame',
  full_name='tbclient.AvatarFrame',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='end_time', full_name='tbclient.AvatarFrame.end_time', index=0,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='props_id', full_name='tbclient.AvatarFrame.props_id', index=1,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=40,
  serialized_end=89,
)

DESCRIPTOR.message_types_by_name['AvatarFrame'] = _AVATARFRAME
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AvatarFrame = _reflection.GeneratedProtocolMessageType('AvatarFrame', (_message.Message,), dict(
  DESCRIPTOR = _AVATARFRAME,
  __module__ = 'tbclient.AvatarFrame_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.AvatarFrame)
  ))
_sym_db.RegisterMessage(AvatarFrame)


# @@protoc_insertion_point(module_scope)
