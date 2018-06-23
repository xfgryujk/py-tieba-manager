# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/ParrProps.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import Level_pb2 as tbclient_dot_Level__pb2
from tbclient import Props_pb2 as tbclient_dot_Props__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/ParrProps.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x18tbclient/ParrProps.proto\x12\x08tbclient\x1a\x14tbclient/Level.proto\x1a\x14tbclient/Props.proto\"b\n\tParrProps\x12\x1e\n\x05level\x18\x02 \x01(\x0b\x32\x0f.tbclient.Level\x12\x15\n\rportrait_time\x18\x01 \x01(\x05\x12\x1e\n\x05props\x18\x03 \x03(\x0b\x32\x0f.tbclient.Props')
  ,
  dependencies=[tbclient_dot_Level__pb2.DESCRIPTOR,tbclient_dot_Props__pb2.DESCRIPTOR,])




_PARRPROPS = _descriptor.Descriptor(
  name='ParrProps',
  full_name='tbclient.ParrProps',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='level', full_name='tbclient.ParrProps.level', index=0,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait_time', full_name='tbclient.ParrProps.portrait_time', index=1,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='props', full_name='tbclient.ParrProps.props', index=2,
      number=3, type=11, cpp_type=10, label=3,
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
  serialized_start=82,
  serialized_end=180,
)

_PARRPROPS.fields_by_name['level'].message_type = tbclient_dot_Level__pb2._LEVEL
_PARRPROPS.fields_by_name['props'].message_type = tbclient_dot_Props__pb2._PROPS
DESCRIPTOR.message_types_by_name['ParrProps'] = _PARRPROPS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ParrProps = _reflection.GeneratedProtocolMessageType('ParrProps', (_message.Message,), dict(
  DESCRIPTOR = _PARRPROPS,
  __module__ = 'tbclient.ParrProps_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.ParrProps)
  ))
_sym_db.RegisterMessage(ParrProps)


# @@protoc_insertion_point(module_scope)