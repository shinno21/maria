# -*- coding: utf-8 -*-
from django.db import models

class Court(models.Model):
    """
    コートマスタ
    """
    name = models.CharField(u"コート名称", max_length=100)
    url = models.CharField(u"コートURL", max_length=300)

    def __unicode__(self):
        return self.name


class Schedule(models.Model):
    """
    スケジュール
    """
    event_date = models.DateField(u"開催日")
    start_time = models.TimeField(u"開始時間")
    end_time = models.TimeField(u"終了時間")
    court_id = models.OneToOneField(Court, verbose_name=u"コートID")
    court_other = models.CharField(u"その他コート", max_length=100, null=True)
    court_other_url = models.CharField(u"その他コート", max_length=300, null=True)
    party_flg = models.BooleanField(u"飲み会有無")

    def __unicode__(self):
        return str(self.event_date).format("MM/DD")


class Visitor(models.Model):
    """
    相手チーム
    """
    name = models.CharField(u"相手チーム名", max_length=100)

    def __unicode__(self):
        return self.name


class VisitorSchedule(models.Model):
    """
    スケジュール相手チーム情報
    """
    schedule_id = models.ForeignKey(Schedule, verbose_name=u"スケジュールID")
    visitor_id = models.ForeignKey(Visitor, verbose_name=u"相手チームID")
    number = models.IntegerField(u"参加人数")


class Member(models.Model):
    """
    メンバー
    """
    name = models.CharField(u"名前", max_length=20)

    def __unicode__(self):
        return self.name


class NumberOfParticipants(models.Model):
    """
    自チーム参加者
    """
    schedule_id = models.ForeignKey(Schedule, verbose_name=u"スケジュールID")
    member_id = models.ForeignKey(Member, verbose_name=u"メンバー")

