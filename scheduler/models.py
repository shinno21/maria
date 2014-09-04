# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import choices


class Court(models.Model):
    """
    コートマスタ
    """
    name = models.CharField(u"コート名称", max_length=100)
    url = models.CharField(u"コートURL", max_length=300, blank=True, null=True)
    station = models.CharField(u"最寄り駅", max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Visitor(models.Model):
    """
    相手チーム
    """
    name = models.CharField(u"相手チーム名", max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']


#class Member(models.Model):
#    """
#    メンバー
#    """
#    name = models.CharField(u"名前", max_length=20)

#    def __unicode__(self):
#        return self.name

#    class Meta:
#        ordering = ['name']


class Schedule(models.Model):
    """
    スケジュールtest
    """
    event_date = models.DateField(u"開催日")
    start_time = models.TimeField(u"開始時間", blank=True, null=True)
    end_time = models.TimeField(u"終了時間", blank=True, null=True)
    court = models.ForeignKey(Court, verbose_name=u"コート", blank=True, null=True)
    court_other = models.CharField(u"その他コート", max_length=100, blank=True, null=True)
    court_other_url = models.CharField(u"その他コートURL", max_length=300, blank=True, null=True)
    party_flg = models.BooleanField(u"飲み会有無")
    status = models.CharField(u"状態", max_length=1, choices=choices.STATUS_CHOICES, blank=True, null=True)
    game_type = models.CharField(u"ゲーム種別", max_length=1, choices=choices.GAME_TYPE, blank=True, null=True)
    comment = models.CharField(u"コメント", max_length=200, blank=True, null=True)

    def __unicode__(self):

        #todo 後でリファクタ必要そう
        if self.start_time:
            s_time = self.start_time.strftime("%H:%M")
        else:
            s_time = ""

        if self.end_time:
            e_time = self.end_time.strftime("%H:%M")
        else:
            e_time = ""
        # この辺りまで

        return self.event_date.strftime("%m/%d(%a.)") + " " \
               + s_time + u" 〜 " + e_time

    class Meta:
        ordering = ['event_date', 'start_time', 'end_time']


class VisitorSchedule(models.Model):
    """
    スケジュール相手チーム情報
    """
    schedule = models.ForeignKey(Schedule, verbose_name=u"スケジュールID")
    visitor = models.ForeignKey(Visitor, verbose_name=u"相手チームID")
    number = models.IntegerField(u"参加人数", blank=True, null=True)
    note = models.CharField(u"備考", max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ['schedule', 'visitor']
        ordering = ['schedule', 'visitor']


class MemberSchedule(models.Model):
    """
    自チーム参加者
    """
    schedule = models.ForeignKey(Schedule, verbose_name=u"スケジュールID")
    member = models.ForeignKey(User, verbose_name=u"メンバー")
    notes = models.CharField(u"備考", max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ['schedule', 'member']
        ordering = ['schedule', 'member']


class HelperSchedule(models.Model):
    """
    助っ人
    """
    schedule = models.ForeignKey(Schedule, verbose_name=u"スケジュールID")
    name = models.CharField(u"助っ人名", max_length=20)
    notes = models.CharField(u"備考", max_length=100, blank=True, null=True)

    class Meta:
        unique_together = ['schedule', 'name']
        ordering = ['schedule', 'name']
