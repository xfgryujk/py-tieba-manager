# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tbclient/Post.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from tbclient import ActPost_pb2 as tbclient_dot_ActPost__pb2
from tbclient import AddPostList_pb2 as tbclient_dot_AddPostList__pb2
from tbclient import Agree_pb2 as tbclient_dot_Agree__pb2
from tbclient import DealInfo_pb2 as tbclient_dot_DealInfo__pb2
from tbclient import Lbs_pb2 as tbclient_dot_Lbs__pb2
from tbclient import OriginThreadInfo_pb2 as tbclient_dot_OriginThreadInfo__pb2
from tbclient import PbContent_pb2 as tbclient_dot_PbContent__pb2
from tbclient import PbPostZan_pb2 as tbclient_dot_PbPostZan__pb2
from tbclient import PbPresent_pb2 as tbclient_dot_PbPresent__pb2
from tbclient import SignatureData_pb2 as tbclient_dot_SignatureData__pb2
from tbclient import SimpleForum_pb2 as tbclient_dot_SimpleForum__pb2
from tbclient import SkinInfo_pb2 as tbclient_dot_SkinInfo__pb2
from tbclient import SubPost_pb2 as tbclient_dot_SubPost__pb2
from tbclient import TPointPost_pb2 as tbclient_dot_TPointPost__pb2
from tbclient import TailInfo_pb2 as tbclient_dot_TailInfo__pb2
from tbclient import TogetherHi_pb2 as tbclient_dot_TogetherHi__pb2
from tbclient import User_pb2 as tbclient_dot_User__pb2
from tbclient import VideoInfo_pb2 as tbclient_dot_VideoInfo__pb2
from tbclient import Zan_pb2 as tbclient_dot_Zan__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='tbclient/Post.proto',
  package='tbclient',
  syntax='proto2',
  serialized_pb=_b('\n\x13tbclient/Post.proto\x12\x08tbclient\x1a\x16tbclient/ActPost.proto\x1a\x1atbclient/AddPostList.proto\x1a\x14tbclient/Agree.proto\x1a\x17tbclient/DealInfo.proto\x1a\x12tbclient/Lbs.proto\x1a\x1ftbclient/OriginThreadInfo.proto\x1a\x18tbclient/PbContent.proto\x1a\x18tbclient/PbPostZan.proto\x1a\x18tbclient/PbPresent.proto\x1a\x1ctbclient/SignatureData.proto\x1a\x1atbclient/SimpleForum.proto\x1a\x17tbclient/SkinInfo.proto\x1a\x16tbclient/SubPost.proto\x1a\x19tbclient/TPointPost.proto\x1a\x17tbclient/TailInfo.proto\x1a\x19tbclient/TogetherHi.proto\x1a\x13tbclient/User.proto\x1a\x18tbclient/VideoInfo.proto\x1a\x12tbclient/Zan.proto\"\xd8\t\n\x04Post\x12#\n\x08\x61\x63t_post\x18\x1b \x01(\x0b\x32\x11.tbclient.ActPost\x12,\n\radd_post_list\x18\x10 \x01(\x0b\x32\x15.tbclient.AddPostList\x12\x17\n\x0f\x61\x64\x64_post_number\x18\x14 \x01(\r\x12\x1e\n\x05\x61gree\x18% \x01(\x0b\x32\x0f.tbclient.Agree\x12\x11\n\tarr_video\x18\x06 \x03(\t\x12\x1e\n\x06\x61uthor\x18\x17 \x01(\x0b\x32\x0e.tbclient.User\x12\x11\n\tauthor_id\x18\x13 \x01(\x03\x12\x10\n\x08\x62img_url\x18\x11 \x01(\t\x12$\n\x07\x63ontent\x18\x05 \x03(\x0b\x32\x13.tbclient.PbContent\x12%\n\text_tails\x18  \x03(\x0b\x32\x12.tbclient.TailInfo\x12\r\n\x05\x66loor\x18\x03 \x01(\r\x12)\n\nfrom_forum\x18& \x01(\x0b\x32\x15.tbclient.SimpleForum\x12+\n\rhigh_together\x18! \x01(\x0b\x32\x14.tbclient.TogetherHi\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x16\n\x0eimg_num_abtest\x18) \x01(\x05\x12\x17\n\x0fios_bimg_format\x18\x12 \x01(\t\x12\x0e\n\x06is_bub\x18\x0b \x01(\r\x12\x0f\n\x07is_fold\x18+ \x01(\x05\x12\x13\n\x0bis_hot_post\x18\x1f \x01(\x05\x12\x11\n\tis_ntitle\x18\n \x01(\r\x12\x17\n\x0fis_post_visible\x18\' \x01(\x05\x12\x10\n\x08is_voice\x18\t \x01(\r\x12\x0f\n\x07is_vote\x18\x08 \x01(\r\x12\x1f\n\x08lbs_info\x18\x07 \x01(\x0b\x32\r.tbclient.Lbs\x12\x11\n\tlego_card\x18$ \x01(\t\x12\x10\n\x08need_log\x18( \x01(\x05\x12\x36\n\x12origin_thread_info\x18* \x01(\x0b\x32\x1a.tbclient.OriginThreadInfo\x12(\n\x0cpb_deal_info\x18# \x01(\x0b\x32\x12.tbclient.DealInfo\x12%\n\x08post_zan\x18\x1e \x01(\x0b\x32\x13.tbclient.PbPostZan\x12$\n\x07present\x18\x1c \x01(\x0b\x32\x13.tbclient.PbPresent\x12*\n\tsignature\x18\x15 \x01(\x0b\x32\x17.tbclient.SignatureData\x12%\n\tskin_info\x18\" \x01(\x0b\x32\x12.tbclient.SkinInfo\x12\x12\n\nstorecount\x18\x19 \x01(\x05\x12(\n\rsub_post_list\x18\x0f \x01(\x0b\x32\x11.tbclient.SubPost\x12\x17\n\x0fsub_post_number\x18\r \x01(\r\x12%\n\ttail_info\x18\x16 \x01(\x0b\x32\x12.tbclient.TailInfo\x12\x0c\n\x04time\x18\x04 \x01(\r\x12\x0f\n\x07time_ex\x18\x0e \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12)\n\x0btpoint_post\x18\x1a \x01(\x0b\x32\x14.tbclient.TPointPost\x12\'\n\nvideo_info\x18\x1d \x01(\x0b\x32\x13.tbclient.VideoInfo\x12\x12\n\nvote_crypt\x18\x0c \x01(\t\x12\x1a\n\x03zan\x18\x18 \x01(\x0b\x32\r.tbclient.Zan')
  ,
  dependencies=[tbclient_dot_ActPost__pb2.DESCRIPTOR,tbclient_dot_AddPostList__pb2.DESCRIPTOR,tbclient_dot_Agree__pb2.DESCRIPTOR,tbclient_dot_DealInfo__pb2.DESCRIPTOR,tbclient_dot_Lbs__pb2.DESCRIPTOR,tbclient_dot_OriginThreadInfo__pb2.DESCRIPTOR,tbclient_dot_PbContent__pb2.DESCRIPTOR,tbclient_dot_PbPostZan__pb2.DESCRIPTOR,tbclient_dot_PbPresent__pb2.DESCRIPTOR,tbclient_dot_SignatureData__pb2.DESCRIPTOR,tbclient_dot_SimpleForum__pb2.DESCRIPTOR,tbclient_dot_SkinInfo__pb2.DESCRIPTOR,tbclient_dot_SubPost__pb2.DESCRIPTOR,tbclient_dot_TPointPost__pb2.DESCRIPTOR,tbclient_dot_TailInfo__pb2.DESCRIPTOR,tbclient_dot_TogetherHi__pb2.DESCRIPTOR,tbclient_dot_User__pb2.DESCRIPTOR,tbclient_dot_VideoInfo__pb2.DESCRIPTOR,tbclient_dot_Zan__pb2.DESCRIPTOR,])




