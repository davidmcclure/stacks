

from django.db import models


class Text(models.Model):


    corpus = models.ForeignKey('Corpus')


    # The raw, unmodified representation of the text.
    source_text = models.TextField()

    # Plain text extracted from the source markup.
    plain_text = models.TextField(null=True)


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
    date_copyrighted = models.TextField(null=True)
    date_submitted = models.TextField(null=True)
    date_accepted = models.TextField(null=True)
    date_captured = models.TextField(null=True)
    type = models.TextField(null=True)
    format = models.TextField(null=True)
    extent = models.TextField(null=True)
    medium = models.TextField(null=True)
    identifier = models.TextField(null=True)
    bibliographic_citation = models.TextField(null=True)
    source = models.TextField(null=True)
    language = models.TextField(null=True)
    relation = models.TextField(null=True)
    is_version_of = models.TextField(null=True)
    is_format_of = models.TextField(null=True)
    has_format = models.TextField(null=True)
    is_replaced_by = models.TextField(null=True)
    replaces = models.TextField(null=True)
    is_part_of = models.TextField(null=True)
    has_part = models.TextField(null=True)
    requires = models.TextField(null=True)
    is_referenced_by = models.TextField(null=True)
    references = models.TextField(null=True)
    coverage = models.TextField(null=True)
    spatial = models.TextField(null=True)
    temporal = models.TextField(null=True)
    rights = models.TextField(null=True)
    audience = models.TextField(null=True)
    edition = models.TextField(null=True)
    location = models.TextField(null=True)
