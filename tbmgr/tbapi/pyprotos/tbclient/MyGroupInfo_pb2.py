# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/MyGroupInfo.proto

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
  name='tbclient/MyGroupInfo.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x1atbclient/MyGroupInfo.proto\x12\x08tbclient\"q\n\x0bMyGroupInfo\x12\x10\n\x08group_id\x18\x01 \x01(\x04\x12\x12\n\ngroup_name\x18\x02 \x01(\t\x12\x16\n\x0emax_member_num\x18\x05 \x01(\r\x12\x12\n\nmember_num\x18\x04 \x01(\r\x12\x10\n\x08portrait\x18\x03 \x01(\t')
)




_MYGROUPINFO = _descriptor.Descriptor(
  name='MyGroupInfo',
  full_name='tbclient.MyGroupInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_id', full_name='tbclient.MyGroupInfo.group_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='group_name', full_name='tbclient.MyGroupInfo.group_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max_member_num', full_name='tbclient.MyGroupInfo.max_member_num', index=2,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='member_num', full_name='tbclient.MyGroupInfo.member_num', index=3,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='portrait', full_name='tbclient.MyGroupInfo.portrait', index=4,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=40,
  serialized_end=153,
)

DESCRIPTOR.message_types_by_name['MyGroupInfo'] = _MYGROUPINFO
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

MyGroupInfo = _reflection.GeneratedProtocolMessageType('MyGroupInfo', (_message.Message,), dict(
  DESCRIPTOR = _MYGROUPINFO,
  __module__ = 'tbclient.MyGroupInfo_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.MyGroupInfo)
  ))
_sym_db.RegisterMessage(MyGroupInfo)


# @@protoc_insertion_point(module_scope)
