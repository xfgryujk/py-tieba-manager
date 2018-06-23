# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/FrsPage/StarRank.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient.FrsPage import StarContriRecord_pb2 as tbclient_dot_FrsPage_dot_StarContriRecord__pb2
from tbclient.FrsPage import StarTaskInfo_pb2 as tbclient_dot_FrsPage_dot_StarTaskInfo__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/FrsPage/StarRank.proto',
  package='tbclient.FrsPage',
  syntax='proto2',
  serialized_pb=_b('\n\x1ftbclient/FrsPage/StarRank.proto\x12\x10tbclient.FrsPage\x1a\'tbclient/FrsPage/StarContriRecord.proto\x1a#tbclient/FrsPage/StarTaskInfo.proto\"\x90\x02\n\x08StarRank\x12>\n\x12\x63ontri_record_list\x18\x03 \x03(\x0b\x32\".tbclient.FrsPage.StarContriRecord\x12\x11\n\trank_name\x18\x01 \x01(\t\x12\x14\n\x0crank_ranking\x18\x02 \x01(\x05\x12\x0b\n\x03url\x18\x08 \x01(\t\x12\x19\n\x11user_contri_score\x18\x04 \x01(\x05\x12!\n\x19user_current_score_notice\x18\x07 \x01(\t\x12\x36\n\x0euser_task_info\x18\x06 \x03(\x0b\x32\x1e.tbclient.FrsPage.StarTaskInfo\x12\x18\n\x10user_task_notice\x18\x05 \x01(\t')
  ,
  dependencies=[tbclient_dot_FrsPage_dot_StarContriRecord__pb2.DESCRIPTOR,tbclient_dot_FrsPage_dot_StarTaskInfo__pb2.DESCRIPTOR,])




_STARRANK = _descriptor.Descriptor(
  name='StarRank',
  full_name='tbclient.FrsPage.StarRank',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contri_record_list', full_name='tbclient.FrsPage.StarRank.contri_record_list', index=0,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank_name', full_name='tbclient.FrsPage.StarRank.rank_name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rank_ranking', full_name='tbclient.FrsPage.StarRank.rank_ranking', index=2,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='url', full_name='tbclient.FrsPage.StarRank.url', index=3,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_contri_score', full_name='tbclient.FrsPage.StarRank.user_contri_score', index=4,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_current_score_notice', full_name='tbclient.FrsPage.StarRank.user_current_score_notice', index=5,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_task_info', full_name='tbclient.FrsPage.StarRank.user_task_info', index=6,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='user_task_notice', full_name='tbclient.FrsPage.StarRank.user_task_notice', index=7,
      number=5, type=9, cpp_type=9, label=1,
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
  serialized_start=132,
  serialized_end=404,
)

_STARRANK.fields_by_name['contri_record_list'].message_type = tbclient_dot_FrsPage_dot_StarContriRecord__pb2._STARCONTRIRECORD
_STARRANK.fields_by_name['user_task_info'].message_type = tbclient_dot_FrsPage_dot_StarTaskInfo__pb2._STARTASKINFO
DESCRIPTOR.message_types_by_name['StarRank'] = _STARRANK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

StarRank = _reflection.GeneratedProtocolMessageType('StarRank', (_message.Message,), dict(
  DESCRIPTOR = _STARRANK,
  __module__ = 'tbclient.FrsPage.StarRank_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.FrsPage.StarRank)
  ))
_sym_db.RegisterMessage(StarRank)


# @@protoc_insertion_point(module_scope)