from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel

user = settings.AUTH_USER_MODEL
commment_lenght = settings.COMMENT_LENGTH


# Entity Comment
class Comment(TimeStampedModel):
    """
    Text comment posted by users
    """

    # User - Foreign key
    user = models.ForeignKey(user, blank=False, null=False, related_name='comment_user')
    # Parent comment (optional) - i.e. a comment of a comment
    starting_comment = models.ForeignKey('Comment', blank=True, null=True, related_name='parent_comment')
    # Text content of a comment
    content = models.TextField(_('comment text'), max_length=commment_lenght, blank=False, null=False)

    class Meta:
        verbose_name = _('comment')
        verbose_name_plural = _('comments')

    def __unicode__(self):
        return self.content

    def get_content(self):
        "Returns the text content for the comment"
        return self.content

    def get_user_id(self):
        "Returns the id of the user who posted the comment"
        return self.comment_user.pk

    def get_date(self):
        "Returns the timestamp associated to the comment"
        return self.created

    def get_parent_comment_id(self):
        "Returns the id of the parent comment"
        return self.parent_comment.pk


    def set_parent_comment(parent_comment):
        self.starting_comment = parent_comment


# Entity Cigarette
class Cigarette(models.Model):
    """
    Cigarette smoked by a user
    """

    # User - Foreign key
    user = models.ForeignKey(user, blank=False, null=False, related_name='user_cigarettes')
    # Date and time associated to the cigarette
    cigarette_date = models.DateField(_('cigarette date'), auto_now_add=True)
    cigarette_time = models.TimeField(_('cigarette time'), auto_now_add=True)

    class Meta:
        verbose_name = _('cigarette')
        verbose_name_plural = _('cigarettes')

    def __unicode__(self):
        return u'%s' % ( self.pk)


    def get_cigarette_user_id(self):
        "Returns the user id who smoked the cigarette"
        return self.cigarette_user.pk

    def get_date(self):
        "Returns the date associated to the cigarette"
        return self.cigarette_date

    def get_time(self):
        "Returns the time associated to the cigarette"
        return self.cigarette_time


