# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/PbPage/RecommendBook.proto

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
  name='tbclient/PbPage/RecommendBook.proto',
  package='tbclient.PbPage',
  syntax='proto2',
  serialized_pb=_b('\n#tbclient/PbPage/RecommendBook.proto\x12\x0ftbclient.PbPage\"\xde\x01\n\rRecommendBook\x12\x12\n\nbook_cover\x18\x06 \x01(\t\x12\x0f\n\x07\x62ook_id\x18\x04 \x01(\t\x12\x11\n\tbook_tips\x18\x08 \x03(\t\x12\x12\n\nbook_title\x18\x07 \x01(\t\x12\x11\n\tbook_type\x18\x05 \x01(\r\x12\x13\n\x0b\x62otton_text\x18\t \x01(\t\x12\x16\n\x0erecommend_text\x18\x01 \x01(\t\x12\x16\n\x0esubscript_icon\x18\n \x01(\t\x12\x14\n\x0csuggest_text\x18\x02 \x01(\t\x12\x13\n\x0bsuggest_url\x18\x03 \x01(\t')
)




_RECOMMENDBOOK = _descriptor.Descriptor(
  name='RecommendBook',
  full_name='tbclient.PbPage.RecommendBook',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='book_cover', full_name='tbclient.PbPage.RecommendBook.book_cover', index=0,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book_id', full_name='tbclient.PbPage.RecommendBook.book_id', index=1,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book_tips', full_name='tbclient.PbPage.RecommendBook.book_tips', index=2,
      number=8, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book_title', full_name='tbclient.PbPage.RecommendBook.book_title', index=3,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='book_type', full_name='tbclient.PbPage.RecommendBook.book_type', index=4,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='botton_text', full_name='tbclient.PbPage.RecommendBook.botton_text', index=5,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='recommend_text', full_name='tbclient.PbPage.RecommendBook.recommend_text', index=6,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='subscript_icon', full_name='tbclient.PbPage.RecommendBook.subscript_icon', index=7,
      number=10, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suggest_text', full_name='tbclient.PbPage.RecommendBook.suggest_text', index=8,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='suggest_url', full_name='tbclient.PbPage.RecommendBook.suggest_url', index=9,
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
  serialized_start=57,
  serialized_end=279,
)

DESCRIPTOR.message_types_by_name['RecommendBook'] = _RECOMMENDBOOK
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RecommendBook = _reflection.GeneratedProtocolMessageType('RecommendBook', (_message.Message,), dict(
  DESCRIPTOR = _RECOMMENDBOOK,
  __module__ = 'tbclient.PbPage.RecommendBook_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.PbPage.RecommendBook)
  ))
_sym_db.RegisterMessage(RecommendBook)


# @@protoc_insertion_point(module_scope)
