# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/ForumButton.proto

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
  name='tbclient/FrsPage/ForumButton.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\"tbclient/FrsPage/ForumButton.proto\x12\x10tbclient.FrsPage\"\x1f\n\x0b\x46orumButton\x12\x10\n\x08is_blueV\x18\x01 \x01(\x05')
)




_FORUMBUTTON = _descriptor.Descriptor(
  name='ForumButton',
  full_name='tbclient.FrsPage.ForumButton',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='is_blueV', full_name='tbclient.FrsPage.ForumButton.is_blueV', index=0,
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
  serialized_start=56,
  serialized_end=87,
)

DESCRIPTOR.message_types_by_name['ForumButton'] = _FORUMBUTTON
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ForumButton = _reflection.GeneratedProtocolMessageType('ForumButton', (_message.Message,), dict(
  DESCRIPTOR = _FORUMBUTTON,
  __module__ = 'tbclient.FrsPage.ForumButton_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.ForumButton)
  ))
_sym_db.RegisterMessage(ForumButton)


# @@protoc_insertion_point(module_scope)
