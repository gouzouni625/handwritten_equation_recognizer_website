from django.db import models

class Sample(models.Model):
    """
    Stores the symbol samples provided by the users
    """

    id = models.AutoField("id", primary_key=True)
    xml = models.TextField("xml", null=False, blank=False, help_text="The xml data of the sample")
    label = models.IntegerField("label", null=False, blank=False, help_text="The label of the"
                                                                            "sample")
    label_literal = models.TextField("label literal", null=False, blank=False,
                                     help_text="Human readable format of the label")
