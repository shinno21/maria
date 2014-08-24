# -*- coding: utf-8 -*-
from django.db import models
import choices

class Court(models.Model):
    """
    コートマスタ
    """
    name = models.CharField(u"コート名称", max_length=100)
    url = models.CharField(u"コートURL", max_length=300, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Schedule(models.Model):
    """
    スケジュール
    """
    event_date = models.DateField(u"開催日")
    start_time = models.TimeField(u"開始時間")
    end_time = models.TimeField(u"終了時間")
    court_id = models.OneToOneField(Court, verbose_name=u"コートID")
    court_other = models.CharField(u"その他コート", max_length=100, null=True)
    court_other_url = models.CharField(u"その他コートURL", max_length=300, null=True)
    party_flg = models.BooleanField(u"飲み会有無")
    status = models.CharField(u"状態", max_length=1, choices=choices.STATUS_CHOICES)
    game_type = models.CharField(u"ゲーム種別", max_length=1, choices=choices.GAME_TYPE)

    def __unicode__(self):
        return self.event_date.strftime("%m/%d(%a.)") + " " \
               + self.start_time.strftime("%H:%M") + "-" + self.end_time.strftime("%H:%M")

    class Meta:
        ordering = ['event_date', 'start_time', 'end_time']


class Visitor(models.Model):
    """
    相手チーム
    """
    name = models.CharField(u"相手チーム名", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


class VisitorSchedule(models.Model):
    """
    スケジュール相手チーム情報
    """
    schedule_id = models.ForeignKey(Schedule, verbose_name=u"スケジュールID")
    visitor_id = models.ForeignKey(Visitor, verbose_name=u"相手チームID")
    number = models.IntegerField(u"参加人数")
    note = models.CharField(u"備考", max_length=100)

    class Meta:
        ordering = ['schedule_id', 'visitor_id']


class Member(models.Model):
    """
    メンバー
    """
    name = models.CharField(u"名前", max_length=20)

    def __unicode__(self):
        return self.name


    class Meta:
        ordering = ['name']



class Participants(models.Model):
    """
    自チーム参加者
    """
    schedule_id = models.ForeignKey(Schedule, verbose_name=u"スケジュールID")
    member_id = models.ForeignKey(Member, verbose_name=u"メンバー")


    class Meta:
        ordering = ['schedule_id', 'member_id']

