# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PbFloor/DataReq.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import CommonReq_pb2 as tbclient_dot_CommonReq__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/PbFloor/DataReq.proto',
  package='tbclient.PbFloor',
  syntax='proto2',
  serialized_pb=_b('\n\x1etbclient/PbFloor/DataReq.proto\x12\x10tbclient.PbFloor\x1a\x18tbclient/CommonReq.proto\"\xba\x01\n\x07\x44\x61taReq\x12#\n\x06\x63ommon\x18\t \x01(\x0b\x32\x13.tbclient.CommonReq\x12\x17\n\x0fis_comm_reverse\x18\n \x01(\x05\x12\n\n\x02kz\x18\x01 \x01(\x03\x12\x0b\n\x03pid\x18\x02 \x01(\x03\x12\n\n\x02pn\x18\x04 \x01(\x05\x12\x0f\n\x07scr_dip\x18\x07 \x01(\x01\x12\r\n\x05scr_h\x18\x06 \x01(\x05\x12\r\n\x05scr_w\x18\x05 \x01(\x05\x12\x0c\n\x04spid\x18\x03 \x01(\x03\x12\x0f\n\x07st_type\x18\x08 \x01(\t')
  ,
  dependencies=[tbclient_dot_CommonReq__pb2.DESCRIPTOR,])




_DATAREQ = _descriptor.Descriptor(
  name='DataReq',
  full_name='tbclient.PbFloor.DataReq',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='common', full_name='tbclient.PbFloor.DataReq.common', index=0,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_comm_reverse', full_name='tbclient.PbFloor.DataReq.is_comm_reverse', index=1,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='kz', full_name='tbclient.PbFloor.DataReq.kz', index=2,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pid', full_name='tbclient.PbFloor.DataReq.pid', index=3,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pn', full_name='tbclient.PbFloor.DataReq.pn', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scr_dip', full_name='tbclient.PbFloor.DataReq.scr_dip', index=5,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scr_h', full_name='tbclient.PbFloor.DataReq.scr_h', index=6,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='scr_w', full_name='tbclient.PbFloor.DataReq.scr_w', index=7,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='spid', full_name='tbclient.PbFloor.DataReq.spid', index=8,
      number=3, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='st_type', full_name='tbclient.PbFloor.DataReq.st_type', index=9,
      number=8, type=9, cpp_type=9, label=1,
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
  serialized_start=79,
  serialized_end=265,
)

_DATAREQ.fields_by_name['common'].message_type = tbclient_dot_CommonReq__pb2._COMMONREQ
DESCRIPTOR.message_types_by_name['DataReq'] = _DATAREQ
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

DataReq = _reflection.GeneratedProtocolMessageType('DataReq', (_message.Message,), dict(
  DESCRIPTOR = _DATAREQ,
  __module__ = 'tbclient.PbFloor.DataReq_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PbFloor.DataReq)
  ))
_sym_db.RegisterMessage(DataReq)


# @@protoc_insertion_point(module_scope)