_POST = _descriptor.Descriptor(
  name='Post',
  full_name='tbclient.Post',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='act_post', full_name='tbclient.Post.act_post', index=0,
      number=27, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_post_list', full_name='tbclient.Post.add_post_list', index=1,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='add_post_number', full_name='tbclient.Post.add_post_number', index=2,
      number=20, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='agree', full_name='tbclient.Post.agree', index=3,
      number=37, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='arr_video', full_name='tbclient.Post.arr_video', index=4,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author', full_name='tbclient.Post.author', index=5,
      number=23, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='author_id', full_name='tbclient.Post.author_id', index=6,
      number=19, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bimg_url', full_name='tbclient.Post.bimg_url', index=7,
      number=17, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='content', full_name='tbclient.Post.content', index=8,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ext_tails', full_name='tbclient.Post.ext_tails', index=9,
      number=32, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='floor', full_name='tbclient.Post.floor', index=10,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='from_forum', full_name='tbclient.Post.from_forum', index=11,
      number=38, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='high_together', full_name='tbclient.Post.high_together', index=12,
      number=33, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='id', full_name='tbclient.Post.id', index=13,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='img_num_abtest', full_name='tbclient.Post.img_num_abtest', index=14,
      number=41, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='ios_bimg_format', full_name='tbclient.Post.ios_bimg_format', index=15,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_bub', full_name='tbclient.Post.is_bub', index=16,
      number=11, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_fold', full_name='tbclient.Post.is_fold', index=17,
      number=43, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_hot_post', full_name='tbclient.Post.is_hot_post', index=18,
      number=31, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_ntitle', full_name='tbclient.Post.is_ntitle', index=19,
      number=10, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_post_visible', full_name='tbclient.Post.is_post_visible', index=20,
      number=39, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_voice', full_name='tbclient.Post.is_voice', index=21,
      number=9, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_vote', full_name='tbclient.Post.is_vote', index=22,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lbs_info', full_name='tbclient.Post.lbs_info', index=23,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lego_card', full_name='tbclient.Post.lego_card', index=24,
      number=36, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_log', full_name='tbclient.Post.need_log', index=25,
      number=40, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='origin_thread_info', full_name='tbclient.Post.origin_thread_info', index=26,
      number=42, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='pb_deal_info', full_name='tbclient.Post.pb_deal_info', index=27,
      number=35, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='post_zan', full_name='tbclient.Post.post_zan', index=28,
      number=30, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='present', full_name='tbclient.Post.present', index=29,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='signature', full_name='tbclient.Post.signature', index=30,
      number=21, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='skin_info', full_name='tbclient.Post.skin_info', index=31,
      number=34, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='storecount', full_name='tbclient.Post.storecount', index=32,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_post_list', full_name='tbclient.Post.sub_post_list', index=33,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='sub_post_number', full_name='tbclient.Post.sub_post_number', index=34,
      number=13, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tail_info', full_name='tbclient.Post.tail_info', index=35,
      number=22, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time', full_name='tbclient.Post.time', index=36,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='time_ex', full_name='tbclient.Post.time_ex', index=37,
      number=14, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='title', full_name='tbclient.Post.title', index=38,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='tpoint_post', full_name='tbclient.Post.tpoint_post', index=39,
      number=26, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='video_info', full_name='tbclient.Post.video_info', index=40,
      number=29, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='vote_crypt', full_name='tbclient.Post.vote_crypt', index=41,
      number=12, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='zan', full_name='tbclient.Post.zan', index=42,
      number=24, type=11, cpp_type=10, label=1,
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
  serialized_start=517,
  serialized_end=1757,
)

