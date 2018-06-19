# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/OriginThreadInfo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import Abstract_pb2 as tbclient_dot_Abstract__pb2
from tbclient import AlaLiveInfo_pb2 as tbclient_dot_AlaLiveInfo__pb2
from tbclient import Media_pb2 as tbclient_dot_Media__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/OriginThreadInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1ftbclient/OriginThreadInfo.proto\x12\x08tbclient\x1a\x17tbclient/Abstract.proto\x1a\x1atbclient/AlaLiveInfo.proto\x1a\x14tbclient/Media.proto\"\xe3\x01\n\x10OriginThreadInfo\x12%\n\t_abstract\x18\x03 \x03(\x0b\x32\x12.tbclient.Abstract\x12\'\n\x08\x61la_info\x18\x06 \x02(\x0b\x32\x15.tbclient.AlaLiveInfo\x12\x0b\n\x03\x66id\x18\x07 \x01(\x03\x12\r\n\x05\x66name\x18\x04 \x01(\t\x12\x12\n\nis_deleted\x18\t \x01(\x05\x12\x1e\n\x05media\x18\x02 \x03(\x0b\x32\x0f.tbclient.Media\x12\x13\n\x0bthread_type\x18\x08 \x01(\x05\x12\x0b\n\x03tid\x18\x05 \x01(\t\x12\r\n\x05title\x18\x01 \x01(\t')
  ,
  dependencies=[tbclient_dot_Abstract__pb2.DESCRIPTOR,tbclient_dot_AlaLiveInfo__pb2.DESCRIPTOR,tbclient_dot_Media__pb2.DESCRIPTOR,])




_ORIGINTHREADINFO = _descriptor.Descriptor(
  name='OriginThreadInfo',
  full_name='tbclient.OriginThreadInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='_abstract', full_name='tbclient.OriginThreadInfo._abstract', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ala_info', full_name='tbclient.OriginThreadInfo.ala_info', index=1,
      number=6, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fid', full_name='tbclient.OriginThreadInfo.fid', index=2,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='fname', full_name='tbclient.OriginThreadInfo.fname', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_deleted', full_name='tbclient.OriginThreadInfo.is_deleted', index=4,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='media', full_name='tbclient.OriginThreadInfo.media', index=5,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='thread_type', full_name='tbclient.OriginThreadInfo.thread_type', index=6,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tid', full_name='tbclient.OriginThreadInfo.tid', index=7,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.OriginThreadInfo.title', index=8,
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
  serialized_start=121,
  serialized_end=348,
)

_ORIGINTHREADINFO.fields_by_name['_abstract'].message_type = tbclient_dot_Abstract__pb2._ABSTRACT
_ORIGINTHREADINFO.fields_by_name['ala_info'].message_type = tbclient_dot_AlaLiveInfo__pb2._ALALIVEINFO
_ORIGINTHREADINFO.fields_by_name['media'].message_type = tbclient_dot_Media__pb2._MEDIA
DESCRIPTOR.message_types_by_name['OriginThreadInfo'] = _ORIGINTHREADINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OriginThreadInfo = _reflection.GeneratedProtocolMessageType('OriginThreadInfo', (_message.Message,), dict(
  DESCRIPTOR = _ORIGINTHREADINFO,
  __module__ = 'tbclient.OriginThreadInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.OriginThreadInfo)
  ))
_sym_db.RegisterMessage(OriginThreadInfo)


# @@protoc_insertion_point(module_scope)
