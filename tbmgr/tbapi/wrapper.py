# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 xfgryujk <xfgryujk@126.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""提供高级的贴吧API
"""

from datetime import datetime
from typing import List, Tuple

from sqlalchemy import (
    Table, Column, Sequence, ForeignKey, Unicode, UnicodeText, Integer, DateTime, Boolean
)
from sqlalchemy.orm import relationship

from .tbclient import TbClient
from .tbtypes import IThread, IPost, ISubPost, Thread, Post, SubPost
from .utils import cached
from ..utils.database import OrmBase, Session


class User(OrmBase):
    __tablename__ = 'users'
    id          = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    name        = Column(Unicode(20), nullable=False, unique=True, index=True)
    show_name   = Column(Unicode(20), nullable=False, index=True)  # 由于昵称可以改，而且爬取时间和百度更新时间不一样，无法保证唯一
    portrait    = Column(Unicode(64), nullable=False)
    update_time = Column(DateTime, index=True)  # 爬取时间


_forum_threads = Table(
    'forum_threads', OrmBase.metadata,
    Column('forum_id', ForeignKey('forums.id'), primary_key=True),
    Column('thread_id', ForeignKey('threads.id'), primary_key=True)
)


class Forum(OrmBase):
    __tablename__ = 'forums'
    id                         = Column(Integer, Sequence('forum_id_seq'), primary_key=True)
    name                       = Column(Unicode(50), nullable=False, unique=True, index=True)  # 我也不知道长度50够不够
    threads: List['OrmThread'] = relationship('OrmThread', secondary=_forum_threads, back_populates='forums')


class ForumUserInfo(OrmBase):
    __tablename__ = 'forum_user_info'
    fid          = Column(Integer, ForeignKey(Forum.id), primary_key=True)
    forum: Forum = relationship(Forum)
    uid          = Column(Integer, ForeignKey(User.id), primary_key=True)
    user: User   = relationship(User)
    level        = Column(Integer)  # 首页无法获取等级，所以可以为null


class ForumThreadInfo(OrmBase):
    __tablename__ = 'forum_thread_info'
    fid                 = Column(Integer, ForeignKey(Forum.id), primary_key=True)
    forum: Forum        = relationship(Forum)
    tid                 = Column(Integer, ForeignKey('threads.id'), primary_key=True)
    thread: 'OrmThread' = relationship('OrmThread')
    is_deleted          = Column(Boolean, nullable=False, default=False)


class ForumPostInfo(OrmBase):
    __tablename__ = 'forum_post_info'
    fid             = Column(Integer, ForeignKey(Forum.id), primary_key=True)
    forum: Forum    = relationship(Forum)
    tid             = Column(Integer, ForeignKey('posts.id'), primary_key=True)
    post: 'OrmPost' = relationship('OrmPost')
    is_deleted      = Column(Boolean, nullable=False, default=False)


class ForumSubPostInfo(OrmBase):
    __tablename__ = 'forum_sub_post_info'
    fid                    = Column(Integer, ForeignKey(Forum.id), primary_key=True)
    forum: Forum           = relationship(Forum)
    tid                    = Column(Integer, ForeignKey('sub_posts.id'), primary_key=True)
    sub_post: 'OrmSubPost' = relationship('OrmSubPost')
    is_deleted             = Column(Boolean, nullable=False, default=False)


# TODO 相关数据不存在时的错误处理
# TODO 爬取Forum, User的信息
# TODO 爬取帖子时更新信息


class OrmThread(OrmBase, IThread):
    __tablename__ = 'threads'
    id                     = Column(Integer, Sequence('thread_id_seq'), primary_key=True)
    fid                    = Column(Integer, ForeignKey(Forum.id), nullable=False)
    forums: List[Forum]    = relationship(Forum, secondary=_forum_threads, back_populates='threads')
    author_id_             = Column('author_id', Integer, ForeignKey(User.id), nullable=False, index=True)
    author: User           = relationship(User, foreign_keys=author_id_)
    create_time_: datetime = Column('create_time', DateTime, index=True)
    title_                 = Column('title', Unicode(35), nullable=False)
    abstract_              = Column('abstract', UnicodeText, nullable=False)
    last_responder_id_     = Column('last_responder_id', Integer, ForeignKey(User.id), nullable=False)
    last_responder: User   = relationship(User, foreign_keys=last_responder_id_)
    n_reply_               = Column('n_reply', Integer, nullable=False)  # 这是爬取得到的回复数，不代表数据库中存的回复数
    update_time            = Column(DateTime, nullable=False, index=True)  # 爬取时间
    posts: List['OrmPost'] = relationship('OrmPost', back_populates='thread')

    # 这个方法用来让静态检查工具闭嘴
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_thread(cls, raw: Thread):
        """需要自己调用session.add(), session.commit()
        """
        session = Session()
        thread = session.query(cls).filter(cls.id == raw.tid).one_or_none()
        if thread is None:
            thread = cls(
                id=raw.tid,
                fid=raw.raw.fid,
                author_id_=raw.author_id,
                create_time_=raw.create_time,
                title_=raw.title,
                abstract_=raw.abstract,
                last_responder_id_=raw.last_responder_id,
                n_reply_=raw.n_reply,
                update_time=datetime.now()
            )
        return thread

    @property
    def tid(self):
        return self.id

    @property
    def author_id(self):
        return self.author_id_

    @property
    def author_name(self):
        return self.author.name

    @property
    def author_show_name(self):
        return self.author.show_name

    @property
    def author_portrait_url(self):
        return self.PORTRAIT_URL_PREFIX + self.author.portrait

    @property
    def create_time(self) -> datetime:
        return self.create_time_

    @property
    def title(self):
        return self.title_

    @property
    def abstract(self):
        return self.abstract_

    @property
    def last_responder_id(self):
        return self.last_responder_id_

    @property
    def last_responder_name(self):
        return self.last_responder.name

    @property
    def last_responder_show_name(self):
        return self.last_responder.show_name

    @property
    def n_reply(self):
        return self.n_reply_


class OrmPost(OrmBase, IPost):
    __tablename__ = 'posts'
    id                     = Column(Integer, Sequence('post_id_seq'), primary_key=True)
    tid_                   = Column('tid', Integer, ForeignKey(OrmThread.id), nullable=False, index=True)
    thread: OrmThread      = relationship(OrmThread, back_populates='posts')
    author_id_             = Column('author_id', Integer, ForeignKey(User.id), nullable=False, index=True)
    author: User           = relationship(User)
    create_time_: datetime = Column('create_time', DateTime, index=True)
    html_content_          = Column('content', UnicodeText, nullable=False)
    floor_                 = Column('floor', Integer, nullable=False)
    n_sub_posts_           = Column('n_sub_posts', Integer, nullable=False)  # 这是爬取得到的评论数，不代表数据库中存的评论数
    update_time            = Column(DateTime, nullable=False, index=True)  # 爬取时间
    sub_posts: List['OrmSubPost'] = relationship('OrmSubPost', back_populates='post')

    # 这个方法用来让静态检查工具闭嘴
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_post(cls, raw: Post):
        """需要自己调用session.add(), session.commit()
        """
        session = Session()
        post = session.query(cls).filter(cls.id == raw.pid).one_or_none()
        if post is None:
            post = cls(
                id=raw.pid,
                tid_=raw.tid,
                author_id_=raw.author_id,
                create_time_=raw.create_time,
                html_content_=raw.html_content,
                floor_=raw.floor,
                n_sub_posts_=raw.n_sub_posts,
                update_time=datetime.now()
            )
        return post

    @property
    def tid(self):
        return self.id

    @property
    def author_id(self):
        return self.author_id_

    @property
    def author_name(self):
        return self.author.name

    @property
    def author_show_name(self):
        return self.author.show_name

    @property
    def author_portrait_url(self):
        return self.PORTRAIT_URL_PREFIX + self.author.portrait

    @property
    def create_time(self) -> datetime:
        return self.create_time_

    @property
    @cached
    def html_content(self):
        return self.html_content_

    @property
    def pid(self):
        return self.id

    @property
    def floor(self):
        return self.floor_

    @property
    @cached
    def author_level(self):
        session = Session()
        return session.query(ForumUserInfo.level).filter(
            ForumUserInfo.fid == OrmThread.fid, OrmThread.id == self.tid,
            ForumUserInfo.uid == self.author_id
        ).scalar()

    @property
    def n_sub_posts(self):
        return self.n_sub_posts_


class OrmSubPost(OrmBase, ISubPost):
    __tablename__ = 'sub_posts'
    id                     = Column(Integer, Sequence('sub_post_id_seq'), primary_key=True)
    pid_                   = Column('pid', Integer, ForeignKey(OrmPost.id), nullable=False, index=True)
    post: OrmPost          = relationship(OrmPost, back_populates='sub_posts')
    author_id_             = Column('author_id', Integer, ForeignKey(User.id), nullable=False, index=True)
    author: User           = relationship(User)
    create_time_: datetime = Column('create_time', DateTime, index=True)
    html_content_          = Column('content', UnicodeText, nullable=False)  # TODO 决定长度
    update_time            = Column(DateTime, nullable=False, index=True)  # 爬取时间

    # 这个方法用来让静态检查工具闭嘴
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def from_sub_post(cls, raw: SubPost):
        """需要自己调用session.add(), session.commit()
        """
        session = Session()
        sub_post = session.query(cls).filter(cls.id == raw.cid).one_or_none()
        if sub_post is None:
            sub_post = cls(
                id=raw.cid,
                pid_=raw.pid,
                author_id_=raw.author_id,
                create_time_=raw.create_time,
                html_content_=raw.html_content,
                update_time=datetime.now()
            )
        return sub_post

    @property
    def tid(self):
        return self.post.thread.id

    @property
    def author_id(self):
        return self.author_id_

    @property
    def author_name(self):
        return self.author.name

    @property
    def author_show_name(self):
        return self.author.show_name

    @property
    def author_portrait_url(self):
        return self.PORTRAIT_URL_PREFIX + self.author.portrait

    @property
    def create_time(self) -> datetime:
        return self.create_time_

    @property
    @cached
    def html_content(self):
        return self.html_content_

    @property
    def cid(self):
        return self.id

    @property
    def pid(self):
        return self.pid_

    @property
    def post_floor(self):
        return self.post.floor

    @property
    def author_level(self):
        session = Session()
        return session.query(ForumUserInfo.level).filter(
            ForumUserInfo.fid == OrmThread.fid, OrmThread.id == self.tid,
            ForumUserInfo.uid == self.author_id
        ).scalar()


class TbClientWrapper(TbClient):
    """带缓存、错误处理、事件、白名单和日志等功能的贴吧API封装
    """

    async def get_threads(self, forum_name, page=1) -> List[OrmThread]:
        # TODO 错误处理
        threads = await super().get_threads(forum_name, page)
        threads = list(map(OrmThread.from_thread, threads))
        session = Session()
        session.add_all(threads)
        session.commit()
        return threads

    async def get_posts(self, fid, tid, page=1, with_sub_post=False
                        ) -> Tuple[List[OrmPost], List[List[OrmSubPost]]]:
        # TODO 错误处理
        posts, sub_posts = await super().get_posts(fid, tid, page, with_sub_post)
        posts = list(map(OrmPost.from_post, posts))
        sub_posts = [list(map(OrmSubPost.from_sub_post, sub_posts_per_post))
                     for sub_posts_per_post in sub_posts]
        session = Session()
        session.add_all(posts)
        for sub_posts_per_post in sub_posts:
            session.add_all(sub_posts_per_post)
        session.commit()
        return posts, sub_posts

    async def get_sub_posts(self, tid, pid, page=1) -> List[OrmSubPost]:
        # TODO 错误处理
        sub_posts = await super().get_sub_posts(tid, pid, page)
        sub_posts = list(map(OrmSubPost.from_sub_post, sub_posts))
        session = Session()
        session.add_all(sub_posts)
        session.commit()
        return sub_posts

    # TODO 白名单、日志


def test():
    from asyncio import get_event_loop

    loop = get_event_loop()
    client = TbClientWrapper({
        'BDUSS': ''
    }, loop)
    loop.run_until_complete(client.init_user_info())
    threads = loop.run_until_complete(client.get_threads('一个极其隐秘只有xfgryujk知道的地方', 1))
    # print(threads[0])
    posts, sub_posts = loop.run_until_complete(client.get_posts(309740, 5010576625, 1, True))
    # print(posts[0])
    # print(sub_posts[2][0])
    sub_posts2 = loop.run_until_complete(client.get_sub_posts(5010576625, 108473589139, 1))
    loop.run_until_complete(client.close())
