# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PbPage/PbPageReqIdl.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient.PbPage import DataReq_pb2 as tbclient_dot_PbPage_dot_DataReq__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/PbPage/PbPageReqIdl.proto',
  package='tbclient.PbPage',
  syntax='proto2',
  serialized_pb=_b('\n\"tbclient/PbPage/PbPageReqIdl.proto\x12\x0ftbclient.PbPage\x1a\x1dtbclient/PbPage/DataReq.proto\"6\n\x0cPbPageReqIdl\x12&\n\x04\x64\x61ta\x18\x01 \x01(\x0b\x32\x18.tbclient.PbPage.DataReq')
  ,
  dependencies=[tbclient_dot_PbPage_dot_DataReq__pb2.DESCRIPTOR,])




_PBPAGEREQIDL = _descriptor.Descriptor(
  name='PbPageReqIdl',
  full_name='tbclient.PbPage.PbPageReqIdl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='tbclient.PbPage.PbPageReqIdl.data', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=86,
  serialized_end=140,
)

_PBPAGEREQIDL.fields_by_name['data'].message_type = tbclient_dot_PbPage_dot_DataReq__pb2._DATAREQ
DESCRIPTOR.message_types_by_name['PbPageReqIdl'] = _PBPAGEREQIDL
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PbPageReqIdl = _reflection.GeneratedProtocolMessageType('PbPageReqIdl', (_message.Message,), dict(
  DESCRIPTOR = _PBPAGEREQIDL,
  __module__ = 'tbclient.PbPage.PbPageReqIdl_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PbPage.PbPageReqIdl)
  ))
_sym_db.RegisterMessage(PbPageReqIdl)


# @@protoc_insertion_point(module_scope)