_POST.fields_by_name['act_post'].message_type = tbclient_dot_ActPost__pb2._ACTPOST
_POST.fields_by_name['add_post_list'].message_type = tbclient_dot_AddPostList__pb2._ADDPOSTLIST
_POST.fields_by_name['agree'].message_type = tbclient_dot_Agree__pb2._AGREE
_POST.fields_by_name['author'].message_type = tbclient_dot_User__pb2._USER
_POST.fields_by_name['content'].message_type = tbclient_dot_PbContent__pb2._PBCONTENT
_POST.fields_by_name['ext_tails'].message_type = tbclient_dot_TailInfo__pb2._TAILINFO
_POST.fields_by_name['from_forum'].message_type = tbclient_dot_SimpleForum__pb2._SIMPLEFORUM
_POST.fields_by_name['high_together'].message_type = tbclient_dot_TogetherHi__pb2._TOGETHERHI
_POST.fields_by_name['lbs_info'].message_type = tbclient_dot_Lbs__pb2._LBS
_POST.fields_by_name['origin_thread_info'].message_type = tbclient_dot_OriginThreadInfo__pb2._ORIGINTHREADINFO
_POST.fields_by_name['pb_deal_info'].message_type = tbclient_dot_DealInfo__pb2._DEALINFO
_POST.fields_by_name['post_zan'].message_type = tbclient_dot_PbPostZan__pb2._PBPOSTZAN
_POST.fields_by_name['present'].message_type = tbclient_dot_PbPresent__pb2._PBPRESENT
_POST.fields_by_name['signature'].message_type = tbclient_dot_SignatureData__pb2._SIGNATUREDATA
_POST.fields_by_name['skin_info'].message_type = tbclient_dot_SkinInfo__pb2._SKININFO
_POST.fields_by_name['sub_post_list'].message_type = tbclient_dot_SubPost__pb2._SUBPOST
_POST.fields_by_name['tail_info'].message_type = tbclient_dot_TailInfo__pb2._TAILINFO
_POST.fields_by_name['tpoint_post'].message_type = tbclient_dot_TPointPost__pb2._TPOINTPOST
_POST.fields_by_name['video_info'].message_type = tbclient_dot_VideoInfo__pb2._VIDEOINFO
_POST.fields_by_name['zan'].message_type = tbclient_dot_Zan__pb2._ZAN
DESCRIPTOR.message_types_by_name['Post'] = _POST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Post = _reflection.GeneratedProtocolMessageType('Post', (_message.Message,), dict(
  DESCRIPTOR = _POST,
  __module__ = 'tbclient.Post_pb2'
  # @@protoc_insertion_point(class_scope:tbclient.Post)
  ))
_sym_db.RegisterMessage(Post)


# @@protoc_insertion_point(module_scope)
