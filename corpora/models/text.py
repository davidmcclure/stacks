

from django.db import models


class Text(models.Model):


    corpus = models.ForeignKey('Corpus')


    # Dublin Core - Library Application Profile
    # http://dublincore.org/documents/library-application-profile/


    title = models.TextField(null=True)
    alternative = models.TextField(null=True)
    creator = models.TextField(null=True)
    contributor = models.TextField(null=True)
    publisher = models.TextField(null=True)
    subject = models.TextField(null=True)
    description = models.TextField(null=True)
    abstract = models.TextField(null=True)
    date = models.TextField(null=True)
    created = models.TextField(null=True)
    valid = models.TextField(null=True)
    available = models.TextField(null=True)
    issued = models.TextField(null=True)
    modified = models.TextField(null=True)
    dateCopyrighted = models.TextField(null=True)
    dateSubmitted = models.TextField(null=True)
    dateAccepted = models.TextField(null=True)
    dateCaptured = models.TextField(null=True)
    type = models.TextField(null=True)
    format = models.TextField(null=True)
    extent = models.TextField(null=True)
    medium = models.TextField(null=True)
    identifier = models.TextField(null=True)
    bibliographicCitation = models.TextField(null=True)
    source = models.TextField(null=True)
    language = models.TextField(null=True)
    relation = models.TextField(null=True)
    isVersionOf = models.TextField(null=True)
    isFormatOf = models.TextField(null=True)
    hasFormat = models.TextField(null=True)
    isReplacedBy = models.TextField(null=True)
    replaces = models.TextField(null=True)
    isPartOf = models.TextField(null=True)
    hasPart = models.TextField(null=True)
    requires = models.TextField(null=True)
    isReferencedBy = models.TextField(null=True)
    references = models.TextField(null=True)
    coverage = models.TextField(null=True)
    spatial = models.TextField(null=True)
    temporal = models.TextField(null=True)
    rights = models.TextField(null=True)
    audience = models.TextField(null=True)
    edition = models.TextField(null=True)
    location = models.TextField(null=True)
