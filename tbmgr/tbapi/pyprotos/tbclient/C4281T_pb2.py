# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/C4281T.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import TwAnchorPKItem_pb2 as tbclient_dot_TwAnchorPKItem__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/C4281T.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x15tbclient/C4281T.proto\x12\x08tbclient\x1a\x1dtbclient/TwAnchorPKItem.proto\"E\n\x06\x43\x34\x32\x38\x31T\x12\x10\n\x08\x64\x65scribe\x18\x01 \x01(\t\x12)\n\x07pk_list\x18\x02 \x03(\x0b\x32\x18.tbclient.TwAnchorPKItem')
  ,
  dependencies=[tbclient_dot_TwAnchorPKItem__pb2.DESCRIPTOR,])




_C4281T = _descriptor.Descriptor(
  name='C4281T',
  full_name='tbclient.C4281T',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='describe', full_name='tbclient.C4281T.describe', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pk_list', full_name='tbclient.C4281T.pk_list', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=66,
  serialized_end=135,
)

_C4281T.fields_by_name['pk_list'].message_type = tbclient_dot_TwAnchorPKItem__pb2._TWANCHORPKITEM
DESCRIPTOR.message_types_by_name['C4281T'] = _C4281T
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

C4281T = _reflection.GeneratedProtocolMessageType('C4281T', (_message.Message,), dict(
  DESCRIPTOR = _C4281T,
  __module__ = 'tbclient.C4281T_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.C4281T)
  ))
_sym_db.RegisterMessage(C4281T)


# @@protoc_insertion_point(module_scope)
